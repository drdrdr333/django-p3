from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += '\n'.join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += '\n'.join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

class BloggingListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-published_date')
    template_name = 'blogging/list.html'

class BloggingDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'


# def list_view(request):
#     published = Post.objects.all()
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context=context)

# def detail_view(request, post_id):
#     published = Post.objects.all()
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)