#!/usr/bin/python

'''
Script to move pictures and videos in DCIM into sub-folders (e.g. 2010-03, 2010-04, etc).
This is to be called by rsyncd.conf in pre-xfer

/home/user/scripts/folderize.py
'''

import os, datetime
from stat import *

# The DCIM directory, where the pictures and videos are
# stored by the N900
dcim = "/home/user/MyDocs/DCIM/"

# The DCIM directory protection mode
dcimProtMode = os.stat(dcim).st_mode

# Picture or video file extensions
pic_vid_extensions = ['.jpg', '.png', '.mp4', '.avi', '.mov']

def isPicOrVid(pathname):
  isPicOrVid = False

  ext = os.path.splitext(pathname)[1].lower()
  if ext in pic_vid_extensions:
    isPicOrVid = True

  return isPicOrVid

for f in os.listdir(dcim):
  pathname = os.path.join(dcim, f)
  mode = os.stat(pathname)[ST_MODE]

  # If it's a file...
  if S_ISREG(mode) and isPicOrVid(pathname):

    # Get the file creation timestamp
    ts = os.stat(pathname).st_ctime
    cTime =  datetime.datetime.fromtimestamp(ts)

    # Create a directory based on file creation date (yyyy-mm)
    # ... if one does not exist yet
    yearMonth = cTime.strftime("%Y-%m")    
    mdDir = os.path.join(dcim, yearMonth)
    if not os.path.exists(mdDir):
      print "Directory %s does not exists. Creating..." % (mdDir)
      os.mkdir(mdDir, dcimProtMode)

    # Move the file from DCIM to the subdirectory created above
    newpathname = os.path.join(mdDir, f)
    print "Moving %s to %s" % (f, mdDir)
    os.rename(pathname, newpathname)
