# 父类：文件
# 子类：txt文件---双击 开开txt文档
#     exe程序  --双击 安装软件
#     MP4视频 --双击  播放视频

from  abc import abstractmethod,ABCMeta
class Double_File(metaclass=ABCMeta): #抽象父类
    @abstractmethod
    def double_click(self):
        pass
#实现多态
class Double_Txt(Double_File):
    def double_click(self):
        print('双击txt文件,打开txt文件')

class Double_exe(Double_File):
    def double_click(self):
        print('双击exe文件,安装文件')

class Double_Mp4(Double_File):
    def double_click(self):
        print('双击mp4文件,视频播放')

#传入不同的文件类型，实现多态性
def double_click(file_obj):
    file_obj.double_click()

#调用实现多态性
txt = Double_Txt()
double_click(txt)

exe = Double_exe()
double_click(exe)

mp4 = Double_Mp4()
double_click(mp4)