import ftplib
import os
import shutil
import sys
import pymysql

# ftp ?| ~U보
host = 'rovitek.inosf.net'
user = 'givet'
passwd = 'Givet23'

# host = 'localhost'
# user = 'test'
# passwd = 'test108'

folder_tree = 0

try:
    conn = pymysql.connect(host='rovitek.inosf.net', user='givet', password='Givet2023', db='fourInch', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT location FROM locations WHERE id = %s"
    vals = sys.argv[1]
    cur.execute(sql, vals)
    row = cur.fetchone()
    print(row)
    conn.commit()
    conn.close()

except Exception as e:
    print(e)

try:
    # ftp ?~W?결
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

        get_folder_name = row[0]
        print(get_folder_name)

        if not os.path.exists("get_imgs"):
            os.makedirs("get_imgs")

        ftp.cwd(get_folder_name)
        ftp.dir()

        file_list = ftp.nlst()
        for folder_tree_file in file_list:
            fd = open(folder_tree_file, 'wb')
            ftp.retrbinary("RETR " + folder_tree_file, fd.write)


except Exception as e:
    print(e)



try:
    get_files = os.listdir(os.getcwd())
    for get_file in get_files:
        if '.png' in get_file or '.jpg' in get_file:
            #print(get_file)
            if os.path.exists("get_imgs/" + get_file):
                print(get_file + " exists")
                os.remove(get_file)
            else:
                shutil.move(get_file, "get_imgs/" + get_file)



except Exception as e:
    print(e)
            
