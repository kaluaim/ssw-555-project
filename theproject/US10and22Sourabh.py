from datetime import datetime, timedelta
import gedcom

def US22UniqueIDs():
    x=0
    y=1
    for k,i in gedcom.FAMs.items():
        if i.famid[x]==i.famid[y]:
           print('ERROR: FAMILY: US22: ' + i.famid[x] + ' IDs are similar')
           x=x+1;
           y=y+1;
    for k,i, in gedcom.INDIs.items():
        if i.indiid[x]==i.indiid[y]:
           print('ERROR: INDIVIDUAL: US22: ' + i.indiid[x] + ' IDs are similar')
           x=x+1;
           y=y+1;

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
