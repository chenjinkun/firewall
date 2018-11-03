#!/usr/bin/dev python3
# -*- coding: utf-8 -*-

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
	cursor.execute('create table user (username varchar(20) primary key, upload boolean, download boolean, delet boolean, mkdir boolean, file_size INTEGER)')
	cursor.execute('create table file_type (username varchar(20) primary key, jpg boolean not null, txt boolean not null, avi boolean not null)')
	cursor.execute('create table ip_check (id integer primary key autoincrement, sourceip blob, targetip blob)')
	cursor.close()
	conn.commit()
	conn.close()

if __name__=='__main__':
	init()
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute('insert into user (username, upload, download, delet, mkdir, file_size) values (\'user1\',\'1\',\'1\',\'0\',\'false\',200)')
	cursor.execute('select * from user where username=?',('user1',))
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into file_type (username, jpg, txt, avi) values (\'user1\',1,1,1)')
	cursor.execute('select * from user where username=?',('user1',))
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into ip_check (sourceip) values (\'192.168.0.0\')')
	cursor.execute('select * from ip_check where id=?','1')
	values = cursor.fetchall()
	print(values)
	cursor.execute('insert into ip_check (targetip) values (\'192.168.1.0\')')
	cursor.execute('select * from ip_check where id=?','2')
	values = cursor.fetchall()
	print(values)
	cursor.close()
	conn.close()
