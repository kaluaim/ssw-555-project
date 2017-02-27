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

    # Demonstration of user stories
    # US01
    fam_check = util_khalid.check_family_dates_before_current(gedcom.FAMs)
    indi_check = util_khalid.check_individual_dates_before_current(gedcom.INDIs)
    # US02

    # US03

    # US04
    US0408.US4MbD()
    # US05

    # US06

    # US07
    util_khalid.check_individual_age_less_than_150(gedcom.INDIs)
    # US08
    US0408.US08bbmp()
