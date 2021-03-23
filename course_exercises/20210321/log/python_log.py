#日志模块
import os,logging
#创建日志对象
logger = logging.getLogger('python实战日志')
#设置日志级别 :  DEBUG<INFO<WARNING<ERROR<CRITICAL
logger.setLevel(level=logging.INFO)
# 1.在控制台打印日志
console = logging.StreamHandler()  #创建控制台输出对象
#设置日志输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s')
console.setFormatter(formatter)  #设置日志输出格式
console.setLevel(level=logging.ERROR)
logger.addHandler(console)  #设置日志在控制台打出
logger.error('this is error log')

# 2.将日志写入在日志文件中
log_path = os.path.join(os.path.dirname(__file__),'python.log')
file_log = logging.FileHandler(log_path,encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s')
file_log.setFormatter(formatter)
#将日志写入文件中
logger.addHandler(file_log)
logger.info('人生')
logger.error('error')
logger.debug('debug')
logger.warning('warning')


