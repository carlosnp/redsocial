from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        # atributos del campo
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de Usuario"
        self.fields["email"].label = "Dirección de Correo Electronico:"
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirme la Contraseña"
