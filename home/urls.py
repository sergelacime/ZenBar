from django.urls import re_path
from .views import *
urlpatterns = [
    re_path(r'^$', Index.as_view(), name="index"),
    re_path(r'^tables/$', TableView.as_view(), name="tables"),
    re_path(r'^stock/$', StockView.as_view(), name="stock"),
    re_path(r'^entries/$', StockEntries.as_view(), name="entries"),
]