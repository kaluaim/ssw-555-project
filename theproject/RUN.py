import gedcom
import ga
import ga2
import ga3
import ga4
import ga5
import ga6
import ga7
import ga8

FILE_PATH = './Gedcom1.ged'
if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_familie()  
    ga.US02bbm()
    ga2.US03bbm()
    ga3.US05bbm()
    ga4.US06bbm()
    ga5.US30bbm()
    ga6.US31bbm()
    ga7.US29bbm()
    ga8.US35bbm()
