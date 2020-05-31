import pysftp
import warnings
import os
from datetime import datetime
import ftplib
import stat
warnings.filterwarnings('ignore')

#cnopts = pysftp.CnOpts()
#cnopts.hostkeys = None

myHostname = "SFTP.asasa.df.au"
myUsername = "sdsdsd"
myPassword = "sdsds"


#---------File transfer (Pick Ticket,etc)from COG to RL Starts Here-------------------

ftp=ftplib.FTP('182.170.100.150')
ftp.login("asasa", '23232')
print("FTP Connected")
ftp.cwd('RLLive/Inbound/')

today = datetime.now()

localFilePath = 'C:/Python_File_Transfer/PickTicket/'
remoteFilePath = '/sharaf_user/Outbound/'

#directory_structure = sftp.listdir_attr()
if os.path.exists(localFilePath + today.strftime('%Y%m%d'))==False:
    os.mkdir(localFilePath + today.strftime('%Y%m%d'))

localFilePath = localFilePath + today.strftime('%Y%m%d')
#, cnopts=cnopts
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword ) as sftp:
    print( "SFTP Connected")
    sftp.cwd('/sharaf_user/Outbound')
    #i=0
    for filename  in sftp.listdir():
        if stat.S_ISREG(sftp.stat(os.path.join(remoteFilePath, filename)).st_mode):
            #i=i+1
            templocalFilePath=localFilePath + '/' + filename
            print("Downloading files " + filename +"from SFTP To Location "+templocalFilePath)
            sftp.get(filename, templocalFilePath)
            sftp.remove(filename)
            #if i==4:
                #break
            # Upload file from sftp to ftp
for root, dirs, files in os.walk(localFilePath, topdown=True):
    relative = root[len(localFilePath):].lstrip(os.sep)
    for f in files:
        filePath = os.path.join(localFilePath, relative, f)
        #ftp.cwd(relative)
        with open(filePath, 'rb') as fileObj:
            ftp.storbinary('STOR ' + f, fileObj)
            print("Uploaded to FTP")

ftp.quit()

#---------File transfer (Pick Ticket,etc)from COG to RL Ends Here-------------------



#---------Sales File transfer (HDR,CLCN,SKU)from COG to RL Starts Here-------------------



today = datetime.now()

localFilePath = 'C:/Python_File_Transfer/Sales/'
remoteFilePath = '/sharaf_user/Outbound/Sales'

#directory_structure = sftp.listdir_attr()
if os.path.exists(localFilePath + today.strftime('%Y%m%d'))==False:
    os.mkdir(localFilePath + today.strftime('%Y%m%d'))

localFilePath = localFilePath + today.strftime('%Y%m%d')
#, cnopts=cnopts
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print( "SFTP Connected")
    sftp.cwd('/sharaf_user/Outbound/Sales')
    #i=0
    for filename  in sftp.listdir():
        if stat.S_ISREG(sftp.stat(os.path.join(remoteFilePath, filename)).st_mode):
            #i=i+1
            templocalFilePath=localFilePath + '/' + filename
            print("Downloading files " + filename +"from SFTP To Location "+templocalFilePath)
            sftp.get(filename, templocalFilePath)
            sftp.remove(filename)
            #if i==4:
                #break
            # Upload file from sftp to ftp
print(localFilePath)
ftp1=ftplib.FTP('121.189.189.155')
ftp1.login("usssn", 'pwdd')
print("Sales FTP Connected")

ftp1.cwd('cottonon/Sales files/SalesFiles2020/')
for root, dirs, files in os.walk(localFilePath, topdown=True):
    relative = root[len(localFilePath):].lstrip(os.sep)
    print('entered')
    for f in files:
        filePath = os.path.join(localFilePath, relative, f)
        print(filePath)
        #ftp.cwd(relative)
        with open(filePath, 'rb') as fileObj:
            try:
                ftp1.storbinary('STOR ' + f, fileObj)
                print("Uploaded to Sales-FTP")
            except ftplib.all_errors as e:
                print('FTP error:', e)

ftp1.quit()


#---------Sales File transfer (HDR,CLCN,SKU)from COG to COTTONON-FTP ends Here-------------------






print("--------------------------")
print("downloaded all files from SFTP to Local and Uploaded to FTP")
