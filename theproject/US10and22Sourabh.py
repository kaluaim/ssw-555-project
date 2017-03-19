from datetime import datetime, timedelta
import gedcom

def US22UniqueIDs():
    print("User Story 22")
    x=0
    y=1
    
    for k,i in gedcom.FAMs.items():
        if i.famid[x]==i.famid[y]:
           print("IDs are similar")
           x=x+1;
           y=y+1;
    print("Family id Not Similar")

    for k,i, in gedcom.INDIs.items():
        if i.indiid[x]==i.indiid[y]:
           print("IDs are similar")
           x=x+1;
           y=y+1;
         
    print("individual id Not Similar")
            
            
            
            
def US10Ma14():
    print("User Story 10: Marriage before 14")
    for l,m in gedcom.FAMs.items():
        for k,i in gedcom.INDIs.items():
            if m.married!=None:
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
                         print("error "+"Married on "+m.married+" Born on "+i.birthday)
                
