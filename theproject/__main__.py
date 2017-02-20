import gedcom
import US04sourabh
import util_khalid

FILE_PATH = 'GEDCOM.ged'

if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_families()

    util_khalid.check_family_dates(gedcom.FAMs)
    util_khalid.check_individual_dates(gedcom.INDIs)
    #US04sourabh.US4MbD()
