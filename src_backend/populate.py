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


def file():
	file = open('techCompanies.json', 'r')
	json_file = json.load(file)
	return json_file

def populate_techlist(json_file):
	for keys, values in json_file.items():
		try:
			obj = TechList.objects.filter(alphabet__iexact=keys)

			if not obj.exists():
				TechList.objects.create(alphabet=keys.upper())
			else:
				print(f'{obj.first()} already exists.')
		except:
			print('something went wrong')
	return TechList.objects.all()

def populate_industry(json_file):
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
				else:
					print(f'{obj.first()} already exists.')
			except:
				print('something went wrong')
	return TechIndustry.objects.all()

def populate_company(json_file):
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
				else:
					print(f'{obj.first()} already exists.')
			except:
				print("something gone wrong")
	return TechCompany.objects.all()



file = file()
populate_techlist(file)
populate_industry(file)
populate_company(file)