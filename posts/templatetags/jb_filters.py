from django import template

register = template.Library()

#criando os próprios filtros
@register.filter(name="plural")
def plural_comentarios(num_comentarios):
    if num_comentarios > 1:
        return f'{num_comentarios} comentários'
    else:
        return f'{num_comentarios} comentario'