# pinglist
A Python script to ping list of hostnames or IP addresses from a file. See also https://github.com/onismo/ping-url-speedtest

This script uses https://github.com/kyan001/ping3.

#### Edit file hosts.txt to update list of hostnames or IP addresses. Example...
```
google.com
yahoo.com
cisco.com
1.1.1.1
8.8.8.8
x.x.x.x # this will Fail
```
#### Run command
```
python pinglist.py
```
#### Sample console output, also outputs to a file named results_{date}.log
```
Ping google.com : PASS
Ping yahoo.com : PASS
Ping cisco.com : PASS
Ping 1.1.1.1 : PASS
Ping 8.8.8.8 : PASS
Ping x.x.x.x : FAIL
```
