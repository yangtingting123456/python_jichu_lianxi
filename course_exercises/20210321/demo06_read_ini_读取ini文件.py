import configparser
import os
#读取ini配置文件
current_path = os.path.dirname(__file__)
conf_path = os.path.join(current_path,'conf/config.ini')
conf = configparser.ConfigParser()  #创建conf对象
conf.read(conf_path,encoding='utf-8')
print('获取全部的组名：',conf.sections())
print('获取某个组中的内容：',conf.items('default'))
print('获取某个组中对应的值：',conf.get('default','excel_path'))
print('获取某个组下所有的key：',conf.options('default'))