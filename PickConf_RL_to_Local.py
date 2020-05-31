import pysftp
import warnings
import os
from datetime import datetime
import ftplib
warnings.filterwarnings('ignore')

#cnopts = pysftp.CnOpts()
#cnopts.hostkeys = None

myHostname = "SFTP.ssss.m.au"
myUsername = "sss"
myPassword = "pwdd"

ftp=ftplib.FTP('172.170.100.150')
ftp.login("sss", 'pwddd')
print("FTP Connected")
ftp.cwd('RLLive/Outbound/')

today = datetime.now()

localFilePath = 'C:/Python_File_Transfer/PickConfirm/'
remoteFilePath = '/sharaf_user/Inbound/'

#directory_structure = sftp.listdir_attr()
if os.path.exists(localFilePath + today.strftime('%Y%m%d'))==False:
    os.mkdir(localFilePath + today.strftime('%Y%m%d'))

localFilePath = localFilePath + today.strftime('%Y%m%d') + '/'

filenames = ftp.nlst() # get filenames within the directory
print (filenames)
for filename in filenames:
    local_filename = os.path.join(localFilePath, filename)
    file = open(local_filename, 'wb')
    ftp.retrbinary('RETR '+ filename, file.write)
    print("Downloaded to Local")
    file.close()
    #, cnopts=cnopts
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
        print("SFTP Connected")
        if filename.startswith("RL_Ack_COG"):
            sftp.cwd('/sharaf_user/Inbound/Acknowledgment/')
            remoteFilePath = '/sharaf_user/Inbound/Acknowledgment/'
        else:
            sftp.cwd('/sharaf_user/Inbound/')
            remoteFilePath = '/sharaf_user/Inbound/'
        sfilepath=localFilePath+filename
        sftp.put(sfilepath,remoteFilePath+filename)
        print("Uploaded to SFTP")
    ftp.delete(filename)

print("-------------------------")
print("downloaded all files from RL to Local and Uploaded to SFTP")

ftp.quit()
