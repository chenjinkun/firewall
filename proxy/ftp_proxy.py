import __init__
import socket
import select
import threading
import re
import struct
from db_policy import check_SOURCEIP, check_TARGETIP
from proxy_control import control

MAX_LISTEN = 10
SO_ORIGINAL_DST = 80

class ftp_proxy:
    def __init__(self, lsport):
        self.lsport = lsport
        self.running = 0

    def proxy_func(self, cc_s, client_ip):
        print("enter proxy func")
        server_addr_in = cc_s.getsockopt(socket.SOL_IP, SO_ORIGINAL_DST, 16)
        (proto, port, a,b,c,d) = struct.unpack('!HHBBBB', server_addr_in[:8])
        server_ip = '%d.%d.%d.%d' % (a,b,c,d)

        if not check_TARGETIP(server_ip):
            print "this server {} is forbidden by the rule".format(server_ip)
            cc_s.close()
            return

        #connect ftp server
        pc_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pc_s.connect((server_ip, port))
        print(server_ip, port)

        while self.running:
            rset, wset, error = select.select([pc_s, cc_s], [], [])
            if pc_s in rset:
                msg = pc_s.recv(4096)
                if len(msg) == 0:
                    break

                print(msg)

                if not control(client_ip, msg):
                    continue

                cc_s.send(msg)

            if cc_s in rset:
                msg = cc_s.recv(4096)
                if len(msg) == 0:
                    break

                print(msg)

                if not control(client_ip, msg):
                    continue

                pc_s.send(msg)

        print "stop the proxy"

    def start_proxy(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('',self.lsport))
        s.listen(10)
        print("start listening")

        while True:
            sock, addr = s.accept()
            print "find client", addr
            if check_SOURCEIP(addr[0]):
                t = threading.Thread(target=self.proxy_func, args=(sock,addr[0],))
                t.setDaemon(True)
                t.start()
                t.join()

                print "fuck stop"
                break
            else:
                print("this client is forbidden by the rule")
                sock.close()
                continue

        print "stop this test"

    def run(self):
        self.running = 1
        self.t = threading.Thread(target=self.start_proxy, args=())
        self.t.setDaemon(True)

    def stop(self):
        self.running = 0


if __name__ == '__main__':
    lsport = 8888
    start_proxy(lsport)
