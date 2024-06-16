import logging
import os

# 日誌檔案名稱
log_filename = 'example.log'

# 如果日誌檔案存在，則清空檔案
if os.path.exists(log_filename):
    with open(log_filename, 'w', encoding='utf-8') as f:
        f.truncate(0)

# 設定 logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 獲取 logger
logger = logging.getLogger(__name__)
