import gedcom
import US0408sourabh as US0408
import util_khalid

FILE_PATH = 'GEDCOM1.ged'

if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_families()

    # US01
    print('\n--- US01: Dates before current date ---')
    fam_check = util_khalid.check_family_dates_before_current(gedcom.FAMs)
    indi_check = util_khalid.check_individual_dates_before_current(gedcom.INDIs)

    # US07
    print('\n--- US07: Less then 150 years old ---')
    util_khalid.check_individual_age_less_than_150(gedcom.INDIs)

    #US04
    US0408.US4MbD()
    #US08
    US0408.US08bbmp()
