screen-lapse
============

Little application that captures screenshots and then processes them into a time lapse video

Overview
===========

Couldn't get chronolapse to work on my computer (probably because I have an ARM processor, I guess I could have tried to compile it from source), so i decided to build my own.  I am going to use apscheduler to grab screenshots at regular intervals and then save those into a folder.  Probably use a seperate script to process the files into a time lapse video (not quite sure how I am going to do that part yet).

Requirements
============

This is a small project, so I am not goint to use virtualenv or a requreiments.txt file
- gnome-screenshot: if you dont have this already <code>sudo apt-get install gnome-screenshot</code>
- apscheduler: <code>sudo pip install apscheduler</code>

Setup Instructions
=====================
At the moment it is pretty bare bones.  The gnome-screenshot utility does not provide the opption to pass in a file path at the command line.  So in order to supress the prompt for a save location, you need to set a default file path using something like the CompzigConfig Settings Manager. At the moment, the script will take a screenshot once a minute.  I am looking in to providing some more save options.
