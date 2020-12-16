from django.urls import path
from .views import posts

urlpatterns = [
    path('', posts.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', posts.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', posts.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', posts.PostDetalhes.as_view(), name='post_detalhes'),
]
