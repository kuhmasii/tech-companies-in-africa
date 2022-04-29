from . models import TechCompany, TechIndustry, TechList
from django.db.models import Q

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