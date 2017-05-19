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
 login_host=dict(default='localhost') # redis server IP address
 login_port=dict(default=6379, type='int') # redis server login port
 db=dict(default=None, type='int') # redis database number to connect
 command=dict(default=None, choices=['set', 'get', 'hmset', 'hmget']) # supported commands in this module
 key=dict(default=None) # set/get command key
 value=dict(default=None) # set command value
 hashkey=dict(default=None) # hmset/hmget command key
 hashfield=dict(default=None, type='list') # hmget command fields (a list)
 hashvalue=dict(default=None, type='dict') # hmset command fields and values (a dictionary)
```

Examples:

Redis 'set' command:
```python
    - hosts: local
      tasks:
        - name: Update mac:ip pair to redis after facts been gathered for linux group of hosts.
          anchor_redis: # use anchor_redis.py module.
            db: 0 # redis db param
            command: set # redis command param is 'set'
            key: "{{hostvars[item]['ansible_default_ipv4']['macaddress']}}" # key param for set cmd
            value: "{{hostvars[item]['ansible_default_ipv4']['address']}}" # value param for set cmd
          with_items:
            - "{{groups['linux']}}"
          when:
            - hostvars[item]['ansible_default_ipv4'] is defined
```
       
        
