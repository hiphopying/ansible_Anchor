def dictzip(lst1, lst2):
    return dict(zip(lst1,lst2))

def arpscanToDict(result1, result2):
    result = dict()
    for i in range(len(result1)):
        if result1[i]['item'] != 'lo' and result1[i]['stdout_lines'] != []:
            result.update(dictzip(result1[i]['stdout_lines'],
                              result2[i]['stdout_lines']))
    return result

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''
    def filters(self):
        return {
            'dictzip': dictzip,
            'arpscanToDict': arpscanToDict
        }

