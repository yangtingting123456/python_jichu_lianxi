from config_utils import ConfigUtils
import logging
conf = ConfigUtils()
log_path = conf.get_log_path()
class LogUtils:
    def __init__(self,log_path):
        self.log_path = log_path
        self.logger = logging.getLogger()

    def set_log
