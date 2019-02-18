from django.contrib import admin
from .models import Curso
from .models import Professor
from .models import Turma

class ProfessorAdmin(admin.ModelAdmin):
    list_display = [ 'nome','telefone']
    search_fields = ['nome']
admin.site.register(Professor,ProfessorAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = [ 'data_inicio','hora_inicio']
    list_filter = ['data_inicio','hora_inicio']
admin.site.register(Turma,TurmaAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = [ 'nome','valor']
    search_fields = ['nome']
    list_filter = ['nome']
admin.site.register(Curso,CursoAdmin)

