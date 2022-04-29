from django.db import models

class TechIndustry(models.Model):
    industry_name = models.CharField(max_length=200, blank=False, null=False)
    indus_slug = models.SlugField(max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('industry_name',)
        verbose_name_plural = 'TechIndustries'

    def __str__(self):
        return self.industry_name

    def get_company_by_indus(self):
        companies = self.indus.all().order_by('company_name')
        return companies


class TechList(models.Model):
    alphabet = models.CharField(max_length=4, blank=False, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('alphabet',)
        verbose_name_plural = 'TechLists'

    def __str__(self):
        return self.alphabet

    def get_company_by_alpha(self):
        companies = self.alpha.all().order_by('company_name')
        return companies


class TechCompany(models.Model):
    industry = models.ForeignKey(
        TechIndustry,
        on_delete=models.CASCADE,
        related_name='indus'
    )
    comp_alphabet = models.ForeignKey(
        TechList,
        on_delete=models.CASCADE,
        related_name='alpha'
    )
    company_name = models.CharField(
        max_length=200, blank=False, null=False
    )
    website_url = models.URLField(blank=True, null=True)
    comp_slug = models.SlugField(max_length=150)
    founders = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('company_name',)
        verbose_name_plural = 'TechCompanies'

    def __str__(self):
        return self.company_name



