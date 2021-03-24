from config_utils import ConfigUtils
import logging
conf = ConfigUtils()
log_path = conf.get_log_path()
class LogUtils:
    def __init__(self,logfile_path = log_path):
        self.logfile_path = logfile_path
        self.logger= logging.getLogger('python实战日志')
        #设置日志级别 :  DEBUG<INFO<WARNING<ERROR<CRITICAL
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(self.logfile_path,encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        # 将日志写入文件中
        self.logger.addHandler(file_log)  #写入文件

    def info(self,message):
        self.logger.info(message)
    def error(self,message):
        self.logger.info(message)

log_obj = LogUtils()

if __name__ == '__main__':
    log_obj.info('我是工具包日志')
    log_obj.error('我是工具包错误日志')