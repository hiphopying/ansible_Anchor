# ansible_Anchor

This repository includes libraries/playbooks/roles to do fact gathering, redis operations, configuration management.

## Playbooks:
### Playbook_findmac.yml
This playbook gather mac:ip mappings from running servers and write mac:ip as key:value pair to redis server.

## Module Libraries:
### anchor_redis.py
This module includes some redis operations for ansible user to interact with redis database.

Examples:

Redis 'set' command:
```
    - hosts: local
      tasks:
        - name: Update mac:ip pair to redis after facts been gathered for linux group of hosts.
          anchor_redis:
            db: 0 # redis db number
            command: set # redis command using set
            key: "{{hostvars[item]['ansible_default_ipv4']['macaddress']}}" 
            value: "{{hostvars[item]['ansible_default_ipv4']['address']}}"
          with_items:
            - "{{groups['linux']}}"
          when:
            - hostvars[item]['ansible_default_ipv4'] is defined
```
       
        
