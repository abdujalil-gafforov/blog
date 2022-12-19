from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, path
from django.utils.html import format_html

from app1.models import Category, User, Comment, Post, About

admin.site.index_title = "Sayt Administratsiyasi"

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'sh_image')
    ordering = ('name',)
    class Meta:
        name_p = 'category'


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'is_active')
    exclude = ('last_login', 'groups', 'user_permissions', 'date_joined')


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('user', 'post', 'text')
    exclude = ()


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ('email', 'address', 'phone_number')


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'id', 'slug', 'status_icon', 'status_buttons')
    readonly_fields = ('is_publish',)


    def response_change(self, request, obj):
        if "status" in request.POST:
            if request.POST["status"] == "active":
                self.confirmed(request, obj.id)
            if request.POST["status"] == "cancel":
                self.canceled(request, obj.id)
        return super().response_change(request, obj)

    def get_urls(self):
        urls = super().get_urls()
        urls += [path('cancel/<int:id>', self.canceled), path('confirm/<int:id>', self.confirmed)]
        return urls

    def canceled(self, request, id):
        post = Post.objects.filter(id=id).first()
        post.is_publish = Post.Status.CANCEL
        post.save()
        return HttpResponseRedirect('../')

    def confirmed(self, request, id):
        post = Post.objects.filter(id=id).first()
        post.is_publish = Post.Status.ACTIVE
        post.save()
        return HttpResponseRedirect('../')

    def status_icon(self, obj):
        data = {
            'pending': '<img src="https://cdn-icons-png.flaticon.com/512/483/483610.png" alt="Simply Easy Learning" width="25px" height="25px" height="80">',
            'active': '<img src="https://cdn-icons-png.flaticon.com/512/4436/4436481.png" alt="Simply Easy Learning" width="25px" height="25px" height="80">',
            'cancel': '<img src="https://cdn-icons-png.flaticon.com/512/5974/5974771.png" alt="Simply Easy Learning" width="25px" height="25px" height="80">',
        }
        return format_html(data[obj.is_publish])
