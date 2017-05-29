# ansible_Anchor

This repository includes an ansible automation tool to scan server mac address in given network range, and render large number of host\' hostname based on pre-defined rules via DHCP.

**Fast scan speed**: It uses arpscan which finish scanning an given subnet with 200~300 hosts in few seconds 

**High discovery rate**: It collects server mac with high successfully rate, regardless of OS, login, firewall.

**Customization allowed**: Both user defined, and auto generated config files are allowed in DHCP for each host

## Architecture:
- ARPscan VM:

    A VM which has access to all the required subnets, and send ARP calls to scan and collect server mac
- Redis Database:

    Store all the IP:mac pairs collected from ARPscan VM
- Ansible server:

    Playbooks/roles/libraries to trigger ARP scan, store IP:mac pairs in redis, and render the information into DHCP auto-generated config file based on pre-defined rules
- DHCP server:

    It contains both user define config file and ansible-generated config files, and takes care of IP assignment, hostname update for all the servers

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
 command=dict(default=None, choices=['set', 'get', 'hmset', 'hmget']) # redis command to use
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
       
        
