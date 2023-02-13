import ftplib
import os
import shutil
import datetime

# ftp 정보
host = 'rovitek.inosf.net'
user = 'givet'
passwd = 'Givet23'

# host = 'localhost'
# user = 'test'
# passwd = 'test108'

folder_tree = 0



try:
    # ftp 연결
    with ftplib.FTP() as ftp:
        ftp.connect(host=host,port=21)
        ftp.encoding = 'utf-8'
        #ftp.set_pasv(False)
        ftp.set_pasv(True)
        s = ftp.login(user=user,passwd=passwd)
        print("Connect success!")

        ftp.cwd("/home/rovitek/4inch/public/data")
        
        # List up files
        list = ftp.nlst()
        ftp.dir()
        #print(list)
 
        list = os.listdir('post_imgs')
        print(list)


        now = datetime.datetime.now()
        print(now.strftime("%Y%m%d%I"))

        #ftp.mkd(now.strftime("%Y%m%d%I%m%S"))

        # with open(file="get_img.py", mode='rb') as wf:
        #     ftp.storbinary('STOR get_img.py', wf)
        
        ftp.close()
        
                
except Exception as e:
    print(e)

