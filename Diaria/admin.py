from django.contrib import admin
from .models import Cliente
from .models import Endereco
from .models import Diaria
from .models import Casa
from .models import ItemDiaria

admin.site.register(Endereco)
admin.site.register(Diaria)
admin.site.register(Casa)
admin.site.register(ItemDiaria)

class ClienteAdmin(admin.ModelAdmin):
    list_display = [ 'nome','telefone']
    search_fields = ['nome']
admin.site.register(Cliente,ClienteAdmin)
