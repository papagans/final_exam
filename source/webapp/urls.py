from django.urls import path
from webapp.views import IndexView, FilesCreateView, FilesDeleteView, FilesUpdateView, FilesDetailView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # # path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('file/create/', FilesCreateView.as_view(), name='file_create'),
    # path('image/add/<int:pk>/', ImagesCreateView.as_view(), name='image_add'),
    path('file/detail/<int:pk>/', FilesDetailView.as_view(), name='file_detail'),
    # # path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('file/<int:pk>/delete/', FilesDeleteView.as_view(), name='file_delete'),
    path('file/<int:pk>/update/', FilesUpdateView.as_view(), name='file_update'),
    # path('announce/add-to-favorites/', AddToFavorites.as_view(), name='add_to_favorites'),
    # path('announce/delete-from-favorites/', DeleteFromFavorites.as_view(), name='delete_from_favorites')

    # path('article/search/', ArticleSearchView.as_view(), name='article_search'),
    # path('article/search/results/', SearchResultsView.as_view(), name='search_results'),
    # path('comments/', CommentListView.as_view(), name='comment_list'),
    # path('comment/add/', CommentCreateView.as_view(), name='comment_add'),
    # path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
    # path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    # path('article/<int:pk>/add-comment/', CommentForArticleCreateView.as_view(), name='article_comment_create'),
]

app_name = 'webapp'