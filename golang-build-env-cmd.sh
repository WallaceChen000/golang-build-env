#!/bin/bash
set +e

message() {
    echo "Please run:" >&2
    echo "            $0 build      " >&2
    echo "            $0 run        " >&2
}

build_rootfs() {
    tar -C ./rootfs/ -zcvf rootfs.tar.gz .
}

build_img() {
    build_rootfs;

    build_date=$(date +%Y%m%d%H%M%S)
    docker images --quiet --filter=dangling=true | xargs --no-run-if-empty docker rmi

    echo "Building golang-build-env image"

    docker build -t wallacechendockerhub/golang-build-env:latest . --no-cache -f Dockerfile
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
        -u root -idt wallacechendockerhub/golang-build-env:latest
}

mount_work_dir() {
    umount_work_dir;
    mount -t cifs -v -o domain="WORKGROUP",username="root",password="PmdjwEsUpfS8YAmD" //172.27.13.243/share/go/src/ /go/src
}

umount_work_dir() {
    umount /go/src
}


<<COMMENT
MULTILINE COMMAND
COMMENT

case "$1" in
    build)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
	build_img;
        ;;
    run)
        sleep 1
        if [ "$#" -ne 1 ]; then
            message;
            exit 1
        fi
	run_gbe;
        exit 0
        ;;
    *)
        message;
        exit 1
        ;;
esac
exit 100
