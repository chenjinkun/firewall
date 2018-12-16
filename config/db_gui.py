#!/usr/bin/python3
from db_policy import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import os,sqlite3

class MyApplication(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Rules Configuration")
		self.geometry("1200x800")
		self.resizable(width=True, height=True)

		menuframe = Frame(self)
		menuframe.pack(side=TOP)

		add_table_button = ttk.Button(menuframe,text="Add Table",command=self.addtable)
		add_table_button.pack(side=LEFT)
		import_databases_button = ttk.Button(menuframe,text="Import databases",command=self.importdb)
		import_databases_button.pack(side=LEFT)

		self.dbframe = Frame(self)
		self.dbframe.pack(side=BOTTOM)
	
		tables = self.lstables()
		self.tree1 = ttk.Treeview(self.dbframe)	
		dbname = self.tree1.insert('',0,'root',text='test',values=('0'))
		index=0
		for table in tables:
			if table!=('sqlite_sequence',):
				self.tree1.insert(dbname,index,text=table,tags='showtable',values=('0'))
				index = index+1
		self.tree1.tag_bind('showtable','<<TreeviewSelect>>',self.__showtable)
		self.tree1.pack(side=LEFT)
		self.dataframe = Frame(self.dbframe)
		self.tree2= ttk.Treeview(self.dataframe,show='headings')
		self.tree2.bind('<Double-1>',self.set_value)
		self.tree2.pack()
		self.adddata_button = ttk.Button(self.dataframe,text='add data',command=self.adddata)
		self.dataframe.pack(side=RIGHT)
		

	
	def __showtable(self,event):
		x=self.tree2.get_children()
		for item in x:
			self.tree2.delete(item)

		for item in self.tree1.selection():
			tablename = self.tree1.item(item,'text')
			db_file = os.path.join(os.path.dirname(__file__),'test.db')
			if os.path.isfile(db_file)==False:
				print('There is no databases')
				return -1
			
			conn = sqlite3.connect(db_file)
			cursor = conn.cursor()
			cursor.execute("select * from '%s'" %tablename)
			values = cursor.fetchall()
			self.col_name_list = [tuple[0] for tuple in cursor.description]
			cursor.close()
			conn.commit()
			conn.close()
			
			self.tree2["columns"] = self.col_name_list
			for col in self.col_name_list:
				self.tree2.column(col,width=100,anchor='center')
				self.tree2.heading(col,text=col)
			for data in values:
				self.tree2.insert('','end',values=data)
			self.adddata_button.pack(side=BOTTOM)
			self.tree2.pack()

	def set_value(self,event):
		print("set value success")
		for item2 in self.tree2.selection():
			item_text = self.tree2.item(item2, "values")
		column = self.tree2.identify_column(event.x)
		row = self.tree2.identify_row(event.y)
		cn = int(str(column).replace('#',''))
		print(cn)
		rn = int(str(row).replace('I',''))
		print(rn)
		entryedit = Entry(self.dataframe)
		entryedit.place(x=(cn-1)*200,y=rn*20)
		def saveedit():
			self.tree2.set(item2,column=column,value=entryedit.get())
			values=list(tuple(item_text))
			values[cn-1]=entryedit.get()
			entryedit.destroy()
			okb.destroy()
			print(values)
			for item1 in self.tree1.selection():
				tablename = self.tree1.item(item1,'text')
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





		okb = ttk.Button(self.dataframe,text='set',command=saveedit)
		okb.place(x=120+(cn-1)*200,y=rn*20)

	def adddata(self):
		for item in self.tree1.selection():
			tablename = self.tree1.item(item,'text')
		if tablename=='ip_pri':
			self.tree2.insert('','end',values=['0.0.0.0',0,0,0,0,0])
			add_ip_pri('0.0.0.0',0,0,0,0,0)
		if tablename=='file_type':
			self.tree2.insert('','end',values=['zero',0,0])
			add_file_type('zero',0,0)
		if tablename=='ip_check':
			self.tree2.insert('','end',values=['-1','0','0'])
			add_SOURCEIP('none')

		self.tree2.update()

	def lstables(self):
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

	def addtable(self):
		messagebox.showinfo('Information','call add table success')

	def importdb(self):
		messagebox.showinfo('Information','call import databases success')

def main():
	app = MyApplication()
	app.mainloop()

if __name__ == '__main__':
	main()
	
