from django.contrib import admin

from blog.models import Post



# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","type","active","author")
    list_filter = ('type',"author")
    search_fields = ('title',)
    list_editable = ("active",)




