import socket,os,sys,struct,zipfile,installer_ui,threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import QObject,pyqtSignal

# data of socket and file datapath
version = 'v0.0.0'
ADDR = ('cn-hn-dx-1.natfrp.cloud',16368)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
import time

OutputString = ''
def print(string,end='\n'): #替换了print函数
    global OutputString
    OutputString = OutputString+string+end
    send = Signal('MainWindow.setText')

# 客户端发送文件
def Send_File_Client():
    global BarRange
    global BarValue
    global OutputString
    BarRange = 0
    send = Signal('MainWindow.setBarRange')
    for i in range(5):
        try:
            userSever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            userSever.connect(ADDR)
            print('服务器连接成功')
            OutputString = '服务器连接成功'
            break
        except Exception as e:
            OutputString = ''
            print(str(e))
            print('[WARNING] 服务器连接失败\n重试%d/5...'%(i+1))
            if i == 4:
                print('[ERROR] 无法连接服务器')
                return False
            time.sleep(2)
    if userSever.recv(1024).decode(encoding='utf-8') != version: #接收vesion
        userSever.send('install'.encode(encoding='utf-8')) #发送更新请求
        fhead = userSever.recv(FILEINFO_SIZE)
        filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
        
        filename = filename.strip('\00'.encode('utf-8')).decode('utf-8')

        print('\n下载文件'+filename)
        
        fp = open(filename,'wb')
        restsize = filesize
        print(u"正在下载...")
        BarRange = filesize
        send = Signal('MainWindow.setBarRange')
        flush_time = time.time()
        recordString = OutputString
        recordLoadsize = 0
        loadedsize = 0
        b_mb = 1024**2
        while 1:
            if restsize > BUFSIZE:
                filedata = userSever.recv(BUFSIZE)
            else:
                filedata = userSever.recv(restsize)
            if not filedata: 
                break
            fp.write(filedata)
            restsize = restsize-len(filedata)
            
            if (time.time()-flush_time) >= 0.5:
                OutputString = recordString
                loadedsize = filesize-restsize
                print('共计|%.02fMB'%(filesize/b_mb))
                print('剩余|%.02fMB'%(restsize/b_mb))
                print('下载|%.02fMB'%(loadedsize/b_mb))
                print('速度|%.02fMB/s'%((loadedsize-recordLoadsize)/0.5/b_mb))
                recordLoadsize = loadedsize
                BarValue = loadedsize
                usend = Signal('MainWindow.setBarValue')
                flush_time = time.time()
            if restsize == 0:
                OutputString = filename+'下载完成\n'
                break
    userSever.send('True'.encode(encoding='utf-8'))
    

    fp.close()
    userSever.close()
    print(u"连接已关闭..." )
    BarRange = 0
    send = Signal('MainWindow.setBarRange')
    return True

def main():
    if Send_File_Client():
        print('正在解压文件...')
        with zipfile.ZipFile('./GenshinCalculator.zip') as zf:
            zf.extractall()
        print('解压完成，正在删除临时文件...')
        os.remove('GenshinCalculator.zip')
        try: os.remove('installer.exe')
        except: pass
        print('下载完成')
    print('将在3秒内退出...')
    time.sleep(3)
    MainWindow.close()

class Signal(QObject):
    signal1 = pyqtSignal()#声明无参数的信号
    def __init__(self,connect_f,parent=None):
        super(Signal,self).__init__(parent)
        self.signal1.connect(eval(connect_f))#将信号连接到打印函数
        self.signal1.emit() #发送信号
class installerMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(installerMainWindow, self).__init__(parent)
    def setText(self):
        global OutputString
        ui.textEdit.setPlainText(OutputString)
    def setBarRange(self):
        global BarRange
        ui.progressBar.setRange(0,BarRange)
    def setBarValue(self):
        global BarValue
        ui.progressBar.setValue(BarValue)


app = QApplication(sys.argv)
ui = installer_ui.Ui_MainWindow()
MainWindow = installerMainWindow()
ui.setupUi(MainWindow)
thread = threading.Thread(target=main)
thread.setDaemon(True)
thread.start()
if __name__ == '__main__':
    MainWindow.show()
    sys.exit(app.exec_())
time.sleep(1)
