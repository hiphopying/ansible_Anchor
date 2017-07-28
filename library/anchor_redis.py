#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: anchor_redis
short_description: Includes various redis commands.
description: 
    - The official redis module only contains 'slave', 'flush', 'config'
    commands. 
    - This module contains much more commands like set/get/hmset/hmget etc to
    interact with redis server.
author: henryy.xu@dell.com
options:
requirements:[redis]
notes:
'''

EXAMPLES = '''

'''

REDIS_HOST = '10.228.104.198'
REDIS_PORT = '32768'
REDIS_DB = 0
REDIS_GET = ['get', 'hgetall',  'hmget']
REDIS_SET = ['set', 'hmset']
REDIS_ACTIONS = REDIS_GET + REDIS_SET

try:
    import redis
except ImportError:
    redis_found = False
else:
    redis_found = True

def anch_update(client, cmd, **kwargs):
    if cmd == "set":
        assert kwargs['key'] != None
        assert kwargs['value'] != None
        key = kwargs['key']
        value = kwargs['value']
        try:
            return client.set(key, value)
        except Exception:
            raise 
    elif cmd == "get":
        assert kwargs['key'] != None
        key = kwargs['key']
        try:
            return client.get(key)
        except Exception:
            raise
    elif cmd == "hgetall":
        assert kwargs['key'] != None
        key = kwargs['key']
        try:
            return client.hgetall(key)
        except Exception:
            raise
    elif cmd == "hkeys":
        assert kwargs['hashkey'] != None
        try:
            return client.hkeys()
        except Exception:
            raise
    elif cmd == "hmset":
        assert kwargs['hashkey'] != None
        assert kwargs['hashvalue'] != None
        hashkey = kwargs['hashkey']
        hashvalue = kwargs['hashvalue']
        try:
            return client.hmset(hashkey, hashvalue)
        except Exception:
            raise
    elif cmd == "hmget":
        assert kwargs['hashkey'] != None
        assert kwargs['hashfield'] != None
        hashkey = kwargs['hashkey']
        hashfield = kwargs['hashfield']
        try:
            return client.hmget(hashkey, hashfield)
        except Exception:
            raise



def main():
    module = AnsibleModule(
        argument_spec = dict(
            login_host=dict(default=REDIS_HOST),
            login_port=dict(default=REDIS_PORT, type='int'),
            db=dict(default=REDIS_DB, type='int'),
            command=dict(default=None, choices=REDIS_ACTIONS),
            key=dict(default=None),
            value=dict(default=None),
            hashkey=dict(default=None),
            hashfield=dict(default=None, type='list'),
            hashvalue=dict(default=None, type='dict')
        ),
        supports_check_mode = True
    )

    if not redis_found:
        module.fail_json(msg="python redis module is required")

    login_host = module.params['login_host']
    login_port = module.params['login_port']
    db = module.params['db']
    try:
        r = redis.StrictRedis(host=login_host, port=login_port, db=db)
        r.ping()
    except Exception:
       e = get_exception()
       module.fail_json(msg="Unable to connect to database {0}".format(e))

    command = module.params['command']
    key = module.params['key']
    value = module.params['value']
    hashkey = module.params['hashkey']
    hashfield = module.params['hashfield']
    hashvalue = module.params['hashvalue']
    
    result = anch_update(r, command, key=key, value=value, hashkey=hashkey,
                   hashfield=hashfield, hashvalue=hashvalue)
    if result and command in REDIS_GET:
        module.exit_json(changed=False, values=result)
    else:
        module.exit_json(changed=True)

from ansible.module_utils.basic import *
from ansible.module_utils.pycompat24 import get_exception

if __name__ == '__main__':
     main()
