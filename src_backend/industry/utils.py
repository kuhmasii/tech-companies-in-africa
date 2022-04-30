from . models import TechCompany, TechIndustry, TechList
from django.db.models import Q
from django.core.paginator import (
    Paginator, 
    EmptyPage,
    PageNotAnInteger
)

def industry_search(request):

    if q := request.GET.get("search"):

        techlist = TechCompany.objects.filter(
            Q(company_name__icontains=q)
            | Q(founders__icontains=q)
            | Q(industry__industry_name__icontains=q)
            | Q(comp_alphabet__alphabet__icontains=q)

        )
    else:
        techlist = TechCompany.objects.all()

    return techlist

def industry_paginator(request, company, number):
    
    page_num = request.GET.get('page')
    paginate = Paginator(company, number)
    try:
        page_obj = paginate.page(page_num)
    except PageNotAnInteger:
        page_obj = paginate.page(1)
    except EmptyPage:
        page_obj = paginate.page(paginate.num_pages)

    custom_range = range(1, 3)   
    if page_num != None:
        left_index = (int(page_num)- 2)
        if left_index < 1:
            left_index = 1

        right_index = (int(page_num) +2)
        if right_index > paginate.num_pages:
            right_index = paginate.num_pages + 1

        custom_range = range(left_index, right_index)

    return page_obj, custom_range