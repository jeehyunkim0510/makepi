from django.urls import path, include

from accountapp.views import AccountCreateView
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "profileapp"

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),

]