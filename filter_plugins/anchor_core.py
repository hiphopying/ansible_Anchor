def arpscanToDict(results):
    result = dict()
    for i in range(len(results)):
        if results[i]['item'] != 'lo' and results[i]['stdout_lines'] != []:
            for line in results[i]['stdout_lines']:
                result[line.split()[0]] = line.split()[1]
    return result

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''
    def filters(self):
        return {
            'arpscanToDict': arpscanToDict
        }

