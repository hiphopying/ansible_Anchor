# ansible_Anchor

This repository includes libraries/playbooks/roles to do fact gathering, redis operations, configuration management.

## Playbooks:
### Playbook_findmac.yml
This playbook gather mac:ip mappings from running servers and write mac:ip as key:value pair to redis server.

## Module Libraries:
### anchor_redis.py
This module includes some redis operations for ansible user to interact with redis database.

Parameters:
```python
 login_host=dict(default='localhost')
 login_port=dict(default=6379, type='int')
 db=dict(default=None, type='int')
 command=dict(default=None, choices=['set', 'get', 'hmset', 'hmget'])
 key=dict(default=None)
 value=dict(default=None)
 hashkey=dict(default=None)
 hashfield=dict(default=None, type='list')
 hashvalue=dict(default=None, type='dict')
```

Examples:

Redis 'set' command:
```python
    - hosts: local
      tasks:
        - name: Update mac:ip pair to redis after facts been gathered for linux group of hosts.
          anchor_redis:
            db: 0 # redis db number
            command: set # redis command using set
            key: "{{hostvars[item]['ansible_default_ipv4']['macaddress']}}" # key param for set cmd
            value: "{{hostvars[item]['ansible_default_ipv4']['address']}}" # value param for set cmd
          with_items:
            - "{{groups['linux']}}"
          when:
            - hostvars[item]['ansible_default_ipv4'] is defined
```
       
        
