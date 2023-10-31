from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):

        temp_commet = form.save(commit=False)
        temp_commet.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_commet.writer = self.request.user
        temp_commet.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
