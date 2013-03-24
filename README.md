lazyup
======

script to upload all files in a *web-based* project to ftp server/web-host with following constraints 

-> ftp server provides only FTPES (explicit) access
-> ftp server does NOT provide ssh access
-> your project is handles via git, and everytime you update a site you have to manually update  it on ftp server
-> Server is a LAMP server
-> you're working on *Windows* (which has git-bash 1.8+)


This script requires python2.7 installed, can be hooked up with git so that it uploads as soon as *git push* operation is complete
