#!/bin/bash

mkdir -p ./logs


# user=`echo $USER`
# if [ "$user" != "root" ]; then
#   echo "Script must be run as root.  Try 'sudo ./start.sh'"
#   exit 1
# fi

sleep=2

echo "starting rotobot"

logfile="./rotobot.log"

if [ -f "$logfile" ]; then
  mv -f "$logfile" "$logfile".1
fi

echo "starting rotobot at $(date)" >> "$logfile"

python3 src/rotobot.py > $logfile 2>&1 &

echo $! > ./rotobot.pid

if [[ $sleep > 0 ]]; then
  echo "sleeping for $sleep seconds"
  sleep $sleep
fi
