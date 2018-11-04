import socket
import select
import threading
import re
import struct

MAX_LISTEN = 10
SO_ORIGINAL_DST = 80

def checkclient(addr):
    return True

def checkserver(addr):
    return True

def checkuser(name):
    return True

def control(msg):
    return True

# def data_transfer_pasv(pc_s, pd_s, cc_s, cd_s):
#     while True:
#         msg = cc_s.recv(4096)
#
#         if len(msg) == 0:
#             return
#
#         if not control(msg):
#             continue
#
#         pc_s.send(msg)
#         msg = pc_s.recv(4096)
#         cc_s.send(msg)
#
#         while True:
#             rset, wset, error = select.select([pd_s, cd_s], [], [])
#             if pd_s in rset:
#                 msg = pd_s.recv(4096)
#                 if len(msg) == 0:
#                     break
#
#                 cd_s.send(msg)
#
#             if cd_s in rset:
#                 msg = cd_s.recv(4096)
#                 if len(msg) == 0:
#                     break
#
#                 pd_s.send(msg)

def deal_with_connect(pc_s, cc_s):
    while True:
        rset, wset, error = select.select([pc_s, cc_s], [], [])
        if pc_s in rset:
            msg = pc_s.recv(4096)
            if len(msg) == 0:
                break

            print(msg)
            cc_s.send(msg)

            # if msg.find(b"227") != -1:
                # info = re.findall(r'\d+', msg.decode())
                # serv_dataport = int(info[5])*256 + int(info[6])
                # serv_addr = '%d.%d.%d.%d' % (int(info[1]), int(info[2]), int(info[3]), int(info[4]))
                #
                # new_msg = "227 Entering Passive Mode (192,168,0,103,211,175).\r\n"
                # print(new_msg.encode())
                # cc_s.send(new_msg.encode())
                #
                # ds = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # ds.bind(('0.0.0.0', 54191))
                # ds.listen(10)
                #
                # print("start listening")
                #
                # cd_s, addr = ds.accept()
                #
                # print("successfully connect client data")
                #
                # pd_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # pd_s.connect((serv_addr, serv_dataport))
                #
                # print("successfully connect server data")
                #
                # data_transfer_pasv(pc_s, pd_s, cc_s, cd_s)
                # continue

        if cc_s in rset:
            msg = cc_s.recv(4096)
            if len(msg) == 0:
                break
            print(msg)

            pc_s.send(msg)

def proxy_func(cc_s):
    print("enter proxy func")
    server_addr_in = cc_s.getsockopt(socket.SOL_IP,SO_ORIGINAL_DST, 16)
    (proto, port, a,b,c,d) = struct.unpack('!HHBBBB', server_addr_in[:8])
    server_ip = '%d.%d.%d.%d' % (a,b,c,d)

    if not checkserver(server_ip):
        cc_s.close()
        return

    #connect ftp server
    pc_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pc_s.connect((server_ip, port))
    print(server_ip, port)

    deal_with_connect(pc_s, cc_s)

def start_proxy(lsport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('',lsport))
    s.listen(10)
    print("start listening")

    while True:
        sock, addr = s.accept()
        print("find client", addr)
        if checkclient(addr):
            t = threading.Thread(target=proxy_func, args=(sock,))
            t.start()
        else:
            sock.close()
            continue

if __name__ == '__main__':
    lsport = 8888
    start_proxy(lsport)
