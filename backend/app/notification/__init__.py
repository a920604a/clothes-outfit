import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)