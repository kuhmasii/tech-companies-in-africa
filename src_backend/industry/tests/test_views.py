from django.test import TestCase
from django.urls import reverse
from industry.models import TechIndustry, TechCompany, TechList


# class TechListViewTests(TestCase):
#     def setUp(self):
#         indus = TechIndustry.objects.create(
#             industry_name="Gaming Tech"
#         )
#         alpha = TechList.objects.create(
#             alphabet="G"
#         )
#         TechCompany.objects.create(
#             industry=indus,
#             comp_alphabet = alpha,
#             company_name = "GAMERS*FREAKS"
#         )


#     def test_tech_list_view(self):
#         """
#         All list of Company is displayed.
#         """

#         obj = TechCompany.objects.all()
#         response = self.client.get(reverse('industry:tech_list'))

#         self.asserEqual(response.status_code, 200)
#         self.assertContains(response, 'GAMERS*FREAKS')
#         self.assertQuerysetEqual(response.context['industry'], obj)

#     def test_tech_alphabeth_view(self):
#         """ 
#         Given a letter, the query should bring
#         out data that correspond to the letter
#         """

#         obj = TechList.objects.get(pk=1)
#         response = self.client.get(
#             reverse('industry:tech_alphabeth', args=(obj.alphabet,))
#             )

#         self.asserEqual(response.status_code, 200)
#         self.assertContains(response, 'G')
#         self.assertQuerysetEqual(response.context['industry'], [obj])


        # still working on this functionality