from django.test import TestCase
from industry.models import TechIndustry, TechCompany, TechList


class TechIndustryTests(TestCase):

    def setUp(self):
        TechIndustry.objects.create(
            industry_name="Gaming Tech"
        )

    def test_industry_creation(self):
        """
        Testing an instance of a TechIndustry model created.
        Instance should return the data of an 'industry_name'
        attribute as the '__str__' of the model, TechIndustry.
        """

        obj = TechIndustry.objects.get(pk=1)
        expected_obj_title = str(obj.industry_name)

        self.assertEqual(obj.__str__(), expected_obj_title)
        self.assertIsInstance(obj, TechIndustry)

    def test_not_industry_creation(self):
        """
        Testing an instance of a TechIndustry model is not 
        created
        """

        obj = TechIndustry.objects.get(pk=1)
        not_obj = 'This is just a dummy word'

        self.assertNotIsInstance(not_obj, TechIndustry)
        self.assertNotEqual(obj.__str__(), not_obj)

    def test_data_for_instance_of_industry_model(self):
        """
        Testing an instance data is correct.
        """

        ins = TechIndustry.objects.get(pk=1)

        self.assertEqual(ins.industry_name, 'Gaming Tech')

    def test_data_not_for_instance_of_industry_model(self):
        """
        Testing an instance data is not correct
        """
        ins = TechIndustry.objects.get(pk=1)

        self.assertNotEqual(ins.industry_name, 'This is not your data')

    def test_get_company_by_indus_with_value(self):
        """
           get_company_by_indus method should return all
           query in TechCompany model.
        """
        ins = TechIndustry.objects.get(pk=1)
        alpha = TechList.objects.create(alphabet='G')
        company = TechCompany.objects.create(
            industry=ins,
            comp_alphabet=alpha,
            company_name='GAMERS*FREAKS'
        )

        get_company = ins.get_company_by_indus()

        self.assertQuerysetEqual([company], get_company)
        self.assertTrue(get_company)

    def test_get_company_by_indus_without_value(self):
        """
           get_company_by_indus method should return an empty
           query in TechCompany model.
        """
        ins = TechIndustry.objects.get(pk=1)

        get_company = ins.get_company_by_indus()

        self.assertFalse(get_company)


class TechListests(TestCase):
    def setUp(self):
        TechList.objects.create(
            alphabet="G"
        )

    def test_techlist_creation(self):
        """
        Testing an instance of a TechList model created.
        Instance should return the data of an 'alphabet'
        attribute as the '__str__' of the model, TechList.
        """

        obj = TechList.objects.get(pk=1)
        expected_obj_title = str(obj.alphabet)

        self.assertEqual(obj.__str__(), expected_obj_title)
        self.assertIsInstance(obj, TechList)

    def test_not_techlist_creation(self):
        """
        Testing an instance of a TechList model is not 
        created
        """

        obj = TechList.objects.get(pk=1)
        not_obj = 'This is just a dummy word'

        self.assertNotIsInstance(not_obj, TechList)
        self.assertNotEqual(obj.__str__(), not_obj)

    def test_data_for_instance_of_techlist_model(self):
        """
        Testing an instance data is correct.
        """

        ins = TechList.objects.get(pk=1)

        self.assertEqual(ins.alphabet, 'G')

    def test_data_not_for_instance_of_techlist_model(self):
        """
        Testing an instance data is not correct
        """
        ins = TechList.objects.get(pk=1)

        self.assertNotEqual(ins.alphabet, 'A')

    def test_get_company_by_alpha_with_value(self):
        """
           get_company_by_alpha method should return all
           query in TechList model.
        """
        ins = TechList.objects.get(pk=1)
        industry = TechIndustry.objects.create(
            industry_name="Gaming Tech"
        )
        company = TechCompany.objects.create(
            industry=industry,
            comp_alphabet=ins,
            company_name='GAMERS*FREAKS'
        )

        get_company = ins.get_company_by_alpha()

        self.assertQuerysetEqual([company], get_company)
        self.assertTrue(get_company)

    def test_get_company_by_alpha_without_value(self):
        """
           get_company_by_alpha method should return an empty
           query in TechList model.
        """
        ins = TechList.objects.get(pk=1)

        get_company = ins.get_company_by_alpha()

        self.assertFalse(get_company)


class TechCompanyTests(TestCase):
    def setUp(self):
        indus = TechIndustry.objects.create(
            industry_name="Gaming Tech"
        )
        alpha = TechList.objects.create(
            alphabet="G"
        )
        TechCompany.objects.create(
            industry=indus,
            comp_alphabet=alpha,
            company_name="GAMERS*FREAKS"
        )

    def test_techcompany_creation(self):
        """
        Testing an instance of a TechCompany model created.
        Instance should return the data of the 'company_name'
        attribute as the '__str__' of the model, TechCompany.
        """

        obj = TechCompany.objects.get(pk=1)
        expected_obj_title = str(obj.company_name)

        self.assertEqual(obj.__str__(), expected_obj_title)
        self.assertIsInstance(obj, TechCompany)

    def test_not_techcompany_creation(self):
        """
        Testing an instance of a TechCompany model is not 
        created
        """

        obj = TechCompany.objects.get(pk=1)
        not_obj = 'This is just a dummy word'

        self.assertNotIsInstance(not_obj, TechCompany)
        self.assertNotEqual(obj.__str__(), not_obj)

    def test_data_for_instance_of_techcompany_model(self):
        """
        Testing an instance data is correct.
        """

        ins = TechCompany.objects.get(pk=1)

        self.assertEqual(ins.company_name, 'GAMERS*FREAKS')

    def test_data_not_for_instance_of_techcompany_model(self):
        """
        Testing an instance data is not correct
        """
        ins = TechCompany.objects.get(pk=1)

        self.assertNotEqual(ins.company_name, 'gameing company')
