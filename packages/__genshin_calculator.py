import sys, os
sys.path = []
path = os.getcwd()
for i in ['',
          '\\DLLs',
          '\\lib',
          '\\lib\\site-packages',
          '\\lib\\site-packages\\win32',
          '\\lib\\site-packages\\win32\\lib',
          '\\lib\\site-packages\\Pythonwin',
          ]:
	sys.path.append(path+'\\packages'+i)
# Packages path. Change it to your path when you are using.

import __gs_calculator_ui as calculator_ui
import threading, time, pytesseract, struct, socket, zipfile
import PyQt5
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PIL import Image, ImageGrab
from matplotlib import pyplot as plt
import numpy as np
print(str(sys.path))

try:
    os.mkdir('images')
    os.mkdir('datas')
except: pass

__version__ = 'Python3-genshin_calculator-v2.0.6'

############################## 开始定义类 ##############################


#################### 帮助 ####################

class _help_():
    def __init__(__help__):
        global __version__
        __help__.menu_help = '''
*************** Help Menu 帮助菜单 ***************
您可以通过以下命令查看帮助
全部帮助 ..... > help.help
帮助菜单 ..... > help.menu
程序信息 ..... > help.progress
更新日志 ..... > help.changelog
资源包与完整性 > help.package
文件帮助 ..... > help.data
指令帮助 ..... > help.command
所有指令 ..... > help.all_command
计算器使用帮助 > help.cal
帮助文档 ..... > docs.qq.com/doc/DRkdwdFdQampkeXJq'''
        __help__.progress_help = '''
********** Progress Information 程序信息 **********
%s
update          | 22_02_25
prgram by       | tanh_Heng|tanh丶桁
email at        | 2196226582@qq.com
bilibili.com    | uid-454721668'''%__version__
        __help__.changelog_help = '''
*********************************** Changelog 更新日志 ***********************************
# 此更新日志已经过删减，将不再区分beta版与正式版。完整更新日志详见：
原神计算器帮助文档 docs.qq.com/doc/DRkdwdFdQampkeXJq
-================================ v1.0.0 update-22_02_07 ================================-
正式版
    genshin_calculator开始使用
-================================ v1.1.5 update-22_02_08 ================================-
正式版
    修复已知bug
    支持了浮点数输入
    支持了'+''*'输入
    优化了输出格式
    加入了[help - All Command|帮助 - 所有指令]
    加入了自动清空输出台，您可以通过\'auto_clear(True/False)\'调整此选项
    加入了[help - Data Help|帮助 - 文件帮助]
    优化了部分[help|帮助]的显示
    优化了存储路径
    支持修改[path|路径]
    修复了读取新文件时无法计算'*''+'的恶性bug
    修复了计算伤害时报错的问题
-================================ v1.1.6 update-22_02_14 ================================-
正式版
    更改了伤害计算公式，修复了原先计算公式伤害乘区错误的问题
-================================ v1.2.0 update-22_02_20 ================================-
正式版
    此版本不兼容1.2.0以下的<data_character.txt>
    修复了本地Notebook无法读取数据的问题
    支持了本地python，增加了本地<Calculator Launcher For Python.py>启动器
    Notebook启动器更改为<Calculator Launcher For Notebook.ipynb>
    支持了windows端<Launcher.exe>，此启动器可脱离python环境使用
    本地计算器删减了[Changelog|更新日志]，将[update-22_02_08]的更新进行了整合
    加入了[录入圣遗物]功能
    预计将在1.3.0支持圣遗物计算器包<packages/ShengYiWu_calculator>，并改善原先角色数据，
    届时旧角色数据<data_character.txt>将不可用，请联系我们进行更新
-================================ v2.0.1 update-22_02_25 ================================-
正式版
    ！！！重大更新 ！！！
    加入了UI界面，替换了控制台
    UI功能：
        保留了原有的所有功能，加入了快捷按键（常用工具），方便使用
        加入了服务控制，支持 运行/中断/暂停/退出 服务
        加入了Tips
    重置了应用图标
    修复了v2.0.0-beta版中无法录入数据与录入圣遗物的问题
    优化了运行状态下的cpu占用，相对v2.0.0-beta减少了约95%的cpu占用
-================================ v2.0.3 update-22_02_28 ================================-
正式版
    优化了应用文件存储方式与路径
    支持了installer.exe下载安装
    支持了检查更新，大幅减少了日常更新占用空间大小'''
        __help__.package_help = '''
******************** Package Help 资源包帮助 ********************
通过以下指令安装或重装资源包
指令标准 ...... > install- (package)
安装tesseract包 > install- Tesseract-OCR'''
        __help__.data_help = '''
************************************* Data Help 文件帮助 *************************************
[Folder]   datas .................. > 保存的角色数据与记录
[Folder]   past_version ........... > 过去的版本(部分)
[Folder]   beta_version ........... > 最近的Beta版本(部分)
[Python]   genshin_calculator.py .. > 当前使用的版本包
[Notebook] genshin_calculator.ipynb > 启动程序
·如果您需要更改<datas>文件路径，请在当前使用的版本包中，更改第4行[self.path = 'xxxx/']路径'''
        __help__.command_help = '''
************************************ Command Help 指令帮助 ************************************
语言：简体中文
在指令栏中，您可以使用三种方法输入指令
·中文指令 ——最直接，且最易理解的，适合一般使用
·集合指令 ——通过函数名调用<genshin_calculator>中的函数，适合一般使用
·Python指令 ——以标准Python代码的形式调用，适合管理员调试
以下是常用指令对应表
| 中文指令 |      集合指令     |            Python指令             |           说明           |
| 录入数据 |  character_input  |  gs_calculator.character_input()  |     录入新的角色数据     |
| 计算伤害 | injury_calculator | gs_calculator.injury_calculator() |  输入角色面板，计算伤害  |
| 查询记录 | injury_read_data  | gs_calculator.injury_read_data()  | 查询已保存的历史伤害记录 |
|   ——   |       clear       |               ——                |       清空所有输出       |
|   ——   |     help.help     |     gs_calculator.help.help()     |       查看所有帮助       |
|   退出   |        ——       |               stop                |         退出程序         |
|   ——   |        ——       |               ——                |           ——           |
若出现[xxx Error]，您应当检查您的指令输入后重启程序。您也可以联系我们反馈问题'''
        __help__.all_command_help = '\n********** All Command 所有指令 **********\n'
        for i in ['__version__','auto_clear_command','help','KangXing','info','load_inj','Data','Include','Data_inj',
                  'character_input()','injury_calculator()','injury_read_data()','auto_clear(_set_)']:
            __help__.all_command_help = __help__.all_command_help+'gs_calculator.'+i+'\n'
        __help__.all_command_help = __help__.all_command_help+'其余指令请使用\'print(dir(gs_calculator))\'查看'

        __help__.cal_help = '''
***************************** Calculator Usage Help 计算器使用帮助 *****************************
·输入数据
您需要按照标准格式输入角色数据。
录入数据时，需要录入的数据包括角色的：
    角色名称
    属性（元素力）
    使用武器
    基础面板(攻击|防御|生命|元素精通|增伤|暴击率|暴击伤害)
    普通攻击倍率
    重击倍率
    元素战技倍率
    元素爆发倍率
计算伤害时，需要输入的数据包括角色的：
    攻击力
    防御力
    生命值
    元素精通
    元素伤害加成
    额外伤害加成
    暴击率
    暴击伤害
对于单项数据，如果角色的没有该项数据，直接按下[Enter]继续下一项输入即可；
对于'输入空值退出',在角色该倍率录入完成后，直接按下[Enter]键即可继续下一项录入；
其中，在输入时带有'[%]'标识的，应按照百分数格式或浮点数格式输入；
从1.1.2版本开始，支持了'*''+'输入，其中'*'即为'x'(乘号)；
其余各项数据则按照常规格式输入即可。
    例如：
    1.
    属性（元素力）
    标准格式：火
    2.
    攻击力
    标准格式：2174
    3.
    元素伤害加成[%]
    标准格式：61.6% 或 0.616
    4.
    元素战技点按第3段倍率[%]/输入空值退出
    标准格式：177.2% 或 1.772
    标准格式：113.2%+113.2% 或 113.2%*2 [需要1.1.2及以上]
    5.
    元素战技长按第1段倍率[%]/输入空值退出
    此角色元素战技没有长按
    标准操作：直接按下[Enter]
·计算伤害
您需要按照要求与格式输入角色数据{详见[Calculator Usage Help 计算器使用帮助 - 输入数据]}。
并且，您需要清楚，计算器并非适用于所有角色。对于部分角色的部分特殊机制或倍率，目前暂不支持。
计算完成后将会输出计算结果，多段伤害将以'|'分割。
·无法录入数据/计算伤害/查询记录
若计算器报错，您应当首先按照计算器报错内容，检查您的输入。
以下是各类报错的对应解决方案：
·录入数据/计算伤害-报错'存在数据录入错误'：
    检查您是否按照格式输入。
·计算伤害/查询记录-报错'该角色数据未设置'：
    您还没有设置该角色的数据。您应当先录入数据再计算伤害。
    您可以查看datas/data_chatacter.txt文件来检查已录入的数据，但并不建议您随意改动。
    您可以查看datas/data_ch_include.txt文件来检查已录入数据的角色，但并不建议您随意改动。
·查询记录-报错'还没有该角色的历史伤害记录'：
    您还没有计算过该角色的伤害并保存。您应当先计算伤害并保存，再查看记录。
    您可以查看datas/data_injurny.txt文件来检查已保存的角色的历史伤害记录，但并不建议您随意改动。
·查询记录-报错'错误序号'：
    检查您的序号是否输入正确。
若以上方案无法解决您的问题，请您联系我们{详见[Progress Information 程序信息]}'''
    def help(__help__):
        print('\n·———————genshin_calculator.help-v1.1.2-update_22_02_14|原神计算器.帮助———————·\n')
        __help__.menu()
        __help__.progress()
        __help__.changelog()
        __help__.package()
        __help__.data()
        __help__.command()
        __help__.all_command()
        __help__.cal()
        print('\n·——————————————————————|——————————————————————·\n')
    def menu(__help__):
        print(__help__.menu_help)
    def progress(__help__):
        print(__help__.progress_help)
    def changelog(__help__):
        print(__help__.changelog_help)
    def package(__help__):
        print(__help__.package_help)
    def data(__help__):
        print(__help__.data_help)
    def command(__help__):
        print(__help__.command_help)
    def all_command(__help__):
        print(__help__.all_command_help)
    def cal(__help__):
        print(__help__.cal_help)


#################### 读写文件 ####################

class data():
        def __init__(self_data,name):
            self_data.name = name
        def read_data(self_data):
            try:
                with open(self_data.name,'r',encoding='utf-8') as load_data:
                    load_data.seek(0,0)
                    data_read = load_data.read()
                    data = []
                    for i in data_read.split('\n'):
                        data.append(i.split(';'))
                    load_data.close()
            except:
                with open(self_data.name,'x') as load_data:
                    load_data.close()
                    data = []
            return data
        def save_data(self_data,data):
            with open(self_data.name,'r+',encoding='utf-8') as load_data:
                data_save = ''
                for each_len in data:
                    for each_info in each_len:
                        data_save = data_save+str(each_info)+';'
                    data_save = data_save[:-1] + '\n'
                data_save = data_save[:-1]
                load_data.write(data_save)
                load_data.close()


#################### 圣遗物计算器 ####################

class ShengYiWu_calculator():
    global main_run
    def __init__(self):
        self.__version__ = '0.1.2'
        self.__help__ = '''genshin_calculator的附加包-用于圣遗物截屏与统计计算'''
    def prt_sc(self,times,wait=0.2):
        if ImageGrab.grabclipboard():
            sc_images = [ImageGrab.grabclipboard()]
        else:
            sc_images = [0]
        for i in range(times):
            while main_run[0]:
                try:
                    image = ImageGrab.grabclipboard()
                    if image != None:
                        if (abs(np.array(image)-np.array(sc_images[i])).sum() != 0):
                            sc_images.append(image)
                            print('\r已截图{}/{}'.format(i+1,times),end='')
                            break
                except OSError:
                    print('[WARNING] failed to open clipboard',end='')
                time.sleep(wait)
        sc_images.remove(sc_images[0])
        return sc_images
    def float_percentage(self,x):
            try:
                x = float(x)
                return round(x,3)
            except:
                pass
            try:
                if x[-1] == '%':
                    try:
                        x = float(x[:-1])/100
                        return round(x,3)
                    except:return False
                else:return False
            except:return False
    def ShengYiWu_to_list(self,file,resize=False,show_image=False):
        img = Image.open(file).convert('L')
        img_arr = np.array(img)
        con = img_arr.reshape((img_arr.shape[0],img_arr.shape[1],1))
        img_arr = np.concatenate((con,con,con),axis=2)
        del con
        if resize:
            shape = img_arr.shape
            img_arr = img_arr[int(shape[0]*0.11):int(shape[0]*0.88),int(shape[1]*0.68):int(shape[1]*0.93),:]
            del shape
        if show_image:
            import matplotlib.pyplot as plt
            plt.figure(figsize=(4,6))
            plt.imshow(img_arr,cmap='gray')
        text = str(pytesseract.image_to_string(img_arr,lang='chi_sim',config='--psm 11 -c min_characters_to_try=5'))
        old = [' ','食','‘','’','“','”','\'',',']
        for i in old:
            text = text.replace(i,'')
        text = text.replace('\n\n','\n')
        def find(string):
            if self.float_percentage(string)and (len(string)>1):
                return True
            if string in ['生之花','死之羽','时之沙','空之杯','理之冠']:
                return True
            for k in ['生命','暴击','攻击','防御','元素','治疗']:
                if (k in string)and(('+'in string)or(len(string)<8)):
                    return True
        text_list = text.split('\n')
        out_list = []
        for i in text_list:
            if find(i):
                out_list.append(i)
        return out_list
    def ShengYiWu_total(self,SYW_list):
        ShengYiWu_dict = {
            '攻击力+':0,
            '攻击力%':0,
            '防御力+':0,
            '防御力%':0,
            '生命值+':0,
            '生命值%':0,
            '元素精通':0,
            '元素伤害加成':0,
            '暴击率':0,
            '暴击伤害':0,
            '元素充能效率':0
            }
        check = []
        for i in SYW_list:
            if len(i) < 4:
                print('\n[错误] 无法识别的圣遗物')
                return False
            if i[0] in ['生之花','死之羽','时之沙','空之杯','理之冠']:
                if i[0] not in check:
                    check.append(i[0])
                else:
                    print('\n[错误] <'+i[0]+'>重复录入')
                    return False
            else:
                print('\n[错误] 未知圣遗物<'+i[0]+'>')
                return False
        if len(check) != 5:
            print('\n[错误] 圣遗物数量错误:<%d>'%len(check))
            return False
        del check
        for i in SYW_list:
            i.remove(i[0])
            i[0] = i[0]+'+'+i[1]
            i.remove(i[1])
            for k in i:
                k = list(k.split('+'))
                if ('元素伤害加成' in k[0]) or ('物理伤害加成' in k[0]):
                    ShengYiWu_dict['元素伤害加成'] += self.float_percentage(k[1])
                elif k[0] in ['攻击力','防御力','生命值']:
                    k[1] = self.float_percentage(k[1])
                    if k[1] < 1:
                        ShengYiWu_dict[k[0]+'%'] += k[1]
                    else:
                        ShengYiWu_dict[k[0]+'+'] += k[1]
                else:
                    ShengYiWu_dict[k[0]] += self.float_percentage(k[1])
        print(str(ShengYiWu_dict))
        return ShengYiWu_dict
    def imgs_show(self,imgs):
        fig = plt.figure(figsize=(12,18))
        for i in range(len(imgs)):
            ax = fig.add_subplot(1,len(imgs),i+1)
            shape = np.array(imgs[i]).shape
            ax.imshow(np.array(imgs[i])[int(shape[0]*0.11):int(shape[0]*0.88),int(shape[1]*0.68):int(shape[1]*0.93),:])
            plt.xticks([])
            plt.yticks([])
        plt.show()
    def prtsc_save(self):
        print('手动截图五次不同圣遗物后自动结束',end='')
        sc_images = self.prt_sc(5)
        #self.imgs_show(sc_images)
        print('\n在<images>文件夹中检查您的截图')
        try:
            for k in range(5):
                sc_images[k].save('images/image_'+str(k)+'.jpg')
            print('截屏已保存')
            return True
        except Exception as e:
            print('保存失败\n错误代码:'+str(e))
            return False
    def ShengYiWu_load_list_total(self):
        imgs_list=[]
        for i in range(5):
            imgs_list.append(self.ShengYiWu_to_list('images/image_%d.jpg'%i,resize=True))
            print('\r'+str(i+1)+'/5',end='')
        return self.ShengYiWu_total(imgs_list)


#################### 计算器 ####################

class genshin_calculator():

    def __init__(self):

        self.path = 'datas/'
        self.auto_clear_command = False

        class YuanSuFanYing():
            def __init__(fy, ShuXing, JingTong):
                fy.ShuXing = ShuXing
                fy.JingTong = JingTong
                fy.ZengFu = (25*self.JingTong)/((self.JingTong+1400)*9)
                fy.JuBian = (16*self.JingTong)/(self.JingTong+2000)
                #fy.JieJing = (40*self.JingTong)/((self.JingTong)*9)
            def get(fy,inj):
                if (fy.ShuXing == '火'):
                    return int(inj*1.5*(1+fy.ZengFu)),'蒸发'
                elif fy.ShuXing == '水':
                    return int(inj*2*(1+fy.ZengFu)),'蒸发'
                elif fy.ShuXing == '冰':
                    return int(inj*1.5*(1+fy.ZengFu)),'融化'
                else:
                    return None,None

        self.YuanSuFanYing = YuanSuFanYing

        self.data_character = data(self.path+'data_character.txt')
        self.data_ch_include = data(self.path+'data_ch_include.txt')
        self.data_injurny = data(self.path+'data_injurny.txt')
        self.data_ShengYiWu = data(self.path+'data_ShengYiWu.txt')
        self.data_weapon = data(self.path+'data_weapon.txt')
        self.KangXing = 0.5

        self.help = _help_()
        try:
            self.ShengYiWu_calculator = ShengYiWu_calculator()
        except:
            self.ShengYiWu_calculator = None
            print('[WARNING] cannot load ShengYiWu_calculator')

    def auto_clear(self,_set_):
        self.auto_clear_command = bool(_set_)
        print('\n\n<calculator> [auto_clear] set auto_clear to {}\n已设置auto_clear为{}\n\n>>>'.format(
            self.auto_clear_command,self.auto_clear_command),end='')

    def DuoDuanBeiLv(self,txt):
        global main_run
        BeiLv = []
        i = 0
        while main_run[0]:
            i += 1
            k = input(txt+'第'+str(i)+'段倍率[%]/输入空值退出:')
            if k == '':
                break
            if '*' in k:
                k = k.split('*')
                BeiLv.append(str(self.float_percentage(k[0]))+'*'+k[1])
            elif '+' in k:
                k = k.split('+')
                apd = ''
                for t in k:
                    apd = apd+str(self.float_percentage(t))+'+'
                BeiLv.append(apd[:-1])
                del apd
            else:
                BeiLv.append(self.float_percentage(k))
        return BeiLv

    def DuoDuanShangHai(self,txt,BeiLv):
        print('角色'+txt+'伤害:',end='')
        inj = []
        inj_fy = []
        try:
            for k in BeiLv:
                if '*' in k:
                    k = k.split('\'')[1].split('*')
                    inj_BaoJi = self.inj*(1+self.BaoShang)*float(k[0])*self.KangXing
                    inj.append(str(int(inj_BaoJi))+'*'+k[1])
                    inj_fy.append(str(self.FanYing.get(inj_BaoJi)[0])+'*'+k[1])
                elif '+' in k:
                    k = k.split('\'')[1].split('+')
                    inj_str = ''
                    inj_fy_str = ''
                    for l in k:
                        inj_BaoJi = self.inj*(1+self.BaoShang)*float(l)*self.KangXing
                        inj_str = inj_str+str(int(inj_BaoJi))+'+'
                        inj_fy_str = inj_fy_str + str(self.FanYing.get(inj_BaoJi)[0])+'+'
                    inj.append(inj_str[:-1])
                    inj_fy.append(inj_fy_str[:-1])
                else:
                    inj_BaoJi = self.inj*(1+self.BaoShang)*float(k)*self.KangXing
                    inj.append(str(int(inj_BaoJi)))
                    inj_fy.append(str(self.FanYing.get(inj_BaoJi)[0]))
            for i in inj:
                print(i+'|',end='')
            print('  共计:'+str(sum(eval(i) for i in inj)))
            if self.FanYing.get(inj_BaoJi)[1] != None:
                print('    '+'  '*len(txt)+self.FanYing.get(inj_BaoJi)[1]+':',end='')
                for i in inj_fy:
                    print(i+'|',end='')
                print('  共计:'+str(sum(eval(i) for i in inj_fy)))
        except:
            print('\r',end='')

    def float_percentage(self,x):
        try:
            x = float(x)
            return round(x,3)
        except:
            pass
        if len(x) == 0:
            return 'Err'
        if x[-1] == '%':
            try:
                x = float(x[:-1])/100
                return round(x,3)
            except:
                return 'Err'
        else:
            return 'Err'

    def character_input(self):
        print('\n<计算器> [录入数据]')
        print('录入角色数据请以标准格式录入，例如[攻击力 2143][普攻倍率 132%]')
        if input('开始录入/y:')=='y':
            info = []
            info.append(input('角色名称:'))
            info.append(input('属性(元素力):'))
            info.append(input('使用武器:'))
            k = []
            for i in ['基础攻击:','基础防御:','基础生命:','基础元素精通:','基础增伤:','基础暴击率','基础暴击伤害']:
                k.append(self.float_percentage(input(i)))
                if 'Err' in k: print('存在数据录入错误，录入失败'); return None
            info.append(k)
            del k
            info.append(self.DuoDuanBeiLv('普通攻击'))
            info.append(self.DuoDuanBeiLv('重击'))
            info.append(self.DuoDuanBeiLv('元素战技点按'))
            info.append(self.DuoDuanBeiLv('元素战技长按'))
            info.append(self.DuoDuanBeiLv('元素爆发'))
            self.info = info
            for i in range(2,5):
                if 'Err' in self.info[i]:
                    print('存在数据录入错误，录入失败')
                    return None    
            print('请确认录入数据: '+str(info))
            if input('录入完成，保存y/n') == 'y':
                self.Data = self.data_character.read_data()
                if [''] in self.Data:
                    self.Data.remove([''])
                self.Include = self.data_ch_include.read_data()
                if [''] in self.Include:
                    self.Include.remove([''])
                self.Data.append(self.info)
                self.Include.append([self.info[0]])
                self.data_ch_include.save_data(self.Include)
                self.data_character.save_data(self.Data)
                print('保存完成')
            else:
                print('取消保存')
        else:
            print('录入失败')

    def injury_calculator(self):
        print('\n<计算器> [计算伤害]')
        self.ch_name = input('角色名称:')
        self.Include = self.data_ch_include.read_data()
        if [self.ch_name] in self.Include:
            self.data_index = self.Include.index([self.ch_name])
            self.info = self.data_character.read_data()[self.data_index]
            self.ShuXing = self.info[1]
            try:
                self.atk = int(input('攻击力'))
                self.FangYu = int(input('防御力'))
                self.ShengMing = int(input('生命值'))
                self.JingTong = int(input('元素精通'))
            except:
                print('存在数据录入错误，录入失败')
                return None
            self.YuanSuJiaCheng = self.float_percentage(input('元素伤害加成[%]'))
            self.atkJiaCheng = self.float_percentage(input('额外伤害加成[%]'))
            self.BaoJi = self.float_percentage(input('暴击率[%]'))
            self.BaoShang = self.float_percentage(input('暴击伤害[%]'))
            try:
                self.atk+self.FangYu+self.JingTong+self.YuanSuJiaCheng+self.atkJiaCheng+self.BaoJi+self.BaoShang
            except:
                print('存在数据录入错误，录入失败')
                return None 
            self.FanYing = self.YuanSuFanYing(self.ShuXing,self.JingTong)
            self.inj = (self.atk)*(1+self.YuanSuJiaCheng+self.atkJiaCheng)
            self.DuoDuanShangHai('普攻',self.info[4][1:-1].split(','))
            self.DuoDuanShangHai('重击',self.info[5][1:-1].split(','))
            self.DuoDuanShangHai('元素战技点按',self.info[6][1:-1].split(','))
            self.DuoDuanShangHai('元素战技长按',self.info[7][1:-1].split(','))
            self.DuoDuanShangHai('元素爆发',self.info[8][1:-1].split(','))
            if input('保存记录y/n') == 'y':
                self.Data_inj = self.data_injurny.read_data()
                if [''] in self.Data_inj:
                    self.Data_inj.remove([''])
                self.Data_inj.append([self.data_index,self.atk,self.FangYu,self.JingTong,self.YuanSuJiaCheng,self.atkJiaCheng,self.BaoJi,self.BaoShang])
                self.data_injurny.save_data(self.Data_inj)
                print('保存完成')
            else:
                print('取消保存')
        else:
            print('该角色数据未设置')

    def injury_read_data(self):
        print('\n<计算器> [查询记录]')
        self.ch_name = input('角色名称:')
        try:
            self.Include = self.data_ch_include.read_data()
        except:
            print('该角色数据未设置，查询失败')
            return None
        try:
            self.Data_inj = self.data_injurny.read_data()
        except:
            print('还没有该角色的历史伤害记录，查询失败')
            return None
        if [self.ch_name] in self.Include:
            self.data_index = self.Include.index([self.ch_name])
        else:
            print('该角色数据未设置，查询失败')
            return None
        self.load_inj = []
        for i in self.Data_inj:
            try:
                if self.data_index == int(i[0]):
                    self.load_inj.append(i[1:])
            except: pass
        if self.load_inj == []:
            print('还没有该角色的历史伤害记录，查询失败')
            return None
        print('查询到历史记录')
        print('序号/伤害/精通/元素伤害加成/额外伤害加成/暴击率/暴击伤害')
        k = 0
        for i in self.load_inj:
            print(str(k)+' '+str(i))
            k += 1
        try:
            self.load_inj = self.load_inj[int(input('输入序号以查看结果-'))]
        except:
            print('错误序号，查询失败')
            return None
        self.info = self.data_character.read_data()[self.data_index]
        self.ShuXing = self.info[1]
        self.atk = int(self.load_inj[0])
        self.FangYu = int(self.load_inj[1])
        self.JingTong = int(self.load_inj[2])
        self.YuanSuJiaCheng = float(self.load_inj[3])
        self.atkJiaCheng = float(self.load_inj[4])
        self.BaoJi = float(self.load_inj[5])
        self.BaoShang = float(self.load_inj[6])
        self.FanYing = self.YuanSuFanYing(self.ShuXing,self.JingTong)
        self.inj = (self.atk)*(1+self.YuanSuJiaCheng+self.atkJiaCheng)
        print('角色名称:'+str(self.ch_name))
        print('属性:'+self.ShuXing)
        print('攻击力:'+str(self.atk))
        print('防御力:'+str(self.FangYu))
        print('元素精通:'+str(self.JingTong))
        print('元素伤害加成:'+str(self.YuanSuJiaCheng))
        print('额外伤害加成:'+str(self.atkJiaCheng))
        print('暴击率:'+str(self.BaoJi))
        print('暴击伤害:'+str(self.BaoShang))
        self.DuoDuanShangHai('普攻',self.info[4][1:-1].split(','))
        self.DuoDuanShangHai('重击',self.info[5][1:-1].split(','))
        self.DuoDuanShangHai('元素战技点按',self.info[6][1:-1].split(','))
        self.DuoDuanShangHai('元素战技长按',self.info[7][1:-1].split(','))
        self.DuoDuanShangHai('元素爆发',self.info[8][1:-1].split(','))
        print('查询完成')

    def ShengYiWu_input(self):
        try:
                if not self.ShengYiWu_calculator:
                    print('[WARNING] cannot load ShengYiWu_calculator\n此功能无法使用')
                    return False
                print('\n<圣遗物> [录入圣遗物]')
                if input('开始录入/y:') != 'y':
                    return False
                if self.ShengYiWu_calculator.prtsc_save():
                    self.Data_ShengYiWu = self.data_ShengYiWu.read_data()
                    if [''] in self.Data_ShengYiWu:
                        self.Data_ShengYiWu.remove([''])
                    print('正在计算圣遗物...',end='')
                    tt = self.ShengYiWu_calculator.ShengYiWu_load_list_total()
                    tt_list = []
                    if not tt:
                        return False
                    for i in tt:
                        tt_list.append(tt[i])
                    self.Data_ShengYiWu.append(tt_list)
                    self.data_ShengYiWu.save_data(self.Data_ShengYiWu)
                    del tt,tt_list
                    print('保存完成')
        except Exception as e:
                print('\n[ERROR] '+str(e))
                print('此功能无法使用')


#################### 检查更新 ####################

ADDR = ('cn-hn-dx-1.natfrp.cloud',16368) # sever address
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')

# 客户端发送文件
def Send_File_Client(message):
    global calOutputString, __version__, filename, recordString
    BarRange = 0
    for i in range(5):
        try:
            userSever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            userSever.connect(ADDR)
            print('服务器连接成功')
            calOutputString = recordString + '服务器连接成功'
            break
        except Exception as e:
            calOutputString = recordString
            print(str(e))
            print('[WARNING] 服务器连接失败\n重试%d/5...'%(i+1))
            if i == 4:
                print('[ERROR] 无法连接服务器')
                return False
            time.sleep(2)
    sever_version = userSever.recv(1024).decode(encoding='utf-8')
    if (sever_version != __version__) or ('install' in message): #接收vesion
        userSever.send(message.encode(encoding='utf-8')) #发送更新请求

        fhead = userSever.recv(FILEINFO_SIZE)
        filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
        
        filename = filename.strip('\00'.encode('utf-8')).decode('utf-8')
        print('\n下载更新'+filename)
        
        fp = open(filename,'wb')
        restsize = filesize
        flush_time = time.time()
        recordString = calOutputString
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
                calOutputString = recordString
                loadedsize = filesize-restsize
                print('共计|%.02fMB'%(filesize/b_mb))
                print('剩余|%.02fMB'%(restsize/b_mb))
                print('下载|%.02fMB'%(loadedsize/b_mb))
                print('速度|%.02fMB/s'%((loadedsize-recordLoadsize)/0.5/b_mb))
                recordLoadsize = loadedsize
                flush_time = time.time()
            if restsize == 0:
                break
        userSever.send('True'.encode(encoding='utf-8'))
        fp.close()
        userSever.close()
        return True
    else:
        userSever.send('False'.encode(encoding='utf-8'))
        userSever.close()
        return 'lastest'

def checkUpdate():
    send = Signal('MainWindow.setAllEnabledFalse')
    print('检查更新\n\n下载文件时将禁用其他功能\n正在连接服务器...')
    def f():
        global recordString, calOutputString
        try:
            recordString = calOutputString
            s = Send_File_Client('update-cal')
            if s:
                if s == 'lastest':
                    print('\n已经是最新版本\n\n>>>')
                    send = Signal('MainWindow.setAllEnabledTrue')
                    return True
                recordString = calOutputString
                if Send_File_Client('update-ui'):
                        print('更新完成\n\n!!重启计算器以应用更新!!\n\n>>>',end='')
                        send = Signal('MainWindow.setAllEnabledTrue')
                        return True
            print('更新失败\n\n>>>',end='')
            send = Signal('MainWindow.setAllEnabledTrue')
            return False
        except Exception as e:
            print('\n[ERROR] '+str(e))
            print('更新失败\n\n>>>')
            send = Signal('MainWindow.setAllEnabledTrue')
            return False
    thr = threading.Thread(target=f)
    thr.setDaemon(True)
    thr.start()

def install(zip_package):
    def f():
            send = Signal('MainWindow.setAllEnabledFalse')
            global recordString, calOutputString
            recordString = calOutputString
            try:
                if Send_File_Client('install-'+zip_package):
                    global filename
                    print('正在解压文件...')
                    with zipfile.ZipFile(filename) as zf:
                        zf.extractall(path=os.getcwd()+'\packages')
                    print('解压完成，正在删除临时文件...')
                    try: os.remove(filename)
                    except: pass
                    print('下载完成\n')
                else:
                    print("没有指定的package: '%s'"%zip_package)
            except Exception as e:
                print('\n[ERROR]'+str(e))
                if str(e)[:10] == '[Errno 13]':
                        print('!!请在退出计算器后自行解压文件!!\n'+
                              '!!若解压后计算器无法启动请重装计算器!!')
            send = Signal('MainWindow.setAllEnabledTrue')
            print('\n>>>',end='')
    print('\n')
    thr = threading.Thread(target=f)
    thr.setDaemon(True)
    thr.start()
        

############################## 开始定义函数 ##############################


#################### ui兼容py ####################

def calMain(): #计算器主进程
    global main_run, gs_calculator, calOutputString
    gs_calculator = genshin_calculator()
    print('<sys> [loaded] genshin_calculator()')
    print('<sys> [checked] gs_calculator')
    print('<sys> [version] '+__version__)
    print('<sys> [control] calculator ready')
    print('计算器就绪')
    code = {'录入数据':'gs_calculator.character_input()','计算伤害':'gs_calculator.injury_calculator()',
            '查询记录':'gs_calculator.injury_read_data()','？':'gs_calculator.help.menu()',
            '?':'gs_calculator.help.menu()','录入圣遗物':'gs_calculator.ShengYiWu_input()'}
    def isUnableCode(enter_str):
        for i in ['auto_clear','ui.','sys.','time.','MainWindow.close']:
            if i in enter_str: return True
        return False
    while main_run[1]:
        while not main_run[0]: time.sleep(1)
        time.sleep(0.1)
        recordString = calOutputString
        enter_str = input('\n>>>')
        if enter_str == '':
            calOutputString = recordString
        else:
            if gs_calculator.auto_clear_command:
                send = Signal('MainWindow.calculatorAutoClear')
                time.sleep(0.1)
                print(enter_str)
            if 'install- ' in enter_str:
                install(enter_str.replace('install- ',''))
            elif enter_str in code:
                eval(code[enter_str])
            elif isUnableCode(enter_str):print("'%s'已禁用"%enter_str)
            else:
                try: eval('gs_calculator.'+enter_str+'()') 
                except:
                    try: eval('gs_calculator.'+enter_str)
                    except:
                        try: eval(enter_str)
                        except:
                            print('未知指令 \''+enter_str+'\'\n'+',输入\'help.menu\'以打开帮助菜单,输入\'help.help\'以打开所有帮助')

def input(prompt='',end=''): #替换了input函数，连接了输入台
    global inputString, main_run
    print(prompt,end='')
    while (inputString == None) and main_run[0]:
        time.sleep(0.1)
    if not main_run[0]:
        returnString = ''
    else:
        returnString = inputString
    inputString = None
    print(str(returnString))
    return returnString
def print(string,end='\n'): #替换了print函数
    global calOutputString, main_run
    if main_run[0]:
        calOutputString = calOutputString+string+end
        send = Signal('MainWindow.calOutputFlush')
def calInputFinished(): #检查是否输入完毕
    global inputString
    inputString = ui.calculatorInput.text()
    ui.calculatorInput.setText('')
def calSetInput(String): #连接按键和函数
    global inputString
    inputString = String
    ui.calculatorInput.setText('')

class Signal(QObject):
    signal1 = pyqtSignal()#声明无参数的信号
    def __init__(self,connect_func,parent=None):
        super(Signal,self).__init__(parent)
        self.signal1.connect(eval(connect_func))#将信号连接到打印函数
        self.signal1.emit() #发送信号

#sever control
def calStopSever():
    global main_run,calOutputString, calRunningStateString
    if main_run[0] == True:
        print('\n\n<sys> [control] sever stopped\n服务暂停')
        main_run[0] = False
        calRunningStateString = '等待启动'
        send = Signal('MainWindow.calRunningStateLabelFlush')
        send = Signal('MainWindow.setAllEnabledFalse')

def calStartSever():
    global main_run,calOutputString, calRunningStateString, inputString
    if main_run[0] == False:
        inputString = None
        main_run[0] = True
        print('<sys> [control] sever restarted\n服务重启')
        calRunningStateString = '正在运行'
        send = Signal('MainWindow.setAllEnabledTrue')
        send = Signal('MainWindow.calRunningStateLabelFlush')
        send = Signal('MainWindow.tipsLabelFlush')

def calBreakSever():
    global main_run
    def f():
        global calOutputString, calRunningStateString
        print('\n\n<sys> [control] sever breaked\n服务中断')
        main_run[0] = False
        calRunningStateString = '服务中断'
        send = Signal('MainWindow.calRunningStateLabelFlush')
        time.sleep(0.5)
        main_run[0] = True
        calRunningStateString = '正在运行'
        send = Signal('MainWindow.calRunningStateLabelFlush')
    if main_run[0] == True:
        threading.Thread(target=f).start()
    else: ui.calculatorStopSeverButton.setChecked(True)
def calSetAutoClear(autoClear):
    pass


#################### ui美化类 ####################

def tipsUpdate():
    global tipsUpdateString, main_run
    tipsList = ['向着星辰与深渊！','原来你也……','使用指令栏以输入指令或内容',
                '今天清委托了吗?','tips有那么好看吗，哼','假发管用吗(?','好像没几条管用的(',
                '有问题请联系我们吖qwq']
    while main_run[1]:
        randList = []
        tipsLen = len(tipsList)
        for i in range(tipsLen):
            for k in range(tipsLen*2):
                r = np.random.randint(0,tipsLen)
                if r not in randList:
                    randList.append(r)
                    break
        for i in randList:
            time.sleep(5)
            if not main_run[0]:
                break
            tipsUpdateString = 'Tips：'+str(tipsList[i])
            send = Signal('MainWindow.tipsLabelFlush')


############################## 主窗口类 ##############################

class calMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(calMainWindow, self).__init__(parent)#(Qmainwindow
    def calOutputFlush(self): #calculator output (print
        global calOutputString
        ui.calculatorOutput.setPlainText(calOutputString)
        ui.calculatorOutput.verticalScrollBar().setValue(ui.calculatorOutput.verticalScrollBar().maximum())
    def tipsLabelFlush(self):
        global tipsUpdateString
        ui.tipsLabel.setText(tipsUpdateString)
    def calRunningStateLabelFlush(self):
        global calRunningStateString
        ui.calRunningStateLabel.setText(calRunningStateString)
        if calRunningStateString == '正在运行':
            ui.calculatorRunSeverButton.setChecked(True)
        ui.calRunningStateLabel.setStyleSheet('QLineEdit{border: 1px solid #c8c8c8;border-radius:5px;font: 10pt "Adobe 宋体 Std R";'+
                                              'background-color: rgb%s;}'%str({'正在运行':(245,250,255),'等待启动':(255, 245, 245),
                                                                               '服务中断':(255, 255, 245),'正在更新':(255, 255, 245)}[calRunningStateString]))
    def calculatorClear(self): #清空输出台
        if main_run[0] == True:
            global calOutputString
            calOutputString = '>>>'
            ui.calculatorOutput.setPlainText('输出已清空\n>>>')
    def calculatorAutoClear(self):
        global calOutputString
        calOutputString = '>>>'
    def closeEvent(self,event):
        global main_run
        main_run = [False,False]
        sys.stdout.write('closed')
        event.accept()
    def setAllEnabledFalse(self):
        ui.calculatorBox.setEnabled(False)
        ui.calculatorBreakSeverButton.setEnabled(False)
        ui.tipsLabel.setText('Tips：遇到困难睡大觉zzZ')
    def setAllEnabledTrue(self):
        ui.calculatorBox.setEnabled(True)
        ui.calculatorBreakSeverButton.setEnabled(True)

############################## 初始化与主进程 ##############################

inputString = None #初始化输入台
calOutputString = '' #初始化输出台
tipsUpdateString = 'Tips: 寻找Tips...'
main_run = [True,True]

app = QApplication(sys.argv)
ui = calculator_ui.Ui_MainWindow()
MainWindow = calMainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowIcon(QIcon("icon.ico"))
calRunningStateString = '正在运行'
send = Signal('MainWindow.calRunningStateLabelFlush')

#if __name__ == '__main__':

def main():
    MainWindow.show()
    calMainThread = threading.Thread(target=calMain)
    tipsUpdateThread = threading.Thread(target=tipsUpdate)
    calMainThread.start()
    tipsUpdateThread.start()
    #connect
    ui.calculatorClearButton.clicked.connect(MainWindow.calculatorClear)#clear
    ui.calculatorAutoClearCheckBox.stateChanged.connect(lambda: gs_calculator.auto_clear(ui.calculatorAutoClearCheckBox.isChecked()))
    ui.calculatorRunSeverButton.clicked.connect(calStartSever)#SeverControl
    ui.calculatorBreakSeverButton.clicked.connect(calBreakSever)
    ui.calculatorStopSeverButton.clicked.connect(calStopSever)
    ui.calculatorQuitSeverButton.clicked.connect(MainWindow.close)
    ui.checkUpdateButton.clicked.connect(checkUpdate)
    ui.calculatorHistoryButton.clicked.connect(lambda String:calSetInput('查询记录'))#tools
    ui.calculatorCharacterInputButton.clicked.connect(lambda String:calSetInput('录入数据'))
    ui.calculatorInjButton.clicked.connect(lambda String:calSetInput('计算伤害'))
    ui.calculatorShengYiWuInputButton.clicked.connect(lambda String:calSetInput('录入圣遗物'))
    ui.calculatorInput.editingFinished.connect(calInputFinished)
    #version
    ui.versionLabel.setText(__version__)

    sys.exit(app.exec_())
