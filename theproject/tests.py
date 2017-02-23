import unittest
from gedcom import Individual, Family
import util_khalid

class TestDates(unittest.TestCase):
    def test_check_family_dates(self):
        fams = {}
        fam1 = Family('1')
        fam1.married = '21 APR 1968'
        fam2 = Family('2')
        fam2.married = '23 MAY 1959'
        fam3 = Family('3')
        fam3.married = '30 NOV 1919'
        fam3.divorced = '29 JUN 1989'
        fams['1'] = fam1
        fams['2'] = fam2
        fams['3'] = fam3
        self.assertTrue(util_khalid.check_family_dates(fams))

    def test_check_individual_dates(self):
        indis = {}
        indi1 = Individual('1')
        indi1.birthday = '21 APR 1968'
        indi2 = Individual('2')
        indi2.birthday = '23 MAY 1959'
        indi3 = Individual('3')
        indi3.birthday = '30 NOV 1919'
        indi3.death = '29 JUN 1989'
        indis['1'] = indi1
        indis['2'] = indi2
        indis['3'] = indi3
        self.assertTrue(util_khalid.check_individual_dates(indis))

    def test_date_before_current(self):
        self.assertTrue(util_khalid.is_date_before_current('13 OCT 1987'))
        self.assertTrue(util_khalid.is_date_before_current('13 OCT 2016'))
        self.assertFalse(util_khalid.is_date_before_current('13 OCT 2090'))

        self.assertRaises(ValueError, util_khalid.is_date_before_current('132342'))
        try:
            self.assertTrue(util_khalid.is_date_before_current('132342'))
            self.fail('Not a vaild date')
        except Exception as e:
            pass

        try:
            self.assertTrue(util_khalid.is_date_before_current('OCT 13 2000'))
            self.fail('Wrong date format')
        except Exception as e:
            pass


if __name__ == '__main__':
    unittest.main()
