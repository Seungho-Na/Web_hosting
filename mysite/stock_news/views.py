from django.http import HttpResponse
from .models import News
from django.template import loader
from django.utils import timezone
from .news_crawler import CrawlObj

#from django.shortcuts import render

def index(request):
    urlsAndtext = CrawlObj().crawl_news()
    for uAt in urlsAndtext:
        n = News(url_text=uAt[0], news_text=uAt[1], pub_date=timezone.now())
        n.save()

    db_news_list = News.objects.order_by('id')
    latest_news_list = db_news_list[len(db_news_list)-len(urlsAndtext):]

    template = loader.get_template('stock_news/index.html')
    context = {
        'latest_news_list': latest_news_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, news_id):
    return HttpResponse("You're looking at news %s." % news_id)
