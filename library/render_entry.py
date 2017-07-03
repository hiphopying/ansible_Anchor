##!/usr/bin/python
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

'''

EXAMPLES = '''

'''

REDIS_HOST = '10.228.104.198'
REDIS_PORT = '32782'
REDIS_DB = 0

try:
    import redis
except ImportError:
    redis_found = False
else:
    redis_found = True

def main():
    module = AnsibleModule(
        argument_spec = dict(
            login_host=dict(default=REDIS_HOST),
            login_port=dict(default=REDIS_PORT, type='int'),
            db=dict(default=REDIS_DB, type='int'),
            inventory=dict(default=None, type='list')
        ),
        supports_check_mode = True
    )

    if not redis_found:
        module.fail_json(msg="python redis module is required")

    login_host = module.params['login_host']
    login_port = module.params['login_port']
    db = module.params['db']
    inventory = module.params['inventory']
    
    try:
        r = redis.StrictRedis(host=login_host, port=login_port, db=db)
        r.ping()
    except Exception:
        e = get_exception()
        module.fail_json(msg="Unable to connect to database {0}".format(e))

    result = dict()
    for ip in inventory:
        mac = r.hmget("dhcpipmac", ip)[0] 
        if r.hmget("dhcpmacip", mac)[0] == ip:
            result[ip] = mac

    if result:
        module.exit_json(changed=False, values=result)
    else:
        module.exit_json(changed=False)

from ansible.module_utils.basic import *
from ansible.module_utils.pycompat24 import get_exception

if __name__ == '__main__':
     main()
