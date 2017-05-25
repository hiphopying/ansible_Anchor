def hostname(data):
    return "dummy_name"

def subnet(ip, vlan):
    prefix = '10.228.'
    if prefix+str(vlan) in ip:
        return True
    return False

class FilterModule(object):

    def filters(self):
        return {
            'hostname': hostname,
            'subnet': subnet,
        }
