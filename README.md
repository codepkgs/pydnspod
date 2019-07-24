# 说明
* 操作dnspod域名(https://www.dnspod.cn)
* 支持对用户、域名以及记录相关的操作。实现了官方95%以上的功能，覆盖了所有常用功能。

# 安装
```
1. 安装requests
pip install requests

2. 安装dns-dnspod
pip install dns-dnspod

3. 使用
import pydnspod

user_id = 'your-user-id'
user_token = 'your-user-token'

创建连接:
dp = pydnspod.connect(user_id, user_token)

获取api版本:
dp.api_version()

操作用户: dp.user.*
dp.user.detail()            # 获取用户的详细信息
dp.user.modify_email()      # 修改用户的邮箱
dp.user.modify_password()   # 修改用户的密码
dp.user.modify_userinfo()   # 修改用户个人信息
dp.user.user_log()          # 获取用户登录日志

操作域名: dp.domain.*
dp.domain.add()             # 添加domain
dp.domain.remove()          # 删除domain
dp.domain.list()            # 列出domain
dp.domain.info()            # domain信息
dp.domain.log()             # domain操作日志
dp.domain.mark()            # domain设置星标
dp.domain.purview()         # 域名权限
dp.domain.remark()          # 域名备注
dp.domain.group_add()       # 添加分组
dp.domain.group_list()      # 列出分组
dp.domain.group_remove()    # 删除分组
dp.domain.group_modify()    # 修改分组
dp.domain.record_line()     # 获取域名支持的线路类型
dp.domain.record_type()     # 获取域名支持的记录类型

操作记录: dp.record.*
pd.record.add()             # 添加record
pd.record.info()            # 查看record信息
pd.record.list()            # 查询符合条件的record
pd.record.remove()          # 删除record
pd.record.remark()          # 给record设置备注
pd.record.modify()          # 修改record
pd.record.modify_status()   # 修改record的状态。启用或禁用
pd.record.record_id()       # 获取符合条件的子域名的record id
pd.record.status()          # 获取启用或禁用的records。
```