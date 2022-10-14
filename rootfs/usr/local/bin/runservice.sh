#!/bin/bash +e

# [signal catch]
_term() {
    echo "Caught SIGTERM signal!"
    sleep 1
    exit 0;
}
trap _term INT TERM KILL;

curpid="$$"

echo "$0: pid: $curpid"

#mount -t tmpfs -o size=200M,nr_inodes=2k,mode=0777 tmpfs /tmp

# [Time zone]
#rm /etc/localtime && ln -s $TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
rm -r /etc/localtime && ln -s /usr/share/zoneinfo/DefZone /etc/localtime

# [schedule s3 job]
#/usr/local/bin/schedule_s3.sh &


while true; do
    
: <<'END_COMMENT'
    monitor_checker=$(pgrep -f iftmonitor.py)
    if [ -z "$monitor_checker" ] ; then
        python3 /vms/bin/iftmonitor.py &
    fi 
END_COMMENT
    
    sleep 1;
done

