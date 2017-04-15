from dateutil.relativedelta import relativedelta
from datetime import datetime
import gedcom

def US09():
    for l,m in gedcom.FAMs.items():

        if gedcom.INDIs[m.husbandid].death != 'N/A':
            father_birthday = datetime.strptime(gedcom.INDIs[m.husbandid].death, '%d %b %Y')
            father_birthday_plus_9 = father_birthday + relativedelta(months=9)
        else:
            father_birthday = 'N/A'

        if gedcom.INDIs[m.wifeid].death != 'N/A':
            mother_birthday = datetime.strptime(gedcom.INDIs[m.wifeid].death, '%d %b %Y')
        else:
            mother_birthday = 'N/A'

        for child in m.children:
            if gedcom.INDIs[child].birthday != 'N/A':
                child_birthday = datetime.strptime(gedcom.INDIs[child].birthday, '%d %b %Y')
                if father_birthday != 'N/A' and child_birthday > father_birthday:
                    print('ERROR: INDIVIDUAL: US09: ' + child + ': Child born after 9 months after death of father.')
                if mother_birthday != 'N/A' and child_birthday > mother_birthday:
                    print('ERROR: INDIVIDUAL: US09: ' + child + ': Child born after death of mother.')

def US11():
    x = 0
    fam_list = []

    for v in gedcom.FAMs.itervalues():
        fam_list.append(v)

    while x < len(fam_list):
        y = x + 1
        while y < len(fam_list):
            if fam_list[x].husbandid == fam_list[y].husbandid and fam_list[x].divorced == 'N/A' and fam_list[y].divorced == 'N/A':
                print('ERROR: FAMILY: US11: ' + fam_list[x].husbandid + ' bigamy ' + fam_list[x].famid + ' and ' + fam_list[y].famid)
            if fam_list[x].wifeid == fam_list[y].wifeid and fam_list[x].divorced == 'N/A' and fam_list[y].divorced == 'N/A':
                print('ERROR: FAMILY: US11: ' + fam_list[x].wifeid + ' bigamy ' + fam_list[x].famid + ' and ' + fam_list[y].famid)
            y = y + 1;
        x = x + 1;
