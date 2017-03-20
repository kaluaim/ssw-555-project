from datetime import datetime

def check_family_dates_before_current(_families):
    for k, v in _families.items():
        if v.married != 'N/A':
            if not is_date_before_current(v.married):
                print('ERROR: FAMILY: US01: ' + v.famid + ': Marriage ' +
                    v.married + ' occurs in the future')
        if v.divorced != 'N/A':
            if not is_date_before_current(v.divorced):
                print('ERROR: FAMILY: US01: ' + v.famid + ': Divorce ' +
                    v.divorced + ' occurs in the future')
    return True

def check_individual_dates_before_current(_individuals):
    for k, v in _individuals.items():
        if v.birthday != 'N/A':
            if not is_date_before_current(v.birthday):
                print('ERROR: INDIVIDUAL: US01: ' + v.indiid + ': Birthday ' +
                    v.birthday + ' occurs in the future')
        if v.death != 'N/A':
            if not is_date_before_current(v.death):
                print('ERROR: INDIVIDUAL: US01: ' + v.indiid + ': Death ' +
                    v.death + ' occurs in the future')
    return True

def check_individual_age_less_than_150(_individuals):
    for k, v in _individuals.items():
        birth_date = datetime.strptime(v.birthday, '%d %b %Y')
        death_date = datetime.now()
        if v.death != 'N/A':
            death_date = datetime.strptime(v.death, '%d %b %Y')
        _age = calculate_dates_range(birth_date, death_date)
        if _age > 150:
            print('ERROR: INDIVIDUAL: US07: ' + v.indiid +
                ': More than 150 years old - Birth date ' + v.birthday)
    return True

def check_family_male_last_names(_families, _individuals):
    for k, v in _families.items():
        family_last_name = _individuals[v.husbandid].name.split('/')[1]
        for i in v.children:
            if _individuals[i].gender == 'M' and _individuals[i].name.split('/')[1] != family_last_name:
                print('ERROR: INDIVIDUAL: US16: ' + _individuals[i].indiid +
                    ': has last name: ' + _individuals[i].name.split('/')[1] +
                    ' diffrent than the family last name: ' + family_last_name)
    return True

def check_gender_role(_families, _individuals):
    for k, v in _families.items():
        if _individuals[v.husbandid].gender != 'M':
            print('ERROR: FAMILY: US21: ' + v.famid + ': Husband gender is not M.')
        if _individuals[v.wifeid].gender != 'F':
            print('ERROR: FAMILY: US21: ' + v.famid + ': Wife gender is not F.')
    return True

def is_date_before_current(_date_string):
    _date = datetime.strptime(_date_string, '%d %b %Y')
    return _date < datetime.now()

def calculate_dates_range(_from, _to):
    '''Takes two dates and return the reange between the two dates as int'''
    return (abs((_from - _to).days))/365
