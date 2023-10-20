from django.contrib import admin
from .models import Client, Site, FilterWord, Notification, Article


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'tts_enabled')

class SitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sitename','internal_id')

class FilterWordsAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'word', 'wordAlias', 'subwordalias', 'stopword')

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'sms', 'telegram', 'whatsapp', 'email')

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_id', 'clientid', 'insert_date', 'article_date','autor', 'url','article_name','article_text','visitors_count','is_top_article','screenshot_url','status','found_word')

# Register  models
admin.site.register(Client, ClientsAdmin)
admin.site.register(Site, SitesAdmin)
admin.site.register(FilterWord, FilterWordsAdmin)
admin.site.register(Notification, NotificationsAdmin)
admin.site.register(Article, ArticlesAdmin)


