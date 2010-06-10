set RSYNC_DIR="C:\Program Files\cwRsync\bin"
set N900_IP=192.168.1.100
set PC_NOTES_DIR="/cygdrive/C/Documents and Settings/%USERNAME%/Application Data/Tomboy/notes/"

pushd .

cd %RSYNC_DIR%

rsync -rulD %1 --progress %PC_NOTES_DIR% --include=*.notes --exclude=Backup %N900_IP%::notes
rsync -rulD --progress %N900_IP%::notes --include=*.notes --exclude=Backup %PC_NOTES_DIR% 

popd

pause