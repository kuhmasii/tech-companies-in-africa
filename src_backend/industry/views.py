from django.shortcuts import render
from . utils import industry_search, industry_paginator
from django.http import Http404
from . models import TechCompany, TechIndustry, TechList


def tech_list(request):

    # industry = TechIndustry.objects.all()
    alphabeth = TechList.objects.all()
    searched = industry_search(request)
    company_list, custom_range = industry_paginator(request, searched, 9)
    context = {'companies': company_list, 
                    'range':custom_range,
                    "alphabeth": alphabeth, 
                }

    return render(request, 'industry/tech_list.html', context)


def tech_alphabeth(request, alpha_name):
    # industry = TechIndustry.objects.all()
    alphabeth = TechList.objects.all()
    try:
        tech_list = TechList.objects.get(alphabet__iexact=alpha_name)
        companies = tech_list.get_company_by_alpha()
        company_list, custom_range = industry_paginator(request, companies, 9)
    except TechList.DoesNotExist:
        raise Http404

    context = {'companies': company_list, 
                'range':custom_range,
                "alphabeth": alphabeth, 
            }
    return render(request, 'industry/alphabeth.html', context)

# Finding a way to automate the industries when new one is added

# def tech_industry(request, indus_slug):
#     industry = TechIndustry.objects.all()
#     alphabeth = TechList.objects.all()
#     try:
#         tech_list = TechIndustry.objects.get(indus_slug__iexact=indus_slug)
#         companies = tech_list.get_company_by_indus()
#     except TechList.DoesNotExist:
#         raise Http404

#     context = {'companies': companies, 'tech_list': tech_list,
#                "industries": industry, "alphabeth": alphabeth, }
#     return render(request, 'industry/industry.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html')



