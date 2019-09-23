from django.shortcuts import render
from django.http import HttpResponse
from trial_urls.models import Topic,WebPage,AccessRecord
# Create your views here.
def make_a_call(request):
    webpages_list = AccessRecord.objects.order_by('date')

    return render(request,'trial_urls/index.html',{'access_records':webpages_list})
