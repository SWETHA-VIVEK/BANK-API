# -*- coding: utf-8 -*-

from django.urls import include, path



from api.views import BranchView,SearchView





urlpatterns = [
   path('branch?<str:q>&<int:limit>&<int:offset>', BranchView.as_view()),
   path('search?<str:q>&<int:limit>&<int:offset>', SearchView.as_view()),
]