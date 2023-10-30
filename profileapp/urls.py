from django.urls import path, include

from accountapp.views import AccountCreateView
from profileapp.views import ProfileCreateView

app_name = "profileapp"

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),

]