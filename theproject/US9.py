from datetime import datetime
import gedcom
import re

def US09():
    print("US09: Birth before death of parents")
    
    for l,m in gedcom.FAMs.items():
        Hid=m.husbandid
        Wid=m.wifeid
        for id1 in m.children:
             #print(id1)
             child=id1
            # print(child)
             for k,i in gedcom.INDIs.items():
                 if child==i.indiid:
                     bday=i.birthday
                     #print(bday)
                 if Hid==i.indiid: 
                     ddayH=i.death
                     #print(dday)
                 if Wid==i.indiid:
                     ddayW=i.death
                     #print(dday)
                     if ddayH!='N/A' and ddayW!='N/A':
                         if bday<ddayH and bday<ddayW:
                             print("OK")
                         else:
                             print(bday)
                             print(ddayH)
                             print(ddayW)
                             
