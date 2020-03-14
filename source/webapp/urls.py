from django.urls import path
from webapp.views import IndexView, FilesCreateView, FilesDeleteView, FilesUpdateView, FilesDetailView, \
    AddToPrivate, DeleteFromPrivate
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/create/', FilesCreateView.as_view(), name='file_create'),
    path('file/detail/<int:pk>/', FilesDetailView.as_view(), name='file_detail'),
    path('file/<int:pk>/delete/', FilesDeleteView.as_view(), name='file_delete'),
    path('file/<int:pk>/update/', FilesUpdateView.as_view(), name='file_update'),
    path('announce/add-to-favorites/', AddToPrivate.as_view(), name='add_to_favorites'),
    path('announce/delete-from-favorites/', DeleteFromPrivate.as_view(), name='delete_from_favorites')
]

app_name = 'webapp'