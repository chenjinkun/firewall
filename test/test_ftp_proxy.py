import test_config
from ftp_proxy import start_proxy
from db_init import init
from db_policy import add_sourceip, add_targetip

init()
add_sourceip('192.168.0.107')
add_targetip('202.120.2.2')
add_targetip('public.sjtu.edu.cn')
start_proxy(8888)
