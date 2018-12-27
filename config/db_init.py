'initiate database'

__author__='xushunye'

import os, sqlite3

def init():

	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file):
		print('db exists')
		return

	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()

	cursor.execute('create table file_type (FILE_TYPE varchar(20) primary key, UPLOAD boolean not null, DOWNLOAD boolean not null)')
	cursor.execute('create table ip_pri (IP varchar(15) primary key, UPLOAD boolean, DOWNLOAD boolean, DELET boolean, MKDIR boolean, FILE_SIZE INTEGER)')
	#cursor.execute('create table ip_check (ID integer primary key autoincrement, SOURCEIP blob, TARGETIP blob)')
	cursor.execute('create table check_sourceip (ID integer primary key autoincrement, SOURCEIP blob)')
	cursor.execute('create table check_targetip (ID integer primary key autoincrement, TARGETIP blob)')
	cursor.close()
	conn.commit()
	conn.close()

if __name__=='__main__':
	init()
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute('insert into ip_pri (IP, UPLOAD, DOWNLOAD, DELET, MKDIR, FILE_SIZE) values (\'192.168.1.1\',\'1\',\'1\',\'0\',\'false\',200)')
	cursor.execute('select * from ip_pri where IP=?',('192.168.1.1',))
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into file_type (FILE_TYPE, UPLOAD, DOWNLOAD) values (\'txt\',1,1)')
	cursor.execute('select * from file_type where FILE_TYPE=?',('txt',))
	values = cursor.fetchall()
	print(values)
	#cursor.execute('insert into ip_check (SOURCEIP) values (\'192.168.0.0\')')
	#cursor.execute('select * from ip_check where ID=?','1')
	#values = cursor.fetchall()
	#print(values)
	#cursor.execute('insert into ip_check (TARGETIP) values (\'192.168.1.0\')')
	#cursor.execute('select * from ip_check where ID=?','2')
	#values = cursor.fetchall()
	#print(values)
	cursor.execute('insert into check_sourceip (SOURCEIP) values (\'192.168.0.1\')')
	cursor.execute('select * from check_sourceip where ID=?',('1',))
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into check_sourceip (SOURCEIP) values (\'192.168.0.2\')')
	cursor.execute('select * from check_sourceip where ID=?',('2',))
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into check_targetip (TARGETIP) values (\'192.168.1.1\')')
	cursor.execute('select * from check_targetip where ID=?',('1',))
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into check_targetip (TARGETIP) values (\'192.168.1.2\')')
	cursor.execute('select * from check_targetip where ID=?',('2',))
	values = cursor.fetchall()
	print(values)
	cursor.close()
	conn.close()
