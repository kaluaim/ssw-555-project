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
    print("")
    print("")
    print("user story 35: list of people born in last 30 days")
    print("")
    print("today's date : " + curdate)
    print("date 30 days before : " +  curdate2)
    print("")
    for k,i, in gedcom.INDIs.items():
        birtdate = datetime.strptime(i.birthday, '%d %b %Y')
        if birtdate < todaydate :
            if birtdate > deadlinedate :
                print("Person name is " + i.name)
                print("Birthday " + i.birthday)
                print("")
                flag = 0
                flag2 = 1
            else:
                flag = 1
        else:
            print("person is born in future")

    if flag2 == 0 :
        if flag == 1:
            print("No one is born in last 30 days")
