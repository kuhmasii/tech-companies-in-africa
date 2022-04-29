from django.contrib import admin
from .models import TechCompany, TechIndustry, TechList

class TechIndustryAdmin(admin.ModelAdmin):
	list_display = ("industry_name", "updated", "created")
	list_filter = ('industry_name', 'updated', 'created')
	prepopulated_fields = {"indus_slug": ("industry_name",)}

class TechCompanyAdmin(admin.ModelAdmin):
	list_display = ("company_name", "industry", "updated", "created")
	list_filter = ('industry', 'comp_alphabet','updated', 'created')
	prepopulated_fields = {"comp_slug": ("company_name","industry","comp_alphabet")}



class TechListAdmin(admin.ModelAdmin):
	list_display = ("alphabet", "updated", "created")
	list_filter = ('alphabet','updated', 'created')

admin.site.register(TechList, TechListAdmin)
admin.site.register(TechIndustry, TechIndustryAdmin)
admin.site.register(TechCompany, TechCompanyAdmin)
