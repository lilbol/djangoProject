from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.ShowsListView.as_view(), name='shows_all'),
    path('shows/<int:id>/', views.ShowsDetailView.as_view(), name='shows_detail'),
    path('shows/<int:id>/delete/', views.ShowsDeleteView.as_view(), name='book_delete'),
    path('shows/<int:id>/update/', views.ShowsUpdateView.as_view(), name='show_update'),
    path('add-show/', views.ShowsCreatView.as_view(), name='add_show'),

]