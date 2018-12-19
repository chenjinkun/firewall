#!/usr/bin/python
import __init__

from db_policy import *
import Tkinter as tk
import ttk
import tkMessageBox
from Tkinter import *
import os,sqlite3,time
import threading

from ftp_proxy import ftp_proxy

def firewall_gui():
	def __showtable(event):
		x=tree2.get_children()
		for item in x:
			tree2.delete(item)

		for item in tree1.selection():
			tablename = tree1.item(item,'text')
			db_file = os.path.join(os.path.dirname(__file__),'test.db')
			if os.path.isfile(db_file)==False:
				print('There is no databases')
				return -1

			conn = sqlite3.connect(db_file)
			cursor = conn.cursor()
			cursor.execute("select * from '%s'" %tablename)
			values = cursor.fetchall()
			col_name_list = [tuple[0] for tuple in cursor.description]
			cursor.close()
			conn.commit()
			conn.close()

			tree2["columns"] = col_name_list
			for col in col_name_list:
				tree2.column(col,width=100,anchor='center')
				tree2.heading(col,text=col)
			for data in values:
				tree2.insert('','end',text='-',values=data)
			adddata_button.pack(side=BOTTOM)
			tree2.pack()

	def set_value(event):
		print("set value success")
		for item2 in tree2.selection():
			item_text = tree2.item(item2, "values")
			print(item_text)
		column = tree2.identify_column(event.x)
		row = tree2.identify_row(event.y)
		cn = int(str(column).replace('#',''))
		if cn==0:
			return
		print(cn)
		rn = int(str(row).replace('I',''))
		print(rn)
		entryedit = Entry(dataframe)
		entryedit.place(x=(cn-1)*200,y=rn*20)
		def saveedit():
			tree2.set(item2,column=column,value=entryedit.get())
			values=list(tuple(item_text))
			values[cn-1]=entryedit.get()
			entryedit.destroy()
			okb.destroy()
			print(values)
			for item1 in tree1.selection():
				tablename = tree1.item(item1,'text')
			if tablename=='ip_pri':
				update_ip_pri(values[0],values[1],values[2],values[3],values[4],values[5])
			if tablename=='file_type':
				update_file_type(values[0],int(values[1]),int(values[2]))
			if tablename=='ip_check':
				print('a')
				print(cn)
				if cn==2:
					update_SOURCEIP(int(values[0]),values[1])
				if cn==3:
					update_TARGETIP(int(values[0]),values[2])

		okb = ttk.Button(dataframe,text='set',command=saveedit)
		okb.place(x=120+(cn-1)*200,y=rn*20)

	def delvalue(event):
		time.sleep(1)
		for item2 in tree2.selection():
			print('000')
			item_text=tree2.item(item2,"values")
			print(item_text)
		for item1 in tree1.selection():
			tablename = tree1.item(item1,'text')
		values=list(tuple(item_text))
		if tablename=='ip_pri':
			delete_ip_pri(values[1])
		if tablename=='file_type':
			delete_fyle_type(values[1])
		if tablename=='ip_check':
			delete_ip_check(values[1])

	def adddata():
		for item in tree1.selection():
			tablename = tree1.item(item,'text')
		if tablename=='ip_pri':
			tree2.insert('','end',values=['0.0.0.0',0,0,0,0,0])
			add_ip_pri('0.0.0.0',0,0,0,0,0)
		if tablename=='file_type':
			tree2.insert('','end',values=['zero',0,0])
			add_file_type('zero',0,0)
		if tablename=='ip_check':
			tree2.insert('','end',values=['-1','0','0'])
			add_SOURCEIP('none')

		tree2.update()

	def lstables():
		db_file = os.path.join(os.path.dirname(__file__),'test.db')
		if os.path.isfile(db_file)==False:
			print('There is no databases')
			return -1

		conn = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute("select name from sqlite_master where type='table'")
		values = cursor.fetchall()
		cursor.close()
		conn.commit()
		conn.close()
		if values==[]:
			return -1
		else :
			return values

	def importdb():
		tkMessageBox.showinfo('Information','call import databases success')
	def addtable():
		tkMessageBox.showinfo('Information','call add table success')

	firewall = ftp_proxy(8888)

	def start():
		firewall.run()
		firewall.t.start()

	def pause():
		firewall.stop()
		firewall.t.join()

	top=tk.Tk()
	top.title('Rules Configuration')
	top.geometry("1200x800")
	top.resizable(width=True, height=True)

	menuframe = Frame(top)
	menuframe.pack(side=TOP)

	add_table_button = ttk.Button(menuframe,text="Add Table",command=addtable)
	add_table_button.pack(side=LEFT)
	import_databases_button = ttk.Button(menuframe,text="Import databases",command=importdb)
	import_databases_button.pack(side=LEFT)

	start_button = ttk.Button(menuframe,text="Start Proxy",command=start)
	start_button.pack(side=LEFT)
	end_button = ttk.Button(menuframe, text="Pause Proxy",command=pause)
	end_button.pack(side=LEFT)

	dbframe = Frame(top)
	dbframe.pack(side=BOTTOM)

	tables = lstables()
	tree1 = ttk.Treeview(dbframe)
	dbname = tree1.insert('',0,'root',text='test',values=('0'))
	index=0
	for table in tables:
		if table!=('sqlite_sequence',):
			tree1.insert(dbname,index,text=table,tags='showtable',values=('0'))
			index = index+1
	tree1.tag_bind('showtable','<<TreeviewSelect>>',__showtable)
	tree1.pack(side=LEFT)
	dataframe = Frame(dbframe)
	tree2= ttk.Treeview(dataframe,show='headings')
	tree2.bind('<Double-1>',set_value)
	tree2.pack()
	adddata_button = ttk.Button(dataframe,text='add data',command=adddata)
	dataframe.pack(side=RIGHT)





	top.mainloop()

if __name__ == '__main__':
	firewall_gui()
