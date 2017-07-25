from django.contrib import admin

# Register your models here.
from .models import Article, Person

'''
Class used to show other related fields in Article
'''
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'mod_date', )

    '''
    used to split forms into several sets
    '''
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Contents', {'classes': ['collapse', ], 'fields': ['content']}),
    ]

    '''
    used to filter entries
    '''
    list_filter = ['title', 'pub_date', ]
    
    '''
    used to search entries, add related fields into the tuple
    '''
    search_fields = ['title', 'mod_date', ]

    '''
    # funtion to get search result, while don't know how to use it.
    def get_search_results(self, req, queryset, search_item):
        queryset, use_distinct = super(ArticleAdmin, self).get_search_results(req, queryset, search_item)
        try:
            search_item_as_str = str(search_item)
            queryset |= self.objects.filter(pub_date=search_item_as_str)
        except:
            pass
        return queryset, use_distinct
    '''

    '''
    Operations with save and delete model
    '''
    def save_model(self, req, obj, form, change):
        if change: # for modification
            obj_original = self.model.objects.get(pk=obj.pk)
        else: # for adding
            obj_original = None

        obj.user = req.user
        obj.save()

    def delete_model(self, req, obj):
        '''
        Given a model instance delete it from the databse
        '''
        # handle something here
        obj.delete()

'''
Class used to show none- fields in Person
'''
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', )

'''
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)
'''
# admin.site.register(Article) # Basic useage of admin
admin.site.register(Article, ArticleAdmin) # Used for show other related fields
admin.site.register(Person, PersonAdmin)
# admin.site.register(MyModelAdmin)
