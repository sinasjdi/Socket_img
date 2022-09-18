import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib

#HOST='192.168.2.205'
PORT=8485

s0=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket 0 created')

s0.bind(('',PORT))
print('Socket 0 bind complete')
s0.listen(10)
print('Socket 0 now listening')

conn0,addr0=s0.accept()

data0 = b""
payload_size0 = struct.calcsize(">L")
print("payload_size0: {}".format(payload_size0))



PORT=8486
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket1 created')

s1.bind(('',PORT))
print('Socket 1 bind complete')
s1.listen(10)
print('Socket 1 now listening')

conn1,addr1=s1.accept()

data1 = b""
payload_size1= struct.calcsize(">L")
print("payload_size1: {}".format(payload_size1))







while True:
    while len(data0) < payload_size0:
       # print("Recv: {}".format(len(data)))
        data0 += conn0.recv(4096)

    #print("Done Recv: {}".format(len(data)))
    packed_msg_size0 = data0[:payload_size0]
    data0 = data0[payload_size0:]
    msg_size0 = struct.unpack(">L", packed_msg_size0)[0]
    #print("msg_size: {}".format(msg_size))
    while len(data0) < msg_size0:
        data0 += conn0.recv(4096)
    frame_data0 = data0[:msg_size0]
    data0 = data0[msg_size0:]

    frame0=pickle.loads(frame_data0, fix_imports=True, encoding="bytes")
    frame0 = cv2.imdecode(frame0, cv2.IMREAD_COLOR)
    
    #print("Hello")
    while len(data1) < payload_size1:
       # print("Recv: {}".format(len(data)))
        data1 += conn1.recv(4096)
    #print("Hello2")
    #print("Done Recv: {}".format(len(data)))
    packed_msg_size1 = data1[:payload_size1]
    data1 = data1[payload_size1:]
    msg_size1 = struct.unpack(">L", packed_msg_size1)[0]
    #print("msg_size: {}".format(msg_size))
    #print("Hello3")
    while len(data1) < msg_size1:
        data1 += conn1.recv(4096)
    frame_data1 = data1[:msg_size1]
    #print("Hello4")
    data1 = data1[msg_size1:]

    frame1=pickle.loads(frame_data1, fix_imports=True, encoding="bytes")
    frame1 = cv2.imdecode(frame1, cv2.IMREAD_COLOR)
    #cv2.imshow('ImageWindow1',frame1)
    cv2.namedWindow("#2")
    cv2.imshow('#2',frame1)
    cv2.waitKey(1)

    cv2.namedWindow("#1")
    cv2.imshow('#1',frame0)
    cv2.waitKey(1)
    #print("Hello5")

