# fetch the json file
# populate the data into the database via each model
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src_backend.settings')
django.setup()


from industry.models import (
			TechList, 
			TechIndustry, 
			TechCompany
		)
import json


file = open('techCompanies.json', 'r')
json_file = json.load(file)

def populate_techlist():
	for key, values in json_file.items():
		try:
			obj = TechList.objects.filter(alphabet__iexact=key)

			if not obj.exists():
				TechList.objects.create(alphabet=key.upper())
		except IndexError:
			pass
	return TechList.objects.all()

def populate_industry():
	for keys,values in json_file.items():
		for val in values:
			try:
				obj = TechIndustry.objects.filter(
					industry_name__iexact=val["industry"]
				)

				if not obj.exists():
					TechIndustry.objects.create(
							industry_name=val['industry']
						)
					print(val['industry'])
			except:
				pass
	return TechIndustry.objects.all()

def populate_company():
	for keys,values in json_file.items():
		for val in values:
			try:
				ind = TechIndustry.objects.filter(
					industry_name__iexact=val["industry"]
				)
				alp = TechList.objects.filter(alphabet__iexact=keys)
				obj = TechCompany.objects.filter(
					company_name__iexact=val["companyName"]
				)

				if not obj.exists():
					TechCompany.objects.create(
							industry=ind.first(),
							comp_alphabet=alp.first(),
							company_name=val['companyName'],
							website_url=val['website'],
							founders=", ".join(val['foundersTwitterHandle']),
							twitter_handle=val['companyTwitterHandle'],
						)
					print(val['companyName'])
			except:
				print("something gone wrong")
	return TechCompany.objects.all()


populate_techlist()
populate_industry()
populate_company()