from django.contrib import admin
from .models import Contas
from .models import Tipodespesa
from .models import Forma_Pagamento

class ContasAdmin(admin.ModelAdmin):
    list_display = [ 'tipo_despesa','vencimento']
    list_filter = ['vencimento','quitado']
    ordering = ['tipo_despesa','vencimento']
admin.site.register(Contas,ContasAdmin)
admin.site.register(Tipodespesa)
admin.site.register(Forma_Pagamento)
admin.site.admin_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Trabalho turma 366'
