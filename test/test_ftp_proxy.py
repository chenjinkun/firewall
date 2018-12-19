import test_config
from ftp_proxy import ftp_proxy
from db_init import init
from db_policy import add_SOURCEIP, add_TARGETIP, add_file_type, add_ip_pri

test_client_ip = '192.168.31.223'

init()
add_SOURCEIP(test_client_ip)
add_TARGETIP('188.131.204.91')
add_file_type('.ppt', download = 0)
add_ip_pri(test_client_ip, download = 1)
# start_proxy(8888)

firewall = ftp_proxy(8888)
firewall.run()
