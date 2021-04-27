from __future__ import absolute_import
import os
import sqlite3
from array import array
import base64
import six
from PIL import Image
from io import BytesIO
from io import open
from time import *
begin_time = time()
path = f'/home/user/MBTiles/L12'
if not os.path.exists(f'/home/user/Directory/12'):
    os.mkdir(f'/home/user/Directory/12')
for root,dirs,files in os.walk(path):
    for file in files:
        db = os.path.join(root,file)
        mydb = sqlite3.connect(db)
        cursor = mydb.cursor()
        sql = f'SELECT tile_column FROM map order by tile_column desc;'
        cursor.execute(sql)
        value = cursor.fetchone()
        if value:
            m = value[0]
            print(m)
            for j in range(m + 1):
                sql1 = f'SELECT * FROM map WHERE tile_column={j}'
                cursor0 = mydb.cursor()
                cursor0.execute(sql1)
                value0 = cursor0.fetchall()
                if value0:
                    if not os.path.exists(f'/home/user/Directory/12/{j}'):
                        os.mkdir(f'/home/user/Directory/12/{j}')
                    for i in value0:
                        if i:
                            temp = i[3]
                            sql2 = f'SELECT * FROM images WHERE tile_id=\'{temp}\''
                            cursor1 = mydb.cursor()
                            cursor1.execute(sql2)
                            value1 = cursor1.fetchone()
                            print(value1)
                            temp1 = i[2]
                            print(temp1)
                            flout = open(f'//home/user/Directory/12/{j}/{temp1}.jpg', u'wb')
                            flout.write(value1[1])
                            flout.close()
                            cursor1.close()
                cursor0.close()
            cursor0.close()
            mydb.close()
end_time = time()
run_time = end_time-begin_time
print(run_time)