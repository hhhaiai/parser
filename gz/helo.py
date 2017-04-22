#  -*- coding: utf-8 -*- 
'''
@Copyright © 2017 sanbo Inc. All rights reserved.
@Description: todo
@Version: 1.0
@Create: 2017年3月14日 下午11:38:16 
@Author: sanbo
'''
import gzip, binascii, os  
from cStringIO import StringIO  
  
def gzip_compress(raw_data):  
    buf = StringIO()  
    f = gzip.GzipFile(mode='wb', fileobj=buf)  
    try:  
        f.write(raw_data)  
    finally:  
        f.close()  
    return buf.getvalue()  
  
def gzip_uncompress(c_data):  
    buf = StringIO(c_data)  
    f = gzip.GzipFile(mode='rb', fileobj=buf)  
    try:  
        r_data = f.read()  
    finally:  
        f.close()  
    return r_data  
  
  
def compress_file(fn_in, fn_out):  
    f_in = open(fn_in, 'rb')  
    f_out = gzip.open(fn_out, 'wb')  
    f_out.writelines(f_in)  
    f_out.close()  
    f_in.close()  
  
def uncompress_file(fn_in, fn_out):  
    f_in = gzip.open(fn_in, 'rb')  
    f_out = open(fn_out, 'wb')  
    file_content = f_in.read()  
    f_out.write(file_content)  
    f_out.close()  
    f_in.close()  
  
  
if __name__ == '__main__':  
    in_data = 'hello, world!'  
    print in_data  
    out_data = gzip_compress(in_data)  
    print binascii.hexlify(out_data)  
  
    r_data = gzip_uncompress(out_data)  
    print r_data  
  
#    raw_f = '/opt/log/raw/access.log_HLJYD-ICS-68_20150609040506.old'  
#    #raw_f = '/home/taoyx/program_develop/python_dev/a.html';  
#  
#    gzip_f2 = '/opt/log/raw/access.log_HLJYD-ICS-68_20150609040506.gz'  
#    #gzip_f2 = '/home/taoyx/program_develop/python_dev/log_gz/cpm.access.log-20150225.gz'  
#    #gzip_f2 = '/home/taoyx/program_develop/python_dev/a.html.1.gz'  
#    compress_file(raw_f, gzip_f2)  
#  
#    #gunzip_f = '/home/taoyx/program_develop/python_dev/log_gz/cpm.access.log-20150225.old'  
#    #gunzip_f = '/home/taoyx/program_develop/python_dev/a.html.1'  
#    #uncompress_file(gzip_f2, gunzip_f)  
