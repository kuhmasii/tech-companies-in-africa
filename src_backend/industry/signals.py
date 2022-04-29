from django.utils.text import slugify
from industry.models import TechIndustry, TechCompany

# signals imports
from django.dispatch import receiver
from django.db.models.signals import(
    post_save, pre_save
)



@receiver(pre_save, sender=TechIndustry)
def industry_slug_create_pre_save_handler(sender, instance, *args, **kwargs):
    if not instance.indus_slug:
        instance.indus_slug = slugify(instance.industry_name)

@receiver(pre_save, sender=TechCompany)
def comp_slug_create_pre_save_handler(sender, instance, *args, **kwargs):
    if not instance.comp_slug:
	    slug = [instance.company_name, instance.industry.industry_name, instance.comp_alphabet.alphabet]
	    instance.comp_slug = slugify(" ".join(slug))