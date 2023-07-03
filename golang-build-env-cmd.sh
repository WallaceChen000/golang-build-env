#!/bin/bash
set +e

CLEAR='\e[0m'
RED='\033[0;31m'
GREEN='\e[0;32m'
YELLOW='\e[0;33m'
BLUE='\e[0;34m'

# assign default value, if the environment variables are empty
: "${CODE_SERVER_IP:="172.27.13.243"}"
: "${CODE_SERVER_SAMBA_DOMAIN:="WORKGROUP"}"
: "${CODE_SERVER_SAMBA_USER:="root"}"
: "${CODE_SERVER_SAMBA_PASSWD:="PmdjwEsUpfS8YAmD"}"
: "${CODE_SERVER_SAMBA_SHARE_FOLDER:="/share/go/src"}"
: "${TARGET_FOLDER:="/go/src"}"
# The colon builtin (:) ensures the variable result is not executed.
# The double quotes (") prevent globbing and word splitting.

: "${BUILD_SERVER_IP:="172.27.13.243"}"
: "${BUILD_SERVER_PORT:="2224"}"
: "${BUILD_SERVER_PASSWD:="PmdjwEsUpfS8YAmD"}"
: "${BUILD_SERVER_WORKDIR:="/go"}"

: "${BUILD_VER:="20230703"}"

message() {
    echo "Please run:" >&2
    echo "            $0 check                  check packages in the environment.       " 1>&2
    echo "            $0 build                  build golang build-server image.         " >&2
    echo "            $0 run                    run golang build-server container.       " >&2
    echo "            $0 stop                   stop golang build-server container.      " >&2
    echo "            $0 runcmd                 run build server container shell.        " >&2
}

packages_check() {
    packages=("sshfs")
    packages+=("sshpass")
    packages+=("rsync")
    packages+=("pv")
    echo "---"
    echo ${packages[@]}
    apt-get update;
    for i in "${packages[@]}"; do
        echo "---"
        echo "$i"
        dpkg-query -l ${i} 1> /dev/null 2>&1; #echo $?
        #apt list ${i}|grep ${i}; #echo $?   # Don't use apt beacuse of 'WARNING: apt does not have a stable CLI interface. Use with caution in scripts'
        if [ $? -ne 0 ]; then
            apt-get install ${i} -q -yy
        else
            echo "${i} is installed"
        fi
    done
}

build_rootfs() {
    tar -C ./rootfs/ -zcvf rootfs.tar.gz .
}

build_img() {
    build_rootfs;

    build_date=$(date +%Y%m%d%H%M%S)

    docker images --quiet --filter=dangling=true | xargs --no-run-if-empty docker rmi

    echo "Building golang-build-env image"

    docker build -t wallacechendockerhub/golang-build-env:go1.19.5-build${BUILD_VER} . --no-cache -f Dockerfile
}

create_persistent_volume() {
    rcmvol=$(docker volume ls -q|grep -w golang-build-env-data)

    if [[ "$rcmvol" == "golang-build-env-data" ]]; then
        echo "volume: golang-build-env-data is ready!"
    else
        echo "volume: golang-build-env-data is not ready, create it!"
        docker volume create golang-build-env-data
    fi
}

run_gbe() {
    echo "Running gbe container"

    create_persistent_volume;
    docker run --name gbe --net=host \
        --restart unless-stopped \
        --mount 'type=volume,src=golang-build-env-data,dst=/var/lib/golang-build-env-data,volume-driver=local' \
        -v /etc/localtime:/usr/share/zoneinfo/DefZone:ro \
        -v /var/run/docker.sock:/var/run/docker.sock \
        --privileged=true \
        -e TZ=$(readlink /etc/localtime) \
        -u root -idt wallacechendockerhub/golang-build-env:go1.19.5-build${BUILD_VER}
}

stop_gbe() {
    docker stop gbe
}

mount_work_dir() {
    umount_work_dir;
    mount -t cifs -v -o domain=${CODE_SERVER_SAMBA_DOMAIN},username=${CODE_SERVER_SAMBA_USER},password=${CODE_SERVER_SAMBA_PASSWD} \
        //${CODE_SERVER_IP}:${CODE_SERVER_SAMBA_SHARE_FOLDER} ${TARGET_FOLDER}
}

umount_work_dir() {
    umount ${TARGET_FOLDER}
}

run_build_server_cmd() {

    SSHPASS=${BUILD_SERVER_PASSWD} sshpass -e ssh -p ${BUILD_SERVER_PORT} -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -q -t \
        root@${BUILD_SERVER_IP} "cd ${BUILD_SERVER_WORKDIR}; bash"

}

<<COMMENT
MULTILINE COMMAND
COMMENT

case "$1" in
    check)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
        echo -e "${RED}👉 $1${CLEAR}\n";
        packages_check;
        exit 0
        ;;
    build)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
        echo -e "${RED}⌛ $1${CLEAR}\n";
        build_img;
        exit 0
        ;;
    run)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
        echo -e "${RED}👉 $1${CLEAR}\n";
        run_gbe;
        exit 0
        ;;
    stop)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
        echo -e "${RED}👉 $1${CLEAR}\n";
        stop_gbe;
        exit 0
        ;;
    runcmd)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
        echo -e "${RED}👉 $1${CLEAR}\n";
        run_build_server_cmd;
        exit 0
        ;;
    *)
        message;
        exit 1
        ;;
esac
exit 100
