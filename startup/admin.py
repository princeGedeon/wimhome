from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from startup.models import Newsletter, Review, Partenaire, Magazine, Team, Compositeur


# Register your models here.
@admin.register(Newsletter)
class NewsAdmin(ExportActionModelAdmin):
  list_display = ("email",)


@admin.register(Review)
class ReviewsAdmin(ExportActionModelAdmin):
  list_display = ("title","author","star","active")
  list_filter = ("author","star")
  list_editable = ("active",)


@admin.register(Partenaire)
class Partenaire(admin.ModelAdmin):
  list_display = ('title','link','active')
  list_filter = ('active',)


@admin.register(Magazine)
class Magazine(admin.ModelAdmin):
  list_display = ('title','link','active')
  list_filter = ('active',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
  list_display = ('nom', 'title', 'link')
  list_filter = ('nom','title')

@admin.register(Compositeur)
class CompAdmin(admin.ModelAdmin):
  list_display = ('nom', 'title', 'link')
  list_filter = ('nom', 'title')




