from django.contrib import admin


from .models import Post, Category ,Comment_Box, Blink

class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug','created_on','author','status',)
    search_fields = ['titte','content']


   

admin.site.register(Post,PostAdmin),
admin.site.register(Category),
admin.site.register(Comment_Box) 
admin.site.register(Blink) 