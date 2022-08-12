#!/bin/bash
DATE=`date +%y_%m_%d`
INFOLOG=$DATE_${HOSTNAME}
./monitoring.sh > /root/$INFOLOG.info

MASTER=$(cat /root/masterip)


sshpass -p root scp /root/$INFOLOG.info root@$MASTER:/root/result 
