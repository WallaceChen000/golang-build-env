#!/bin/bash
set +e

message() {
    echo "Please run:" >&2
    echo "            $0 mount                mount /go/src.            " 1>&2
    echo "            $0 umount               umount /go/src.           " 1>&2
}


mount_work_dir() {
    umount_work_dir;
    mount -t cifs -v -o domain="WORKGROUP",username="root",password="PmdjwEsUpfS8YAmD" //172.27.13.243/share/go/src/ /go/src
}

umount_work_dir() {
    umount /go/src
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
