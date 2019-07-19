
from pydnspod.dnspod import


class User(Dnspod):
    """
    dnspod account information
    """
    
    def __init__(self, login_token):
        super(User, self).__init__(login_token)

    def detail(self):
        self.uri = '/User.Detail'
        ret = self._do_request(self.uri)
        return ret


if __name__ == '__main__':
    login_token = '108196,e494731ad1b1672fecb4866d8bd968eb'
    user = User(login_token)
    print(user.detail())
