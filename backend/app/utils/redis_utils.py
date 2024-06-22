import redis
from app.conf import config
import pickle


class Redis(object):
    """
    redis資料庫操作
    """

    @staticmethod
    def _get_r():
        host = config.REDIS["HOST"]
        port = config.REDIS["PORT"]
        db = config.REDIS["DB"]
        passwd = config.REDIS["PASSWD"]
        r = redis.StrictRedis(host=host, port=port, db=db, password=passwd)
        return r

    @classmethod
    def write_dict(self, key, value, expire=None):
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = config.REDIS["EXPIRE"]
        r = self._get_r()
        r.set(key, pickle.dumps(value), ex=expire_in_seconds)

    @classmethod
    def read_dict(self, key):
        r = self._get_r()
        data = r.get(key)
        if data is None:
            return None
        return pickle.loads(data)

    @classmethod
    def delete(self, *names):

        r = self._get_r()
        r.delete(*names)

    @classmethod
    def expire(self, name, expire=None):

        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = config.REDIS["EXPIRE"]
        r = self._get_r()
        r.expire(name, expire_in_seconds)
