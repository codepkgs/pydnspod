# coding: utf-8
import requests


class DnspodApiException(Exception):
    pass


class Dnspod(object):
    """
    dnspod base class
    """

    def __init__(self, user_id, user_token):
        """
        :param user_id: api token id
        :param user_token: api token
        """

        self.login_token = '{},{}'.format(user_id, user_token)
        self.user_agent = 'dns-dnspod client/1.0.0 (x_hezhang@126.com)'
        self.base_url = 'https://dnsapi.cn'
        self.__headers = {'User-Agent': self.user_agent}
        self.payload = {
            'login_token': self.login_token,
            'format': 'json',
            'lang': 'en',
            'error_on_empty': 'no'
        }

    def _do_request(self, uri=''):
        if uri.startswith('/'):
            self.api = self.base_url + uri
        else:
            self.api = self.base_url + '/' + uri

        try:
            response = requests.post(self.api, data=self.payload, headers=self.__headers)
            ret = response.json()
            if ret.get('status', {}).get('code') == '1':
                return ret
            else:
                raise DnspodApiException(ret)
        except Exception:
            raise

    def api_version(self):
        ret = self._do_request('/Info.Version')
        return ret.get('status').get('message')
