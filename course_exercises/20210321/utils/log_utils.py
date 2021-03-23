from config_utils import ConfigUtils
import logging
conf = ConfigUtils()
log_path = conf.get_log_path()
class LogUtils:
    def __init__(self,log_path):
        self.log_path = log_pathlogger
        logger= logging.getLogger('python实战日志')
        #设置日志级别 :  DEBUG<INFO<WARNING<ERROR<CRITICAL
        logger.setLevel(level=logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        # 将日志写入文件中
        logger.addHandler(file_log)

    def set_log_leve(self):
        self.logger.setLevel(level=logging.info())

    def set_log_format(self):
        self.logger
