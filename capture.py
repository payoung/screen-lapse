import sys
import os
from apscheduler.scheduler import Scheduler
import time
import glob
import datetime

"""
This script captures screenshots at one minute intervals
TODO:
- Allow user to provide a url via sys.argv and have the program fetch and rename
the files and store the file in a new folder
- Allow user to specify new folder to put files in.  If none is provided (but
an input path is) then create a default path
- Rename files to make them a bit mroe sensible (assuming user provides paths)
"""

sched = Scheduler()

@sched.interval_schedule(minutes=1)
def run_capture():
    os.system("gnome-screenshot")

sched.start()

while True:
    time.sleep(1)
    pass

