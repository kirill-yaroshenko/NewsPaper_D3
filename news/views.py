from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    
    model = News
    ordering = ['-date']
    template_name = "news.html"
    context_object_name = "news"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        
        return context



class PostDetail(DetailView):
    
    model = News
    template_name = 'post.html'
    context_object_name = 'post'
