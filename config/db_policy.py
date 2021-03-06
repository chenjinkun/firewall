'update database'

__author__='xushunye'

import os, sqlite3, db_init

#####################################  operations  on table ip_pri  ###############################################
#userindex = {'username':0,'upload':1,'download':2,'delet':3,'mkdir':4,'file_size':5}
ip_pri_index = {'ip':0,'upload':1,'download':2,'delet':3,'mkdir':4,'file_size':5}

def add_ip_pri(ip,upload=0,download=0,delet=0,mkdir=0,file_size=0):

	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return


	flag = (upload !=0 and upload !=1) or (download !=0 and download !=1) or (delet !=0 and delet !=1) or (mkdir !=0 and mkdir !=1) or (file_size<0)
	if flag:
		print('add user failed, you put invalid data')
		return
	else :
		conn = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute("insert into ip_pri values ('%s','%d','%d','%d','%d','%d');" % (ip,upload,download,delet, mkdir,file_size))
		cursor.close()
		conn.commit()
		conn.close()

def update_ip_pri(ip,upload,download,delet,mkdir,file_size):
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
		cursor.execute("update ip_pri set UPLOAD =?  where IP=?",(upload,ip))
	if download !=0 and download !=1:
		print('update failed,please set download to 1 or 0')
		return
	else :
		cursor.execute("update ip_pri set DOWNLOAD =?  where IP=?",(download,ip))
	if delet !=0 and delet !=1:
		print('update failed,please set delet to 1 or 0')
		return
	else :
		cursor.execute("update ip_pri set DELET =?  where IP=?",(delet,ip))
	if mkdir !=0 and mkdir !=1:
		print('update failed,please set mkdir to 1 or 0')
		return
	else :
		cursor.execute("update ip_pri set MKDIR =?  where IP=?",(mkdir,ip))
	if file_size<0 :
		print('update failed, file_size should greater than 0')
	else :
		cursor.execute("update ip_pri set FILE_SIZE =? where IP=?",(file_size,ip))
	cursor.close()
	conn.commit()
	conn.close()

def update_ip_pri_id(ID,ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("update ip_pri set IP =?  where IP=?",(ip,ID))
	cursor.close()
	conn.commit()
	conn.close()


def delete_ip_pri(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from ip_pri where IP=?",(ip,))
	cursor.close()
	conn.commit()
	conn.close()

def check_pri(ip,pri):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select * from ip_pri where IP=?",(ip,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return -1
	else :
		return values[0][ip_pri_index[pri]]

def exists_ip(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select * from ip_pri where IP=?",(ip,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return 0
	else :
		return 1
###########################   operations  on table ip_pri      #####################################


############################ operations  on table file_type   ##################################
#file_typeindex={'username':0,'jpg':1,'txt':2,'avi':3}

file_pri_index = {'file_type':0,'upload':1,'download':2}
def add_file_type(file_type,upload=0,download=0):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return
	flag = (upload !=0 and upload !=1) or (download !=0 and download !=1)
	if flag:
		print('add file_type failed, you put invalid data')
		return
	else :
		conn = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute("insert into file_type values ('%s','%d','%d');" % (file_type,upload, download))
		cursor.close()
		conn.commit()
		conn.close()

def update_file_type_id(file_type,new_file_type):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()

	cursor.execute("update file_type set FILE_TYPE =?  where FILE_TYPE=?",(new_file_type,file_type))

	cursor.close()
	conn.commit()
	conn.close()



def update_file_type(file_type,upload,download):
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
		cursor.execute("update file_type set UPLOAD =?  where FILE_TYPE=?",(upload,file_type))
	if download !=0 and download !=1:
		print('update failed,please set download to 1 or 0')
		return
	else :
		cursor.execute("update file_type set DOWNLOAD =?  where FILE_TYPE=?",(download,file_type))

	cursor.close()
	conn.commit()
	conn.close()


def delete_file_type(file_type):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from file_type where FILE_TYPE=?",(file_type,))
	cursor.close()
	conn.commit()
	conn.close()

def check_type(file_type, pri):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return -1
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select * from file_type where FILE_TYPE=?",(file_type,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return -1
	else :
		return values[0][file_pri_index[pri]]

def filetype_blacklist(pri=None):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return -1
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	if pri == 'download':
		cursor.execute("select FILE_TYPE from file_type where DOWNLOAD='0'")
	elif pri == 'upload':
		cursor.execute("select FILE_TYPE from file_type where UPLOAD='0'")
	else:
		return ()

	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	return values

############################  optinons on table file_type    ################################


###########################  operations  on table check_sourceip    ####################################
def add_SOURCEIP(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("insert into check_sourceip (SOURCEIP) values ('%s');" % ip)
	cursor.close()
	conn.commit()
	conn.close()

def delete_SOURCEIP(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from check_sourceip where SOURCEIP=?",(ip,) )
	cursor.close()
	conn.commit()
	conn.close()


def update_SOURCEIP(ID,ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()

	if ID==-1:
		cursor.execute("select max(ID) from check_sourceip")
		values = cursor.fetchall()
		ID=values[0]
		ID=ID[0]
		cursor.execute("update check_sourceip set SOURCEIP =?  where ID=?",(ip,ID))
	else:
		cursor.execute("update check_sourceip set SOURCEIP =?  where ID=?",(ip,ID))

	cursor.close()
	conn.commit()
	conn.close()

def check_SOURCEIP(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return False

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select ID from check_sourceip where SOURCEIP=?",(ip,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return 0
	else :
		return 1
############################  operations  on table check_sourceip    ###################################


###########################  operations  on table check_targetip    ####################################
def add_TARGETIP(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("insert into check_targetip (TARGETIP) values ('%s');" % ip)
	cursor.close()
	conn.commit()
	conn.close()

def delete_TARGETIP(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("delete from check_targetip where TARGETIP=?",(ip,) )
	cursor.close()
	conn.commit()
	conn.close()

def update_TARGETIP(ID,ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	if ID==-1:
		cursor.execute("select max(ID) from check_targetip")
		values = cursor.fetchall()
		ID=values[0]
		ID=ID[0]
		cursor.execute("update check_targetip set TARGETIP =?  where ID=?",(ip,ID))
	else:
		cursor.execute("update check_targetip set TARGETIP =?  where ID=?",(ip,ID))
	cursor.close()
	conn.commit()
	conn.close()

def check_TARGETIP(ip):
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file)==False:
		print('db does not exists')
		return False

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute("select ID from check_targetip where TARGETIP=?",(ip,))
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	if values==[]:
		return 0
	else :
		return 1
############################  operations  on table check_targetip    ###################################



############################ operations  on table ip_check    #################################

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
	#cursor.execute('insert into ip_check (SOURCEIP) values (\'192.168.0.0\')')
	#cursor.execute('select * from ip_check where id=?','1')
	#values = cursor.fetchall()
	#print(values)
	#cursor.execute('insert into ip_check (destinateip) values (\'192.168.1.0\')')
	#cursor.execute('select * from ip_check where id=?','2')
	#values = cursor.fetchall()
	#print(values)
	#cursor.close()
	#conn.close()


####test on table ip_pri########
	db_init.init()
	add_ip_pri('192.168.1.1',1,1,1,1,200)
	show_table('ip_pri')
