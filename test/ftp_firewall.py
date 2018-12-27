import test_config
from db_init import init
from db_policy import add_SOURCEIP, add_TARGETIP, add_file_type, add_ip_pri
from db_gui import firewall_gui

test_client_ip = '192.168.31.223'

init()
add_SOURCEIP(test_client_ip)
add_TARGETIP('188.131.204.91')
add_file_type('.ppt', download = 0, upload = 1)
add_ip_pri(test_client_ip, download = 1, upload = 1)

firewall_gui()
