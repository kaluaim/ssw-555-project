from datetime import datetime
import gedcom
divdate=[]
mardate=[]
def US4MbD():
    print("USER STORY 04")
    for k,i in gedcom.FAMs.items():
        divdate=i.divorced
        mardate=i.married
        #print(divdate)
        if i.divorced != 'N/A':
            if i.divorced < i.married:
                print('error')
            
            else:
                print("everything is fine. No divorce before marriage")
        
            
        
def US08bbmp():
    print("User story 8")
    #import families from gedcom
    for l,m in gedcom.FAMs.items():
        if m.married:
            #If the person is married check for bday and id 
            for k,i, in gedcom.INDIs.items():
                id1=i.indiid
                bday=i.birthday
            #Identify the child using
                if id1 in m.children:
                    if bday<m.married:
                        print("error"+'id='+id1)
                       # print('id='+id1)
                    else:
                        print("Everything is OK " + 'id '+id1)
                        #print('id'+id1)
