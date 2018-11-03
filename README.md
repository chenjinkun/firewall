# 透明代理防火墙项目firewall

### 版本号：v0.0.0    更新时间：2018.10.26

#### 开发环境

python 3.6

sqlite3



#### 开发注意事项

1. Develop分支为当前最新分支，master分支为当前可提交的最新分支。所有的开发均以Develop分支为起点新建分支进行，完成一定功能后，提交pull request到Develop分支，由 @chenjinkun 进行merge。每开发出一版可提交给老师的版本，由@chenjinkun 将Develop分支merge到master分支。**切记不要直接push到master或Develop分支。**
2. 版本号说明，整体项目有突破性进展，第一个版本号+1；有模块性的进展，第二个版本号+1；第三个版本号用于个人测试版本的标识或bug修复。
3. 所有的python代码均写为可调用的模块，即所有功能均以类或者函数的方式实现。模块内的测试以在python代码中添加` if __name__ == '__main__'`的部分进行测试。模块之间的集成测试将后期统一编写测试脚本进行。
4. 每次提交pull request，需要将自己写的代码名称、功能、以及和其他模块的交互接口情况添加的README.md中的代码结构部分。



#### 代码结构

##### proxy模块

主要实现ftp协议的代理功能（包括主动模式和被动模式）。模块中包含的代码及其功能分别为：

+ 

##### config模块

主要实现防火墙规则的配置，防火墙规则的数据库存储，以及用户界面设计。模块中包含的代码及其功能分别为：
数据库表创建模块
数据库表操作模块：
1.user表相关操作: 
	def add_user()  def update_user()  def delete_user()  
	def check_pri(username, pri)  pri 可以是'upload' ,'download','delet','mkdir','file_size', 函数正常返回0或1.
2.file_type表相关操作： 
	def add_file_type(),def update_file_type(),def delete_file_type(),
	def check_type(username,file_type) file_type 可以是 'jpg','txt','avi'。函数正常返回0或1.
3.ip_check表相关操作： 
	def add_sourceip() def add_targetip() def delete_sourceip() def delete_targetip() 
	def check_sourceip(ip) def check_targetip(ip) 函数正常返回0或1.

+ 

##### control模块

主要实现对防火墙规则的解析以及对接收到的ftp协议数据的解析。模块中包含的代码及其功能分别为：

- 

