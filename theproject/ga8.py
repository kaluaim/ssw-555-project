from datetime import datetime, timedelta
import gedcom

birtdate=[]
now = datetime.now()
d = datetime.today() - timedelta(30)
curdate = now.strftime("%d %b %Y")
curdate2 = d.strftime("%d %b %Y")
todaydate = datetime.strptime(curdate, '%d %b %Y')
deadlinedate = datetime.strptime (curdate2 , '%d %b %Y' )
def US35bbm():
    flag = 0
    flag2 = 0
    for k,i, in gedcom.INDIs.items():
        birtdate = datetime.strptime(i.birthday, '%d %b %Y')
        if birtdate < todaydate :
            if birtdate > deadlinedate :
                flag = 0
                flag2 = 1
            else:
                flag = 1
        else:
            print('ERROR: INDIVIDUAL: US35: ' + i.indiid + ': Is born in future.')
