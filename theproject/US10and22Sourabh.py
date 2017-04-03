from datetime import datetime, timedelta
import gedcom


# check Fam IDs
def US22UniqueIDs():
    x = 0
    fam_list = []
    indi_list = []

    for v in gedcom.FAMs.itervalues():
        fam_list.append(v)

    for v in gedcom.INDIs.itervalues():
        indi_list.append(v)

    while x < len(fam_list):
        y = x + 1
        while y < len(fam_list):
            if fam_list[x].famid == fam_list[y].famid:
                print('ERROR: FAMILY: US22: ' + fam_list[x].famid +
                ' for husbandid ' + fam_list[x].husbandid +
                ' IDs are similar to husbandid ' + fam_list[y].husbandid)
            y = y + 1;
        x = x + 1;

        while x < len(indi_list):
            y = x + 1
            while y < len(indi_list):
                if indi_list[x].indiid == indi_list[y].indiid:
                    print('ERROR: INDIVIDUAL: US22: ' + indi_list[x].indiid +
                    ' for ' + indi_list[x].name + ' IDs are similar to ' +
                    indi_list[y].name)
                y = y + 1;
            x = x + 1;
            
            

def US10Ma14():
    for l,m in gedcom.FAMs.items():
        for k,i in gedcom.INDIs.items():
            if m.married != 'N/A':
                if i.indiid==m.husbandid or i.indiid==m.wifeid:
                    bday=i.birthday
                    mrdate=m.married
                    bday1=bday.split(' ')
                    a=bday1[2]
                    mrdate1=mrdate.split(' ')
                    b=mrdate1[2]
                    d1 = datetime.strptime(a, "%Y")
                    d2 = datetime.strptime(b, "%Y")
                    diff=((d2-d1).days)
                    #print(diff)
                    if diff<=5110:
                        print('ERROR: INDIVIDUAL: US10: ' + i.indiid +
                            ': Birthday ' + i.birthday +
                            ' got married before begin 14 at marriage date: '
                            + m.married)
