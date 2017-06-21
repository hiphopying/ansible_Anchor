def arpscanToDict(results):
    result = []
    for i in results:
        if i['item'] != 'lo' and i['stdout_lines']:
            for line in i['stdout_lines']:
                result.append(line.split())
    return dict(result)

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''
    def filters(self):
        return {
            'arpscanToDict': arpscanToDict
        }

