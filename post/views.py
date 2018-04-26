from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import PostModel

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'post/index.html'
    model = PostModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostModel.objects.all()
        return context

class PostView(generic.DetailView):
    template_name = 'post/post.html'
    model = PostModel


def about(request):
    template_name = 'post/about.html'
    return render(request, template_name, {})

def contact(request):
    template_name = 'post/contact.html'
    return render(request, template_name, {})