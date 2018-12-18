# 透明代理防火墙项目firewall

### 版本号：v0.3.0    更新时间：2018.12.18

#### 更新记录
完成了gui的基本开发，以及完成控制模块的基本功能实现。
后续需要：用户界面完善，集成测试等工作

#### 开发环境

python 2.7

sqlite3


#### 开发注意事项

1. Develop分支为当前最新分支，master分支为当前可提交的最新分支。所有的开发均以Develop分支为起点新建分支进行，完成一定功能后，提交pull request到Develop分支，由 @chenjinkun 进行merge。每开发出一版可提交给老师的版本，由@chenjinkun 将Develop分支merge到master分支。**切记不要直接push到master或Develop分支。**
2. 版本号说明，整体项目有突破性进展，第一个版本号+1；有模块性的进展，第二个版本号+1；第三个版本号用于个人测试版本的标识或bug修复。
3. 所有的python代码均写为可调用的模块，即所有功能均以类或者函数的方式实现。模块内的测试以在python代码中添加` if __name__ == '__main__'`的部分进行测试。模块之间的集成测试将后期统一编写测试脚本进行。
4. 每次提交pull request，需要将自己写的代码名称、功能、以及和其他模块的交互接口情况添加的README.md中的代码结构部分。



#### 代码结构

##### proxy模块

主要实现ftp协议的代理功能（包括主动模式和被动模式）。模块中包含的代码及其功能分别为：

+ ftp_proxy.py包括ftp代理功能的初步实现，调用start_proxy(lsport)函数可启动代理功能，其中lsport是代理所监听的端口号。 checkclient、checkserver、checkuser、control等函数均为后面的防火墙功能所需要的接口，通过这些接口返回的结果以确定是否进行控制转发。

##### config模块

主要实现防火墙规则的配置，防火墙规则的数据库存储，以及用户界面设计。模块中包含的代码及其功能分别为：
数据库表创建模块
数据库表操作模块：
1.ip_pri表相关操作: 
	def add_ip_pri()  def update_ip_pri()  def delete_ip_pri()  
	def check_pri(ip, pri)  pri 可以是'upload' ,'download','delet','mkdir','file_size', 函数正常返回0或1.
2.file_type表相关操作： 
	def add_file_type(),def update_file_type(),def delete_file_type(),
	def check_type(file_type,pri) file_type 可以是 'jpg','txt','avi',pri可以是 upload,download. 函数正常返回0或1.
3.ip_check表相关操作： 
	def add_sourceip() def add_targetip() def delete_sourceip() def delete_targetip() 
	def check_sourceip(ip) def check_targetip(ip) 函数正常返回0或1.

+

##### control模块

主要实现对防火墙规则的解析以及对接收到的ftp协议数据的解析。模块中包含的代码及其功能分别为：

-
