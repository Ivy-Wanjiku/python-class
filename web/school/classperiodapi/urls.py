from django.urls import path, include
from .views import ClassPeriodListView
urlpatterns = {
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view')
}




