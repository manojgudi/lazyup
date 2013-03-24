lazyup
======

script to upload all files in a *web-based* project to ftp server/web-host with following constraints 

-> ftp server provides only FTPES (explicit) access<br>
-> ftp server does NOT provide ssh access<br>
-> your project is handles via git, and everytime you update a site you have to manually update  it on ftp server<br>
-> Server is a LAMP server<br>
-> you're working on *Windows* (which has git-bash 1.8+)<br>


This script requires python2.7 installed, can be hooked up with git so that it uploads as soon as *git push* operation is complete<br>

To Do:

1. Reduce code redundnacy by removing multiple-time logging
2. Upload only patch files instead of whole project(This is a issue which has to be solved by some php script which patches all files on remote_path since server doesnt provide shell access)
3. Remove upload folder from remote_path/upload/ as default upload path
