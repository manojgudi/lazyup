import zipfile
import os
import sys
from ftplib import FTP_TLS

def del_existing_folder(uname, pwd, site,path, remote_path):
    # Connect to ftp site using ftpes
    try:
        ftp = FTP_TLS(site)
    except:
        print "Cannot access ftp site by TLS"
        exit()

    # login to site
    try:
        ftp.login(user=uname, passwd=pwd)
        print 'Login Successful'
    except:
        print list(uname)
        print list(pwd)
        print "Login Failed, abort..."
        exit()

    # Establish secure connection
    ftp.prot_p()
    ftp.storbinary('STOR rmtree.php', open(path+ '\\' +'rmtree.php'))

    # Invoke the script
    import urllib2 as url
    url.urlopen(remote_path + '/rmtree.php') # path must be like  http://www.smscreatives.in/demos i.e. NO extra forwardslash at end
    ftp.delete('rmtree.php')
    
    

def zipfolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        try:
            dirs.remove('.git') # Remove .git sub-directory
        except:
            pass
        for file in files:
            if file == 'file_up.zip' or file == 'lazyup.py' or file == 'credentials.xml' or file == 'rmtree.php':
                pass
            else:    
                fn = os.path.join(base, file)
                print fn
                zipobj.write(fn, fn[rootlen:])

def uploadzip(uname, pwd, site, zip_fn, path):
    # Connect to ftp site using ftpes
    try:
        ftp = FTP_TLS(site)
    except:
        print "Cannot access ftp site by TLS"
        exit()

    # login to site
    try:
        ftp.login(user=uname, passwd=pwd)
        print 'Login Successful'
    except:
        print list(uname)
        print list(pwd)
        print "Login Failed, abort..."
        exit()

    # Establish secure connection
    ftp.prot_p()

    # File uploads in ~/upload/  directory, so remove earlier upload directory if present
    try:
        ftp.rmd('upload')
        print "existing upload folder deleted"
    except:
        pass
        # make new upload directory
    try:
        ftp.mkd('upload')
    except:
        print "Cannot Make Directory, aborting"
        ftp.quit()
        exit()
        
    ftp.cwd('/upload/')
    
    ftp.storbinary("STOR "+zip_fn, open(path + "\\" + zip_fn, 'rb'))  # path must be like c:\users i.e. NO extra backslash at end
    print (zip_fn+' has been uploaded')

    # Upload the unzip_file.php (assuming unzip_file.php is in path)
    ftp.storbinary('STOR unzip.php', open(path+ '\\' +'unzip.php'))
    print ('unzip.php' +' has been uploaded')
    print 'exiting ftp...'
    ftp.quit()


# Invoke that php script
    # Assuming its uploaded to public_html/demo
def unzip_file(remote_path):
    import urllib2 as url
    url.urlopen(remote_path + '/upload/unzip.php') # path must be like  http://www.smscreatives.in/demos i.e. NO extra forwardslash at end

# Reads credentials from xmlfile and returns 3 values, username, password, remotepath
def getdata(xmlfile, path):  # Assuming xmlfile is in path, path without backslash
    import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(path+"\\"+xmlfile)
    except:
        print "XML file not found"
        exit()
        
    root = tree.getroot()
    uname = root[0].text
    pwd = root[1].text
    remotepath = root[2].text
    site = root[3].text
    return [uname, pwd, remotepath, site]


###### MAIN SECTION ########

path = os.getcwd()

# Get credentials
[uname, pwd, remote_path, site]  = getdata('credentials.xml', path)

# Delete Existing folder
del_existing_folder(uname, pwd, site, path, remote_path)

# Zip the folder
zipfolder('file_up',path)

# Upload Zip
uploadzip(uname, pwd, site, 'file_up.zip', path)

# Unzip file by invoking unzip.php
unzip_file(remote_path)  # Where unzip.php was uploaded
print "Your site is online at "+remote_path+'/upload/'