#!/usr/bin/dev python3
# -*- coding: utf-8 -*-

'update database'

__author__='xushunye'

import os, sqlite3, db_init

#####################################  options on table user   ###############################################
userindex = {'username':0,'upload':1,'download':2,'delet':3,'mkdir':4,'file_size':5}

def add_user(name,pri_upload=0,pri_download=0,pri_delete=0,pri_mkdir=0,size=0):

	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 


	flag = (pri_upload !=0 and pri_upload !=1) or (pri_download !=0 and pri_download !=1) or (pri_delete !=0 and pri_delete !=1) or (pri_mkdir !=0 and pri_mkdir !=1) or (size<0)
	if flag:
		print('add user failed, you put invalid data')
		return
	else :
		conn = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute("insert into user values ('%s','%d','%d','%d','%d','%d');" % (name,pri_upload,pri_download,pri_delete, pri_mkdir,size))
		cursor.close()
		conn.commit()
		conn.close()

def update_user(name,upload,download,delet,mkdir,file_size):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	if upload !=0 and upload !=1:
		print('update failed,please set upload to 1 or 0')
		return 
	else :
		cursor.execute("update user set upload =?  where username=?",(upload,name))
	if download !=0 and download !=1:
		print('update failed,please set download to 1 or 0')
		return 
	else :
		cursor.execute("update user set download =?  where username=?",(download,name))
	if delet !=0 and delet !=1:
		print('update failed,please set delet to 1 or 0')
		return 
	else :
		cursor.execute("update user set delet =?  where username=?",(delet,name))
	if mkdir !=0 and mkdir !=1:
		print('update failed,please set mkdir to 1 or 0')
		return 
	else :
		cursor.execute("update user set mkdir =?  where username=?",(mkdir,name))
	if file_size<0 :
		print('update failed, file_size should greater than 0')
	else :
		cursor.execute("update user set file_size =? where username=?",(file_size,name))
	cursor.close()
	conn.commit()
	conn.close()

def delete_user(name):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from user where username=?",(name,))
	cursor.close()
	conn.commit()
	conn.close()

def check_pri(name,pri):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select * from user where username=?",(name,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return
	else :
		return values[0][userindex[pri]]
###########################   options on table user      #####################################


############################ options on table file_type   ##################################
file_typeindex={'username':0,'jpg':1,'txt':2,'avi':3}

def add_file_type(name,jpg=0,txt=0,avi=0):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	flag = (jpg !=0 and jpg !=1) or (txt !=0 and txt !=1) or (avi !=0 and avi !=1)
	if flag:
		print('add file_type failed, you put invalid data')
		return
	else :
		conn = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute("insert into file_type values ('%s','%d','%d','%d');" % (name,jpg,txt,avi))
		cursor.close()
		conn.commit()
		conn.close()

def update_file_type(name,jpg,txt,avi):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	if jpg !=0 and jpg !=1:
		print('dateup failed,please set jpg to 1 or 0')
		return 
	else :
		cursor.execute("update file_type set jpg =?  where username=?",(jpg,name))
	if txt !=0 and txt !=1:
		print('update failed,please set txt to 1 or 0')
		return 
	else :
		cursor.execute("update file_type set txt =?  where username=?",(txt,name))
	if avi !=0 and avi !=1:
		print('update failed,please set avi to 1 or 0')
		return 
	else :
		cursor.execute("update file_type set avi =?  where username=?",(avi,name))
	cursor.close()
	conn.commit()
	conn.close()


def delete_file_type(name):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from file_type where username=?",(name,))
	cursor.close()
	conn.commit()
	conn.close()

def check_type(name,file_type):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select * from file_type where username=?",(name,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return
	else :
		return values[0][file_typeindex[file_type]]
############################  optinons on table file_type    ###############################



###########################  options on table ip_check    #####################################
def add_sourceip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("insert into ip_check (sourceip) values ('%s');" % ip)
	cursor.close()
	conn.commit()
	conn.close()

def add_targetip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("insert into ip_check (targetip) values ('%s');" % ip)
	cursor.close()
	conn.commit()
	conn.close()

def delete_sourceip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from ip_check where sourceip=?",(ip,))
	cursor.close()
	conn.commit()
	conn.close()

def delete_targetip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from ip_check where targetip=?",(ip,) )
	cursor.close()
	conn.commit()
	conn.close()

def check_sourceip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select id from ip_check where sourceip=?",(ip,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return 0
	else :
		return 1

def check_targetip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return 
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select id from ip_check where targetip=?",(ip,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return 0
	else :
		return 1
############################ options on table ip_check    #################################

def show_table(table_name):
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute("select * from '%s' " %table_name)
	values = cursor.fetchall()
	print(values)

if __name__=='__main__':
	#init()
	#conn = sqlite3.connect('test.db')
	#cursor = conn.cursor()
	#cursor.execute('insert into user (username, upload, download, del, mkdir, file_size) values (\'user1\',\'1\',\'1\',\'0\',\'false\',200)')
	#cursor.execute('select * from user where username=?',('user1',))
	#values = cursor.fetchall()
	#print(values)
	#cursor.execute('insert into file_type (username, jpg, txt, avi) values (\'user1\',1,1,1)')
	#cursor.execute('select * from user where username=?',('user1',))
	#values = cursor.fetchall()
	#print(values)
	#cursor.execute('insert into ip_check (sourceip) values (\'192.168.0.0\')')
	#cursor.execute('select * from ip_check where id=?','1')
	#values = cursor.fetchall()
	#print(values)
	#cursor.execute('insert into ip_check (destinateip) values (\'192.168.1.0\')')
	#cursor.execute('select * from ip_check where id=?','2')
	#values = cursor.fetchall()
	#print(values)
	#cursor.close()
	#conn.close()


####test on table user########
	db_init.init()
	add_user('user1',1,1,1,1,200)
	add_user('user2',0,0,1,1,-100)
	add_user('user3',-1,0,1,1,200)
	add_user('user4',0,0,1,2,200)
	show_table('user')
	update_user('user1',0,1,1,1,200)
	update_user('user5',1,1,1,1,200)
	update_user('user2',0,0,1,1,200)
	show_table('user')
	print(check_pri('user1','download'))
	print(check_pri('user2','file_size'))
	print(check_pri('user6','upload'))
	delete_user('user6')
	delete_user('user1')
	show_table('user')

##### test on table file_type#############
	add_file_type('user1',1,1,1)
	add_file_type('user2',1,0,1)
	add_file_type('user3',1,2,-1)
	show_table('file_type')
	update_file_type('user1',0,1,1)
	update_file_type('user4',1,1,1)
	show_table('file_type')
	print(check_type('user1','txt'))
	print(check_type('user5','txt'))
	delete_file_type('user1')
	show_table('file_type')

########test on table check_ip ##############

	add_sourceip('192.168.0.1')
	add_targetip('192.168.0.2')
	add_sourceip('192.168.0.3')
	add_targetip('192.168.0.4')
	show_table('ip_check')
	delete_sourceip('192.168.0.1')
	delete_sourceip('192.168.0.2')
	delete_targetip('192.168.0.4')
	show_table('ip_check')
	add_sourceip('192.168.0.5')
	add_targetip('192.168.0.6')
	print(check_targetip('192.168.0.6'))
	print(check_targetip('192.168.0.5'))
	print(check_sourceip('192.168.0.5'))
	print(check_sourceip('192.168.0.1'))
	show_table('ip_check')
































