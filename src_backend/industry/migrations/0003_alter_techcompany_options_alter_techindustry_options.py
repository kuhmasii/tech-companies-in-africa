# Generated by Django 4.0 on 2022-04-20 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_techcompany_website_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='techcompany',
            options={'ordering': ('company_name',), 'verbose_name_plural': 'TechCompanies'},
        ),
        migrations.AlterModelOptions(
            name='techindustry',
            options={'ordering': ('industry_name',), 'verbose_name_plural': 'TechIndustries'},
        ),
    ]
