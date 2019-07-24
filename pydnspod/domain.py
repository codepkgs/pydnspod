from pydnspod.base import Api


class Domain(Api):
    """
    operate domains
    """

    def list(self):
        """
        get all domains
        :return:
        """

        uri = '/Domain.List'
        ret = self._do_request(uri)
        data = {
            'info': ret.get('info'),
            'domains': ret.get('domains')
        }
        return data

    def info(self, domain):
        """
        get domain info
        :param domain: domain_id or domain_name
        :return: domain info
        """

        payload = self._switch_payload(domain)
        uri = '/Domain.Info'
        ret = self._do_request(uri, **payload)
        return ret.get('domain')

    def log(self, domain, offset=0, length=500):
        """
        get domain operate log
        :param domain: domain_name or domain_id
        :param offset: log offset
        :param length: logs number
        :return:
        """
        uri = '/Domain.Log'
        payload = self._switch_payload(domain)
        payload.update(offset=offset, length=length)
        ret = self._do_request(uri, **payload)
        return ret.get('log')

    def add(self, domain, group_id='', is_mark=False):
        """
        add domain
        :param domain: domain name, no www
        :param group_id: domain group id, group must bu exist
        :param is_mark: True or False
        :return: domain info
        """

        payload = {'domain': domain}
        uri = '/Domain.Create'

        if group_id:
            try:
                group_id = int(group_id)
            except ValueError:
                raise ValueError('invalid group id')
            else:
                payload['group_id'] = group_id

        if is_mark:
            payload['is_mark'] = 'yes'
        else:
            payload['is_mark'] = 'no'

        ret = self._do_request(uri, **payload)
        return ret.get('domain')

    def remove(self, domain):
        """
        remove domain
        :param domain: domain_id or domain_name
        :return: True or False or throw Exception
        """

        payload = self._switch_payload(domain)

        uri = '/Domain.Remove'
        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def modify_status(self, domain, is_enabled=True):
        """
        modify domain status
        :param domain: domain_id or domain_name
        :param is_enabled: True enable, False disable
        :return: True or False
        """

        payload = self._switch_payload(domain)
        uri = '/Domain.Status'

        if is_enabled:
            payload.update(status='enable')
        else:
            payload.update(status='disable')

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def group_list(self):
        """
        get domain group list
        :return: groups
        """
        uri = '/Domaingroup.List'
        ret = self._do_request(uri)
        return ret.get('groups')

    def group_add(self, group_name):
        """
        create group
        only supper vip account
        :param group_name: group name
        :return: group id
        """

        payload = {}
        if group_name:
            payload['group_name'] = group_name
        else:
            raise ValueError('invalid group name')

        uri = '/Domaingroup.Create'
        ret = self._do_request(uri, **payload)
        return ret.get('groups', {}).get('id')

    def group_modify(self, group_id, group_name):
        """
        modify group name
        :param group_id: group id
        :param group_name: modified group_name
        :return: True or False
        """
        uri = '/Domaingroup.Modify'
        payload = {
            'group_id': group_id,
            'group_name': group_name
        }
        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def group_remove(self, group_id):
        """
        delete group
        :param group_id: group id you want to delete
        :return: True or False
        """

        uri = '/Domaingroup.Remove'
        payload = {
            'group_id': group_id
        }

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def change_group(self, domain, group_id):
        """
        change domain group
        :param domain: domain id or domain_name
        :param group_id: changed group_id
        :return: True or False
        """

        uri = '/Domain.Changegroup'
        payload = self._switch_payload(domain)
        payload.update(group_id=group_id)

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def mark(self, domain, is_mark=False):
        """
        mark domain
        :param domain: domain name or domain_id
        :param is_mark: True is marked, False is not marked
        :return:
        """
        uri = '/Domain.Ismark'
        payload = self._switch_payload(domain)
        if is_mark:
            payload.update(is_mark='yes')
        else:
            payload.update(is_mark='no')
        print(payload)

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def remark(self, domain, content):
        """
        set domain remark. if want to delete remark, set content to empty
        :param domain: domain name or domain id
        :param content: remark content
        :return: True or False
        """

        uri = '/Domain.Remark'
        payload = self._switch_payload(domain)
        payload.update(remark=content)

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def purview(self, domain):
        """
        get domain purview
        :param domain: domain id or domain name
        :return: purview list
        """
        uri = '/Domain.Purview'
        payload = self._switch_payload(domain)

        ret = self._do_request(uri, **payload)
        return ret.get('purview')

    def record_type(self, domain_grade):
        """
        get the domain grade allowd records type
        :param domain_grade: domain_grade
        :return: record types
        """

        uri = '/Record.Type'
        payload = {
            'domain_grade': domain_grade
        }

        ret = self._do_request(uri, **payload)
        return ret.get('types')

    def record_line(self, domain, domain_grade):
        """
        get domain grade allowed line
        :param domain: domain id or domain name
        :param domain_grade: domain grade
        :return: dict
        """

        uri = '/Record.Line'
        payload = self._switch_payload(domain)
        payload.update(domain_grade=domain_grade)

        ret = self._do_request(uri, **payload)
        return {
            'line_ids': ret.get('line_ids'),
            'lines': ret.get('lines')
        }
