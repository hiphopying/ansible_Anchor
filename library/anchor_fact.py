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
module: anchor_fact
short_description: gather facts with additional info on the hosts.
description: 
    - The ansble setup module does not gather facts like HBA info, this module
    is developped for addtional facts.
author: henryy.xu@dell.com
options:
requirements:
notes:
'''

EXAMPLES = '''

'''
def filter_ansible_fact(ansible_facts):
    assert ansible_facts != None
    if ansible_facts['ansible_system'] == 'Linux':
        filtered_facts = dict()
        filtered_facts['architecture'] = \
                ansible_facts['ansible_architecture']
        filtered_facts['os_ip'] = \
                ansible_facts['ansible_default_ipv4']['address']
        filtered_facts['distribution'] = \
                ansible_facts['ansible_distribution']
        filtered_facts['distribution_version'] = \
                ansible_facts['ansible_distribution_version']
        filtered_facts['hostname'] = \
                ansible_facts['ansible_hostname']
        filtered_facts['processor'] = \
                ansible_facts['ansible_processor'][1]
        filtered_facts['memtotal_mb'] = \
                ansible_facts['ansible_memtotal_mb']
        filtered_facts['product_name'] = \
                ansible_facts['ansible_product_name']
        filtered_facts['product_serial'] = \
                ansible_facts['ansible_product_serial']
        filtered_facts['system'] = \
                ansible_facts['ansible_system']
        return filtered_facts
    else:
        return ansible_facts


def append_hba_info(filtered_facts):
    return filtered_facts

def append_additional_info(filtered_facts):
    pass
    return filtered_facts

def main():
    module = AnsibleModule(
        argument_spec = dict(
            ansible_facts = dict(default=None, type='dict', required=True)
        )
    )
    
    data = append_hba_info(filter_ansible_fact(module.params['ansible_facts']))
    module.exit_json(changed=False, value=data)

from ansible.module_utils.basic import *
from ansible.module_utils.pycompat24 import get_exception

if __name__ == '__main__':
     main()
