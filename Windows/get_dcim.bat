set RSYNC="C:\Program Files\cwRsync\bin\rsync"
set N900_IP=192.168.1.100

%RSYNC% -az --progress shing@%N900_IP%::camera "/cygdrive/C/N900/DCIM"