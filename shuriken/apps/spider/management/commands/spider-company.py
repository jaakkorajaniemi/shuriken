from django.core.management.base import BaseCommand, CommandError
from shuriken.apps.spider.submodels.spider.company import *
from shuriken.apps.spider.submodels.spider.companies import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        companies = Companies()

        # Bind for reading from excel
        companies.bind(COMPANY_NAME, 'Company name')
        companies.bind(COMPANY_CATEGORY, 'Industry')
        companies.bind(COMPANY_URL, 'Link')
        companies.bind(COMPANY_SUMMARY, 'Business before')
        companies.bind(COMPANY_DESCRIPTION, 'Quote/reference text')
        companies.read(datatype='xlsx', dataname='source.xlsx')

        # Bind for writing into template
        companies.bind(COMPANY_NAME, "title")
        companies.bind(COMPANY_SUMMARY, "subtitle")
        companies.bind(COMPANY_DESCRIPTION, "description")
        companies.bind(COMPANY_URL, "url")
        companies.bind(COMPANY_CATEGORY, "category")
        companies.write(datatype="pptx", dataname='output.pptx', template='template.pptx')
