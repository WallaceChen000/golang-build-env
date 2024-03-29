#!/bin/bash
set +e

: "${CODE_SERVER_IP:="172.27.13.243"}"
: "${CODE_SERVER_SAMBA_DOMAIN:="WORKGROUP"}"
: "${CODE_SERVER_SAMBA_USER:="root"}"
: "${CODE_SERVER_SAMBA_PASSWD:="PmdjwEsUpfS8YAmD"}"
: "${CODE_SERVER_SAMBA_SHARE_FOLDER:="/share/go/src"}"
: "${TARGET_FOLDER:="/go/src"}"

: "${BUILD_SERVER_PASSWD:="123456"}"
: "${BUILD_SERVER_PORT:="2700"}"
: "${BUILD_SERVER_IP:="172.27.13.243"}"
: "${BUILD_SERVER_FOLDER:="/srv/samba/share/go/src"}"

message() {
    echo "Please run:" >&2
    echo "            $0 mount                mount /go/src.            " 1>&2
    echo "            $0 umount               umount /go/src.           " 1>&2
}

mount_work_dir() {
    umount_work_dir;
    #mount -t cifs -v -o domain=${CODE_SERVER_SAMBA_DOMAIN},username=${CODE_SERVER_SAMBA_USER},password=${CODE_SERVER_SAMBA_PASSWD} \
    #    //${CODE_SERVER_IP}:${CODE_SERVER_SAMBA_SHARE_FOLDER} ${TARGET_FOLDER}
    echo ${BUILD_SERVER_PASSWD} |sshfs -p ${BUILD_SERVER_PORT} -o password_stdin root@${BUILD_SERVER_IP}:${BUILD_SERVER_FOLDER} ${TARGET_FOLDER} -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no
}

umount_work_dir() {
    umount ${TARGET_FOLDER}
}

case "$1" in
    mount)
        sleep 1
        mount_work_dir;
        exit 0
        ;;
    umount)
        sleep 1
        umount_work_dir;
        exit 0
        ;;
    *)
        message;
        exit 1
        ;;
esac

exit 0
