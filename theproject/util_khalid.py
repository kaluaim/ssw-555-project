from datetime import datetime

def check_family_dates_before_current(_families):
    print('\nChecking families dates before current date...')
    for k, v in _families.items():
        print('Checking: ' + v.famid)
        if v.married != 'N/A':
            if not is_date_before_current(v.married):
                print('-- [Error]: married after current!')
                return False
            else:
                print('-- [OK]: Married before current date')
        if v.divorced != 'N/A':
            if not is_date_before_current(v.divorced):
                print('-- [Error]: divorced after current!')
                return False
            else:
                print('-- [OK]: Divorced before current date')
    return True

def check_individual_dates_before_current(_individuals):
    print('\nChecking individuals dates before current date...')
    for k, v in _individuals.items():
        print('Checking: ' + v.name)
        if v.birthday != 'N/A':
            if not is_date_before_current(v.birthday):
                print('-- [Error]: birthday after current!')
                return False
            else:
                print('-- [OK]: Birthday before current date')
        if v.death != 'N/A':
            if not is_date_before_current(v.death):
                print('-- [Error]: death date after current!')
                return False
            else:
                print('-- [OK]: Death before current date')
    return True

def check_individual_age_less_than_150(_individuals):
    print('\nChecking individuals age less than 150...')
    for k, v in _individuals.items():
        birth_date = datetime.strptime(v.birthday, '%d %b %Y')
        death_date = datetime.now()
        if v.death != 'N/A':
            death_date = datetime.strptime(v.death, '%d %b %Y')
        _age = calculate_dates_range(birth_date, death_date)
        if _age > 150:
            print('[Error]: ' + v.name + ' is ' + str(_age) )
        else:
            print('[OK]: ' + v.name + ' is ' + str(_age))

    return True

def is_date_before_current(_date_string):
    _date = datetime.strptime(_date_string, '%d %b %Y')
    return _date < datetime.now()

def calculate_dates_range(_from, _to):
    '''Takes two dates and return the reange between the two dates as int'''
    return (abs((_from - _to).days))/365
