from django.contrib import admin

# Register your models here.
from .models import Article, Person

'''
Class used to show other related fields in Article
'''
class ArticleAdmin(admin.ModelAdmin):
   list_display = ('title', 'pub_date', 'mod_date', )

'''
Class used to show none- fields in Person
'''
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', )

# admin.site.register(Article) # Basic useage of admin
admin.site.register(Article, ArticleAdmin) # Used for show other related fields
admin.site.register(Person, PersonAdmin)
