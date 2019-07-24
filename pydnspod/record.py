from pydnspod.base import Api


class Record(Api):
    """
    manage domain records
    """

    def add(self, domain, sub_domain, record_type, value, ttl=600,
            record_line='默认', enable=True, mx='', weight=''):
        """
        create record
        :param domain: parent domain id or domain name
        :param sub_domain: sub_domain, example: www
        :param record_type: record type, example: A
        :param value: record value
        :param ttl: record ttl, default is: 600
        :param record_line: record line, example: 移动，联通
        :param enable: True is enable this record, False is disable this record
        :param mx: mx value, 1-20
        :param weight: only for company vip domain.
        :return: record info
        """

        uri = '/Record.Create'
        status = 'enable' if enable else 'disable'
        record_type = str(record_type).upper()
        payload = self._switch_payload(domain)
        payload.update(
            sub_domain=sub_domain,
            record_type=record_type,
            value=value,
            ttl=ttl,
            record_line=record_line,
            enable=status,
            mx=mx,
            weight=weight
        )

        ret = self._do_request(uri, **payload)
        return ret.get('record')

    def list(self, domain, sub_domain='', record_type='', record_line='',
             offset=None, length=None, keyword=''):
        """
        get record list
        :param domain: domain id or domain name
        :param sub_domain: sub_domain, example: www
        :param record_type: record_type, example: A
        :param record_line: record line, example: 默认
        :param offset: record offset, the first record is 0
        :param length: get record counts, max 3000.
        :param keyword: search record
        :return:
        """

        uri = '/Record.List'
        payload = self._switch_payload(domain)

        if sub_domain:
            payload.update(sub_domain=sub_domain)

        if record_type:
            payload.update(record_type=str(record_type).upper())

        if record_line:
            payload.update(record_line=record_line)

        if offset:
            payload.update(offset=offset)

        if length:
            payload.update(length=length)

        if keyword:
            payload.update(keyword=keyword)

        ret = self._do_request(uri, **payload)
        return {
            'domain': ret.get('domain'),
            'info': ret.get('info'),
            'records': ret.get('records')
        }

    def record_id(self, domain, sub_domain):
        """
        get record id about sub domain
        :param domain:
        :param sub_domain:
        :return: record id list
        """
        uri = '/Record.List'
        payload = self._switch_payload(domain)
        payload.update(sub_domain=sub_domain)

        ret = self._do_request(uri, **payload)
        data = []
        for r in ret.get('records'):
            data.append(r['id'])

        return data

    def modify(self, domain, record_id, sub_domain, record_type, value, ttl=600,
               record_line='默认', enable=True, mx='', weight=''):
        """
        modify record
        :param domain: domain id or domain name
        :param record_id: record id
        :param sub_domain: sub_domain, example: www
        :param record_type: record type, example: A
        :param value: record value
        :param ttl: ttl
        :param record_line: record line, example: 默认
        :param enable: enable or disable this record
        :param mx: mx value, 1-20
        :param weight: only for company vip domain, 0-100
        :return:
        """
        uri = '/Record.Modify'
        status = 'enable' if enable else 'disable'
        record_type = str(record_type).upper()
        payload = self._switch_payload(domain)
        payload.update(
            record_id=record_id,
            sub_domain=sub_domain,
            record_type=record_type,
            value=value,
            ttl=ttl,
            record_line=record_line,
            enable=status,
            mx=mx,
            weight=weight
        )

        ret = self._do_request(uri, **payload)
        return ret.get('record')

    def remove(self, domain, record_id):
        """
        delete recode
        :param domain: domain id or domain name
        :param record_id: record id
        :return: True or False
        """

        uri = '/Record.Remove'
        payload = self._switch_payload(domain)
        payload.update(record_id=record_id)

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def remark(self, domain, record_id, content):
        """
        set record remark
        :param domain: domain id or domain name
        :param record_id: record id
        :param content: remark content
        :return: True or False
        """

        uri = '/Record.Remark'
        payload = self._switch_payload(domain)
        payload.update(record_id=record_id, remark=content)
        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def info(self, domain, record_id):
        """
        get record info
        :param domain: domain id or domain name
        :param record_id: record id
        :return:
        """

        uri = '/Record.Info'
        payload = self._switch_payload(domain)
        payload.update(record_id=record_id)

        ret = self._do_request(uri, **payload)
        return ret.get('record')

    def modify_status(self, domain, record_id, enable=True):
        """
        modify record status
        :param domain: domain id or domain name
        :param record_id: record id
        :param enable: True is enable, False is disable
        :return:
        """

        uri = '/Record.Status'
        payload = self._switch_payload(domain)
        status = 'enable' if enable else 'disable'
        payload.update(
            record_id=record_id,
            status=status
        )

        ret = self._do_request(uri, **payload)
        return True if ret.get('status', {}).get('code') == '1' else False

    def status(self, domain, enable=True):
        """
        get all records of the special status
        :param domain: domain id or domain name
        :param enable: True status is enable, False statu is disable
        :return:
        """

        uri = '/Record.List'
        payload = self._switch_payload(domain)

        if enable:
            status = 1
        else:
            status = 0

        ret = self._do_request(uri, **payload)
        records = ret.get('records')
        data = [r for r in records if int(r.get('enabled')) == status]
        return {
            'total': len(data),
            'records': data
        }

