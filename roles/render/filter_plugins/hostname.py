def hostname(ip):
    name_pattern = 'E2E-{}-{}'
    if ip.startswith('10.228'):
        lab_number = '02'
    elif ip.startswith('10.103'):
        lab_number = '04'
    else:
        lab_number = 'unknown'
    ending = ''.join(ip.split('.')[2:])
    return name_pattern.format(lab_number, ending)

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
