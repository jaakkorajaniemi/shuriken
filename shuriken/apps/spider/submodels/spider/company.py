from django.db import models

COMPANY_CREATED_AT = 'created_at'
COMPANY_UPDATED_AT = 'updated_at'
COMPANY_NAME = 'name'
COMPANY_URL = 'url'
COMPANY_SUMMARY = 'summary'
COMPANY_DESCRIPTION = 'description'
COMPANY_CATEGORY = 'category'
COMPANY_SUBCATEGORY = 'subcategory'
COMPANY_LOCATION = 'location'
COMPANY_COUNTRY = 'country'
COMPANY_CITY = 'city'
COMPANY_FOUNDERS = 'founders'
COMPANY_FOUNDED = 'founded'
COMPANY_FUNDING_TOTAL = 'funding_sum'
COMPANY_FUNDING_ROUND = 'funding_rnd'

class Company(models.Model):

    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='Published at', null=False)
    updated_at  = models.DateTimeField(auto_now_add=True, verbose_name='Modified at', null=False)

    name        = models.CharField(default='', max_length=256, null=False)
    url         = models.CharField(default='', max_length=256, null=True)
    summary     = models.TextField(default='', max_length=256, null=True)
    description = models.TextField(default='')
    
    category    = models.CharField(default='', max_length=256, null=True)
    subcategory = models.CharField(default='', max_length=256, null=True)

    location    = models.CharField(default='', max_length=128, null=True)
    country     = models.CharField(default='', max_length=128, null=True)
    city        = models.CharField(default='', max_length=128, null=True)
    founded     = models.DateTimeField(null=True)
    founders    = models.CharField(default='', max_length=256, null=True)

    funding_rnd = models.CharField(default='', max_length=256, null=True)
    funding_sum = models.CharField(default='', max_length=256, null=True)

    # Export
    def write(self, type, name, argv):
        pass

    # Import
    def read(self, type, name, argv):
        pass

    def load_crunchbase(self):
        if self.url is None:
            return False

        pass