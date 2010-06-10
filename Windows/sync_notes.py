import os, sys, getopt

class SyncNotes:
  '''
  Synchronize Tomboy notes between Windows PC and Maemo / N900 using rsync.
  Kills Tomboy process before synchronizing and restarts it afterwards
  '''

  def __init__(self, options):

    self.WIN_TOMBOY_PATH = "C:\Program Files\Tomboy\Tomboy.exe"
    self.WIN_SYNC_NOTES_BATCH_SCRIPT = "C:\N900\scripts\Windows\_sync_notes.bat"
    self.TOMBOY_PROCESS_NAME = 'tomboy.exe'
    self.PID = self.isrunning()
    self.options = options
    if self.PID != "None":
      print("%s is still running. Please exit the application before syncing." % self.TOMBOY_PROCESS_NAME)
      response = raw_input("Do you want to kill the %s process now (y/n)? (It will be restarted after the sync.) " \
                           % (self.TOMBOY_PROCESS_NAME))
      if response.lower() == 'y':
        self.killTomboy()
        self.run_sync_notes_batch()
        self.startTomboy()
      else:
        print("This script will now exit.")
    else:
      self.run_sync_notes_batch()

  def killTomboy(self):
    os.system(r'taskkill /F /PID ' + self.PID)

  def startTomboy(self):
    os.startfile(self.WIN_TOMBOY_PATH, '')

  def isrunning(self):
    '''
    # Adopted from http://www.daniweb.com/code/snippet228205.html
    Returns the process ID if tomboy is running. If not, returns none.   
    '''
    
    try:
      p = os.popen(r'tasklist /FI "IMAGENAME eq "'+ self.TOMBOY_PROCESS_NAME + ' /FO "LIST" 2>&1' , 'r' )
      PID = p.read().split('\n')[2].split(":")[1].lstrip(" ")
      p.close()
      return PID
    except:
      p.close()
      return "None"

  def run_sync_notes_batch(self):
    batch_args = ""
    for o, a in self.options:
      if  o in ("-d", "--delete"):
        batch_args = batch_args + "--delete"

    os.system(self.WIN_SYNC_NOTES_BATCH_SCRIPT + ' ' + batch_args)

def processCmdLineArgs():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "d", ["delete"])
  except getopt.GetoptError, err:
    print str(err) # will print something like "option -a not recognized"
    sys.exit(2)
  return opts


def main():
  options = processCmdLineArgs()
  syncNotes = SyncNotes(options)

if __name__ == "__main__":
  sys.exit(main())
