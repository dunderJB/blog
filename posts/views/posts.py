from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from ..models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages


class PostIndex(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related(
            "categoria_post"
        )  # isso é uma melhora de performance no código evitando consulta na hora de carregar o item categoria post a partir do post, esse item irá seguir a fk pelo proprio objeto post
        qs = qs.order_by("-id").filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(When(comentario__publicado_cometario=True, then=1))
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = "posts/post_busca.html"

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get("termo")

        if not termo:
            return qs

        qs = qs.filter(  # sempre escolher o objeto qual eu quero fazer querys para pesquisar things em seus atributos, lembrando que essa class PostBusca herda uma classe que o modelo de objeto que está sendo usado é o Posts
            Q(titulo_post__icontains=termo)
            | Q(autor_post__first_name__iexact=termo)
            | Q(conteudo_post__icontains=termo)
            | Q(excerto_post__icontains=termo)
            | Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs


class PostCategoria(PostIndex):
    template_name = "posts/post_categoria.html"

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get("categoria", None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)

        return qs


class PostDetalhes(UpdateView):
    model = Post
    template_name = "posts/post_detalhe.html"
    form_class = FormComentario
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(
            publicado_cometario=True, post_comentario=post.id
        )
        contexto["comentarios"] = comentarios
        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()

        messages.success(self.request, "Comentário enviado com sucesso!")

        return redirect("post_detalhes", pk=post.id)
