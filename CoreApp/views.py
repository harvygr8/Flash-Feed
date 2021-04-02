from django.shortcuts import render
from django.views.generic.base import TemplateView
from pygooglenews import GoogleNews

# Create your views here.

from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "coreapp/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Home,self).get_context_data(*args, **kwargs)
        NewsList=[]
        GNews=GoogleNews()

        if 'srch' in self.request.GET:
            SearchVal=self.request.GET.get('srch')
            Results=GNews.search(SearchVal)
            for Item in Results['entries']:
                NewsList.append(Item)
        else:
            Results=GNews.top_news()
            for Item in Results['entries']:
                NewsList.append(Item)

        context['NewsList']=NewsList
        return context

class Sports(TemplateView):
        template_name = "coreapp/sports.html"

        def get_context_data(self, *args, **kwargs):
            context = super(Sports,self).get_context_data(*args, **kwargs)
            NewsList=[]
            GNews=GoogleNews()

            if 'srch' in self.request.GET:
                SearchVal=self.request.GET.get('srch')
                Results=GNews.search(SearchVal)
                for Item in Results['entries']:
                    NewsList.append(Item)
            else:
                Results=GNews.topic_headlines('sports')
                for Item in Results['entries']:
                    NewsList.append(Item)

            context['NewsList']=NewsList
            return context

# def Home(request):
#     NewsList=[]
#     GNews=GoogleNews()
#
#     if 'srch' in request.GET:
#         SearchVal=request.GET.get('srch')
#         Results=GNews.search(SearchVal)
#         for Item in Results['entries']:
#             NewsList.append(Item['title'])
#     else:
#         Results=GNews.search('India')
#         for Item in Results['entries']:
#             NewsList.append(Item)
#
#     return render(request,'CoreApp/index.html',context={'NewsList':NewsList})
