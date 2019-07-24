from pydnspod.domain import Domain
from pydnspod.record import Record
from pydnspod.user import User
from pydnspod.base import ApiVersion

__author__ = 'zhanghe'
__version__ = '1.0.0'

class Connection(object):
    def __init__(self, user_id, user_token):
        self.user_id = user_id
        self.user_token = user_token
        self.domain = Domain(user_id, user_token)
        self.user = User(user_id, user_token)
        self.record = Record(user_id, user_token)
        self.__api_version = ApiVersion(user_id, user_token)

    def api_version(self):
        return self.__api_version.api_version()


connect = Connection