#读取配置文件工具包
import os
import configparser
current_path = os.path.dirname(__file__)
conf_path = os.path.join(current_path,'../conf/config.ini')
class ConfigUtils:
    def __init__(self,config_path = conf_path):
        self.config_path = config_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_path,encoding='utf-8')

    def get_excel_path(self):
        return self.conf.get('default','excel_path')
    def get_config_path(self):
        return self.conf.get('default','config_path')
    def get_log_path(self):
        return self.conf.get('default','log_path')

config = ConfigUtils()

if __name__ == '__main__':
    print(config.get_excel_path())
    print(config.get_config_path())
    print(config.get_log_path())