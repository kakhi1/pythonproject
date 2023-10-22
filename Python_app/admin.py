from django.contrib import admin
from .models import Client, Site, FilterWord, Notification, Article
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

# Create a resource class for the FilterWord model to export data.
class FilterWordResource(resources.ModelResource):
    class Meta:
        model = FilterWord

# Define the FilterWordsImportExportAdmin class, which includes both import and export functionality.
class FilterWordsImportExportAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    resource_class = FilterWordResource
    list_display = ('id', 'clientid', 'word', 'wordAlias', 'subwordalias', 'stopword')
    search_fields = ['clientid__name', 'word']

# Define Inline classes for the related models
class ArticleInline(admin.StackedInline):
    model = Article
    extra = 0

class NotificationInline(admin.StackedInline):
    model = Notification
    extra = 0

# Define a custom function to toggle TTS settings.
def toggle_tts_enabled(modeladmin, request, queryset):
    for client in queryset:
        client.tts_enabled = not client.tts_enabled
        client.save()

toggle_tts_enabled.short_description = "Toggle Text-to-Speech setting"

# Admin class for the Client model. 
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'tts_enabled')
    actions = [toggle_tts_enabled]
    inlines = [ArticleInline, NotificationInline]

# Admin class for the Site model.
class SitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sitename', 'internal_id')

# Admin class for the Notification model.
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'sms', 'telegram', 'whatsapp', 'email')

# Admin class for the Article model.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_id', 'clientid', 'insert_date', 'article_date', 'autor', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_article', 'screenshot_url', 'status', 'found_word')
    list_filter = ('clientid',)
    search_fields = ('clientid__username', )

# Register models in the admin interface.
admin.site.register(Client, ClientAdmin)
admin.site.register(Site, SitesAdmin)
admin.site.register(Notification, NotificationsAdmin)
admin.site.register(Article, ArticlesAdmin)
admin.site.register(FilterWord, FilterWordsImportExportAdmin)

