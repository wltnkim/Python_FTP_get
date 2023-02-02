import ftplib
import os

# ftp 정보
#host = 'rovitek.inosf.net'
#user = 'givet'
#passwd = 'Givet23'

host = 'localhost'
user = 'test'
passwd = 'test108'

folder_tree = 0

# ###############
# # 다건 파일 다운로드
# ###############
try:
    # ftp 연결
    with ftplib.FTP() as ftp:
        ftp.connect(host=host,port=21)
        ftp.encoding = 'utf-8'
        s = ftp.login(user=user,passwd=passwd)
        print("Connect success!")

        #ftp.cwd('D:git/')  # 현재 폴더 이동
        #print(ftp.pwd())

        #filename = "main_.py"
        #ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)

        # List up files
        list = ftp.nlst()
        print(list)

        # 파일다운로드
        
        for file in list :
            filename = file.split(sep='.')
            if not len(filename) >= 2:
                print("Directory : " + file)

                while (folder_tree > 0):
                    folder_tree = folder_tree - 1
                    ftp.cwd('..')

                ftp.cwd(file)
                folder_tree = folder_tree + 1

                file_list = ftp.nlst()
                for folder_tree_file in file_list:
                    print("File : " + file + "/" + folder_tree_file)
                    fd = open(folder_tree_file, 'wb')
                    ftp.retrbinary("RETR " + folder_tree_file, fd.write)

            else:
                while (folder_tree > 0):
                    folder_tree = folder_tree - 1
                    ftp.cwd('..')

                print("File : " + file)
                fd = open(file, 'wb')
                ftp.retrbinary("RETR " + file, fd.write)


except Exception as e:
    print(e)
