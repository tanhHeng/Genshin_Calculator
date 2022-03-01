import socket 
import struct
import os
import time
import threading
import sys

# data of socket and file datapath
ADDR = ('192.168.124.8',10086) # Sever Address
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')

# Sever
def Reveiver_File_Server():

    sendFileSever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sendFileSever.bind(ADDR)
    sendFileSever.listen(10)
    print(u"等待连接...\n")
    def run(sendFileClient,addr):
        while not sendFileClient._closed:
            try:
                print(u"客户端已连接—> \n[IP]{} [端口]{}".format(addr[0],addr[1]))

                sendFileClient.send('Python3-genshin_calculator-v2.0.6'.encode(encoding='utf-8')) #发送verion
                checkUpdate = sendFileClient.recv(10240).decode(encoding='utf-8') #接收更新请求
                print('<%s>[响应消息]'%addr[1]+checkUpdate)
                if checkUpdate == 'install':
                    filename = 'GenshinCalculator.zip'
                elif checkUpdate == 'update-cal':
                    filename = '../GenshinCalculator/packages/__genshin_calculator.py'
                elif checkUpdate == 'update-ui':
                    filename = '../GenshinCalculator/packages/__gs_calculator_ui.py'
                elif 'install-' in checkUpdate:
                    checkUpdate = checkUpdate.replace('install-','')
                    filename = 'packages/%s.zip'%checkUpdate
                else:
                    filename = ''
                    sendFileClient.close()
                    print(u"<%s>连接已关闭\n"%addr[1])
                if filename != '':
                    print('<%s>传输文件'%addr[1]+filename)
                    fhead=struct.pack(bytes('128s11I'.encode('utf-8')),bytes(filename.encode('utf-8')),
                                      0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
                    sendFileClient.send(fhead)
                    fp = open(filename,'rb')
                    while 1:
                        filedata = fp.read(BUFSIZE)
                        if not filedata: 
                            break
                        sendFileClient.send(filedata)
                    print(u"<%s>文件传送完毕，正在断开连接...\n"%addr[1])
                    if eval(sendFileClient.recv(1024).decode(encoding='utf-8')):
                        fp.close()
                        sendFileClient.close()
                        print(u"<%s>连接已关闭\n"%addr[1])
                        break
            except Exception as e:
                try:
                    print(e)
                    sendFileClient.send('False'.encode(encoding='utf-8'))
                    break
                except Exception as e:
                    print(e)
                    break
    while True:
        sendFileClient,addr = sendFileSever.accept()
        thread = threading.Thread(target=run, args=(sendFileClient,addr))
        thread.setDaemon(True)
        thread.start()
if __name__ == '__main__':
    thread = threading.Thread(target=Reveiver_File_Server())
    thread.setDaemon(True)
    thread.start()
    while True:time.sleep(1)
