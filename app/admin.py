from django.contrib import admin
from .models import Post, Tecnologia
from django.contrib.auth.models import User

# Register your models here.

admin.site.unregister(User)

class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]


admin.site.register(Post)
admin.site.register(Tecnologia)
admin.site.register(User, UserAdmin)
