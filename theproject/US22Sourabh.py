from datetime import datetime, timedelta
import gedcom

#sprint 2
def US22UniqueIDs():
    print("User Story 22")
    x=0
    y=1
    
    for k,i in gedcom.FAMs.items():
        if i.famid[x]==i.famid[y]:
           print("IDs are similar")
           x=x+1;
           y=y+1;
        else:
            print("Family id Not Similar")

    for k,i, in gedcom.INDIs.items():
        if i.indiid[x]==i.indiid[y]:
           print("IDs are similar")
           x=x+1;
           y=y+1;
        else:
            print("individual id Not Similar")
