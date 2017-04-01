from datetime import datetime, timedelta
import gedcom

def US12():
    for k, v in gedcom.FAMs.items():
        if gedcom.INDIs[v.husbandid].birthday != 'N/A' and gedcom.INDIs[v.wifeid] != 'N/A':
            bd_father = datetime.strptime(gedcom.INDIs[v.husbandid].birthday, '%d %b %Y')
            bd_mother = datetime.strptime(gedcom.INDIs[v.wifeid].birthday, '%d %b %Y')
            for c in v.children:
                if gedcom.INDIs[c].birthday != 'N/A':
                    bd_child = datetime.strptime(gedcom.INDIs[c].birthday, '%d %b %Y')
                    diff_father = (abs((bd_father - bd_child).days))/365
                    diff_mother = (abs((bd_mother - bd_child).days))/365
                    if diff_father > 80:
                        print('ERROR: INDIVIDUAL: US12: ' + c + ': Has over 80 years than his father [ ' + str(diff_father) + 'years ].')
                    if diff_mother > 60:
                        print('ERROR: INDIVIDUAL: US12: ' + c + ': Has over 60 years than his mother [ ' + str(diff_mother) + 'years ].')

def US36():
    for k, v in gedcom.INDIs.items():
        if v.death != 'N/A':
            _date = datetime.strptime(v.death, '%d %b %Y')
            death = abs((_date  - datetime.today()).days)
            if death < 30:
                print('ERROR: INDIVIDUAL: US36: ' + v.indiid + ': died in the last 30 days [ ' + str(death) + 'days ].')
