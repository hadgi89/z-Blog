from django.contrib import admin
from django import forms

from .models import *


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagAdminForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)
    list_display = ('id', 'title')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)
    list_display = ('id', 'title')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)
    list_display = ('id', 'user', 'title', 'image', 'post_sourse', 'is_draft')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created_at', 'updated_at')
        
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['profile'].initial = request.user.profile
        return form


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     save_as = True
#     save_on_top = True
#     list_display = ('id', 'post', 'username', 'comment', 'active')