from django.shortcuts import render
from django.views.generic import ListView
from auth_person.models import Post_news, User

# Create your views here.


def blog(request, foo):
    inf = {'login': foo}
    return render(request, 'blog/blog.html', context=inf)

class feed(ListView):
    template_name = 'blog/feed.html'
    model = Post_news
    paginate_by = 10
    def get_queryset(self):
        user_name = self.kwargs['foo']
        print(user_name)
        return Post_news.objects.all().order_by('-date_post').filter(user__login=user_name)

    def get_context_data(self, *, object_list=None, **kwargs):
