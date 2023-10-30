from django.urls import path
from django.views.generic import TemplateView


app_name = "profileapp"

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),

]