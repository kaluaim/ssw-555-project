from datetime import datetime

def check_family_dates(_families):
    for k, v in _families.items():
        if not is_date_before_current(v.married):
            return False
        if v.divorced != 'N/A':
            if not is_date_before_current(v.divorced):
                return False
    return True

def check_individual_dates(_individuals):
    for k, v in _individuals.items():
        if not is_date_before_current(v.birthday):
            return False
        if v.death != 'N/A':
            if not is_date_before_current(v.death):
                return False
    return True

def is_date_before_current(_date_string):
    _date = datetime.strptime(_date_string, '%d %b %Y')
    return _date < datetime.now()
