from django.db import models
from django.contrib import admin
from .models import Post, Tecnologia
from django.contrib.auth.models import User
from mdeditor.widgets import MDEditorWidget

# Register your models here.

admin.site.unregister(User)

# class PostInline(admin.TabularInline):
#     model = Post
#     extra = 1

class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'conteudo')
        }),
        ('Relacionamentos', {
            'classes': ('collapse', ),
            'fields': ('autor', 'tecnologias')
        }),
    )
    list_display = ['descricao', 'titulo',]
    list_filter = ['titulo', 'tecnologias', ]
    list_per_page = 1
    ordering = ['titulo', ]
    search_fields = ['titulo', 'descricao', ]
    search_help_text = "Busca de posts por titulo"



admin.site.register(Post, PostAdmin)
admin.site.register(Tecnologia)
admin.site.register(User, UserAdmin)
