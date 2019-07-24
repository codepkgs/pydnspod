from pydnspod.base import Api


class User(Api):
    """
    dnspod account information
    """

    def detail(self):
        """
        get user detail information
        :return:
        """
        uri = '/User.Detail'
        ret = self._do_request(uri)
        return ret.get('info').get('user')

    def modify_userinfo(self, lastname='', title='先生', real_name='', telephone=''):
        """
        modify user information
        :param lastname: your lastname, only one character
        :param title: your title, 先生" or "女士"
        :param real_name: your real_name
        :param telephone: your telephone
        :return: if modify success return True, else return False or throw Exception
        """
        payload = {}

        if lastname and len(lastname) != 1:
            raise ValueError('lastname length must be 1 char')

        if title and title not in ('先生', '女士'):
            raise ValueError('title muse be "先生" or "女士"')

        nick = '{} {}'.format(lastname, title)
        payload['nick'] = nick

        if real_name:
            payload['real_name'] = real_name

        if telephone:
            payload['telephone'] = telephone

        uri = '/User.Modify'
        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def modify_password(self, old_password, new_password):
        """
        modify user password, this function may be paused by dnspod
        :param old_password: old password
        :param new_password: new password
        :return: True or False or throw Exception
        """
        payload = {
            'old_password': old_password,
            'new_password': new_password
        }

        uri = '/Userpasswd.Modify'
        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def modify_email(self, old_email, new_email, password):
        """
        modify user email, this function may be paused by dnspod
        :param old_email: old email
        :param new_email: new email
        :param password: current login password
        :return:
        """
        payload = {
            'old_email': old_email,
            'new_email': new_email,
            'password': password
        }

        uri = '/Useremail.Modify'
        ret = self._do_request(uri, **payload)
        if ret.get('status', {}).get('code') == 1:
            return True
        else:
            return False

    def user_log(self):
        """
        get user operate logs
        :return: log list
        """
        uri = '/User.Log'
        ret = self._do_request(uri)
        return ret.get('log')
