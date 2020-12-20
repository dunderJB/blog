from django import template

register = template.Library()

# era para funcionar sendo um filtro customizado usado depois do pipe igual o title no front end
# @register.filter(name="plural_comentario")
# def plural_comentario(num_comentarios):
#     try:
#         qtd_comentario = int(num_comentarios)

#         if qtd_cometario == 0:
#             return f"Nenhum comentário(s)"
#         elif qtd_comentario == 1:
#             return f"{qtd_cometario} comentario"
#         else:
#             return f"{qtd_cometario} comentarios"
#     except:
#         return "Nenhum comentário(s)"
