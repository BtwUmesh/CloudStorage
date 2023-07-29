import pysftp
import os
import subprocess
import paramiko
import time
from scp import SCPClient

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
sftpHost = '192.168.1.71'
sftpPort = 22
uname = 'Server'
pwd = '123'

def menu():
    print()
    print()
    print()
    print("#############################################")
    print("####        Choose 1 for Upload          ####")
    print("####        Choose 2 for Download        ####")
    print("####        Choose 3 for Exit            ####")
    print("#############################################")

menu()
choice=int(input("Enter your choice: "))

while choice != 3:
    if choice==1:
        subprocess.call([r'C:\Users\Umesh Kumar\Desktop\Project\Files\Copy.bat'])
        dir=os.chdir(r'C:\Users\Umesh Kumar\Documents\Python\Temp')

    
        with pysftp.Connection(sftpHost, port=sftpPort, username=uname, password=pwd, cnopts=cnopts) as sftp:
          print("connected to sftp server!")
          print("Uploading File...")
          sftp.put('a.E01', preserve_mtime=True)
          sftp.put('Name.txt',preserve_mtime=True)
          print("File Uploaded!!")


        con = paramiko.SSHClient()
        con.load_system_host_keys()
        con.connect(sftpHost, username=uname, password=pwd)

        stdin, stdout, stderr = con.exec_command('C:\\Users\\Server\\Desktop\\Server\\Files\\Split.bat')

        if stderr.read() == b'':
            print('Processing...Please wait...')
            # time.sleep(1)
            print('Done!!!')
        else:
            print('An error occurred')
        # subprocess.call([r'C:\Users\Umesh Kumar\Desktop\Project\Files\Cleanup.bat'])
        # stdin, stdout, stderr = con.exec_command('C:\\Users\\Server\\Desktop\\Server\\Files\\Cleanup.bat')

    elif choice==2:
        dir = os.chdir(r'C:\Users\Umesh Kumar\Documents\Python\Downloads')

        print('\n#####################################################################')
        print('#################### Choose The File to Download ####################')
        print('#####################################################################\n')


        stdin, stdout, stderr = con.exec_command('C:\\Users\\Server\\Desktop\\Server\\Files\\Dir.bat')

        with pysftp.Connection(sftpHost, port=sftpPort, username=uname, password=pwd, cnopts=cnopts) as sftp:
            sftp.get("Data.txt", preserve_mtime=True)

        with open("Data.txt") as file:
            name = file.read()
            print(name)

        subprocess.call([r'C:\Users\Umesh Kumar\Desktop\Project\Files\DFile.bat'])

        with pysftp.Connection(sftpHost, port=sftpPort, username=uname, password=pwd, cnopts=cnopts) as sftp:
            sftp.put("DName.txt", preserve_mtime=True)

        stdin, stdout, stderr = con.exec_command('C:\\Users\\Server\\Desktop\\Server\\Files\\Join.bat')

        print("File Compiled Downloading...")

        time.sleep(5)

        with pysftp.Connection(sftpHost, port=sftpPort, username=uname, password=pwd, cnopts=cnopts) as sftp:
            sftp.get("a.E01", preserve_mtime=True)
        subprocess.call([r'C:\Users\Umesh Kumar\Desktop\Project\Files\Rename.bat'])
        print("File Downloaded Successfully !!")
        subprocess.call([r'C:\Users\Umesh Kumar\Desktop\Project\Files\Cleanup.bat'])
        stdin, stdout, stderr = con.exec_command('C:\\Users\\Server\\Desktop\\Server\\Files\\Cleanup.bat')

    else:
        print("Invalid Chioice")
    
    print()
    menu()
    choice=int(input("Enter your choice: "))

exit()




