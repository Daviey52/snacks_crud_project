from django.urls import path
from django.urls.resolvers import URLPattern
from .views import snacksCreateView ,SnacksDetailView,SnacksDeleteView,SnacksListView,SnacksUpdateView

urlpatterns = [
  path('',SnacksListView.as_view(), name='snacks_list'),
  path('<int:pk>',SnacksDetailView.as_view(), name='snacks_detail'),
  path('new/',snacksCreateView.as_view(),name='snacks_create'),
  path('<int:pk>/edit',SnacksUpdateView.as_view(),name='snacks_update'),
  path('<int:pk>/delete', SnacksDeleteView.as_view(),name='snacks_delete'),
]
