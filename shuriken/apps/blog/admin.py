from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, File
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content','description',)

admin.site.register(Post, PostAdmin)
admin.site.register(File)


