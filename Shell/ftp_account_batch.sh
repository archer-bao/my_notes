#!/bin/bash

cat ./ftp_account.txt | while read line
do
    if [ "$line" = "" ]
    then
        exit
    fi
    account=`echo $line|awk -F ' '  '{print $1}'`
    password=`echo $line|awk -F ' '  '{print $2}'`
    loginShell=`which nologin`
    useradd $account -s $loginShell -b /home/log/newlog 
    echo "$account:$password"| chpasswd
done
