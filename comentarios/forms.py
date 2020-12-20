from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get("g-recaptcha-response")

        req = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": "6LcOkA0aAAAAAAhkfP1b_g3MlN0WjvA_GnF70RZq",
                "response": recaptcha_response,
            },
        )

        recaptcha_result = req.json()

        if not recaptcha_result.get("success"):
            self.add_error("comentario", "Rcaptcha incorreto =/")

        data_cleaned = self.cleaned_data
        nome = data_cleaned.get("nome_comentario")
        email = data_cleaned.get("email_comentario")
        comentario = data_cleaned.get("comentario")

        if len(nome) < 5:
            self.add_error(
                "nome_comentario", "O nome precisar possui mais de 5 caracteres"
            )

    class Meta:
        model = Comentario
        fields = ("nome_comentario", "email_comentario", "comentario")
