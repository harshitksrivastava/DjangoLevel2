from django.contrib import admin
from trial_urls.models import Topic,AccessRecord,WebPage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
