import requests


class DnspodApiException(Exception):
    pass


class Api(object):
    """
    dnspod base class
    """

    def __init__(self, user_id, user_token):
        """
        :param user_id: api token id
        :param user_token: api token
        """

        self.__login_token = '{},{}'.format(user_id, user_token)
        self.__user_agent = 'dns-dnspod client/1.0.0 (x_hezhang@126.com)'
        self.__base_url = 'https://dnsapi.cn'
        self.__headers = {'User-Agent': self.__user_agent}

    def _do_request(self, uri='', **kwargs):
        """
        send request
        :param uri: request uri
        :param kwargs: fill payload
        :return: dict
        """

        payload = {
            'login_token': self.__login_token,
            'format': 'json',
            'lang': 'cn',
            'error_on_empty': 'no'
        }

        payload.update(kwargs)

        if uri.startswith('/'):
            self.__api = self.__base_url + uri
        else:
            self.__api = self.__base_url + '/' + uri

        try:
            response = requests.post(self.__api, data=payload, headers=self.__headers)
            ret = response.json()
            if ret.get('status', {}).get('code') == '1':
                return ret
            else:
                raise DnspodApiException(ret)
        except Exception:
            raise

    def _switch_payload(self, domain):
        """
        padding domain_name or domain_id in payload
        :param domain: domain_name or domain_id
        :return: payload
        """

        if isinstance(domain, int):
            payload = {'domain_id': domain}
        elif isinstance(domain, str):
            if domain.isdigit():
                payload = {'domain_id': domain}
            else:
                payload = {'domain': domain}
        else:
            raise TypeError('domain muse be int or str')

        return payload


class ApiVersion(Api):
    def api_version(self):
        ret = self._do_request('/Info.Version')
        return ret.get('status').get('message')
