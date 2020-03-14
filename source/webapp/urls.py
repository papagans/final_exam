from django.urls import path
from webapp.views import IndexView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # # path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    # path('announce/create/', AnnonceCreateView.as_view(), name='announce_create'),
    # path('image/add/<int:pk>/', ImagesCreateView.as_view(), name='image_add'),
    # path('announce/detail/<int:pk>/', AnnounceDetailView.as_view(), name='announce_detail'),
    # # path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    # path('image/<int:pk>/delete/', ImagesDeleteView.as_view(), name='image_delete'),
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