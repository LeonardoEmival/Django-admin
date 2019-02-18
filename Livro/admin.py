from django.contrib import admin
from .models import Colecao
from .models import Livro
from .models import Caixa
from .models import Amigo
from .models import Emprestimo
from .models import Grupo_amigo
admin.site.register(Grupo_amigo)

class ColecaosAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(Colecao, ColecaosAdmin)

class LivroAdmin(admin.ModelAdmin):
    list_display = ['numero_edicao','ano']
admin.site.register(Livro,LivroAdmin)

class CaixaAdmin(admin.ModelAdmin):
    list_display = ['numero','etiqueta','cor']
    list_filter = ['cor']
admin.site.register(Caixa,CaixaAdmin)

class AmigoAdmin(admin.ModelAdmin):
    list_display = ['nome','grupo_amigo','telefone']
admin.site.register(Amigo,AmigoAdmin)

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['data_emprestimo']
    def data_f(self, obj):
        return obj.data_emprestimo.strftime('%d/%m/%y')
        data_f.short_description = 'data_emprestim'
admin.site.register(Emprestimo,EmprestimoAdmin)
