# -*- coding: utf-8 -*-

import __init__
from db_policy import filetype_blacklist

#import for test
from db_init import init
from db_policy import add_file_type, check_pri
#end import for test

def control(ip, msg):
    msg = msg.decode('gbk').encode('utf-8')

    #check if this file_type can be uploaded
    if msg.find('STOR'.encode('utf-8')) != -1:
        blacklist_type = filetype_blacklist('upload')
        for black_type in blacklist_type:
            if msg.find(black_type.encode('utf-8')) != -1:
                print "type {} can not be uploaded".format(black_type)
                return False

        #check if this ip can upload files
        if not check_pri(str(ip), 'upload'):
            print "ip {} cannot upload files".format(str(ip))
            return False

    #check if this file_type can be downloaded
    if msg.find('RETR'.encode('utf-8')) != -1:
        blacklist_type = filetype_blacklist('download')
        for black_type in blacklist_type:
            if msg.find(black_type.encode('utf-8')) != -1:
                print "type {} can not be downloaded".format(black_type)
                return False

        #check if this ip can download files
        if not check_pri(str(ip), 'download'):
            print "ip {} cannot download files".format(str(ip))
            return False

    #todo: add it in db_policy
    if msg.find('CWD') != -1:
        pass

    #check if this ip can make directory
    if msg.find('MKD'.encode('utf-8')) != -1:
        if not check_pri(str(ip), 'mkdir'):
            print "ip {} cannot make directories".format(str(ip))
            return False

    #check if this ip can delete files
    if msg.find('DELE'.encode('utf-8')) != -1:
        if not check_pri(str(ip), 'delet'):
            print "ip {} cannot delete files".format(str(ip))
            return False

    return True

if __name__ == '__main__':
    init()
    add_file_type('.ppt', download = 0)
    msg = 'RETR hello.ppt'
    if control(0, msg):
        print "accept"
    else:
        print "refused"
