from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetList, SnippetDetail, UserList, UserDetail, user_snippet_post

urlpatterns = [
    path("snippets/", SnippetList.as_view()),
    path("snippets/<int:pk>/", SnippetDetail.as_view()),
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("users/<int:pk>/snippets", user_snippet_post)
]