from django.http import HttpResponse
from .models import News
from django.template import loader
from django.utils import timezone
from .news_crawler import CrawlObj

#from django.shortcuts import render

def index(request):
    urls = CrawlObj().crawl_news_url()
    for url in urls:
        n = News(url_text=url, pub_date=timezone.now())
        n.url_text = url
        n.save()

    news_list = News.objects.order_by('id')
    length = len(news_list)
    latest_news_list = news_list[length-10:]

    template = loader.get_template('stock_news/index.html')
    context = {
        'latest_news_list': latest_news_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, news_id):
    return HttpResponse("You're looking at news %s." % news_id)
