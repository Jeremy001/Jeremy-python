#!/usr/bin/env python
#coding=utf-8

import sys
import os 

filename=sys.argv[1]
sh=open(filename)
sql=sh.read()
str=sql.split(';')
sql_list=[]
for i in range(0,len(str)-1):
   sql_list.append(str[i])

from pyhive import hive  
from TCLIService.ttypes import TOperationState
conn = hive.Connection(
	host='cloudera-edge-01.cdh01.cn-hangzhou.dianjia.io',
	port=10000,
	username="admin",
	database="default")
print "connect hive database success"
cursor = conn.cursor()

for i in range(0,len(sql_list)):
    cursor.execute(sql_list[i])
print "execute hive sql success"

#断开连接
cursor.close()
conn.close() 
print "close hive connect success"

