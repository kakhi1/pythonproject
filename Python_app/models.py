from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=255, unique=True)
    siteid = models.IntegerField()
    filterwordsid = models.IntegerField()
    tts_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class FilterWord(models.Model):
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    wordAlias = models.CharField(max_length=1022)
    subwordalias = models.CharField(max_length=255, null=True, blank=True)
    stopword = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.word

class Notification(models.Model):
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    sms = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Notification for {self.clientid.username}"

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.IntegerField()
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    insert_date = models.DateTimeField(auto_now_add=True)
    article_date = models.DateTimeField()
    autor = models.CharField(max_length=128, default='none')
    url = models.URLField(max_length=1022)
    article_name = models.TextField()
    article_text = models.TextField()
    visitors_count = models.IntegerField(default=0)
    is_top_article = models.BooleanField(default=False)
    screenshot_url = models.CharField(max_length=90, null=True, blank=True)
    status = models.IntegerField(default=1)
    found_word = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.article_name

class Site(models.Model):
    id = models.AutoField(primary_key=True)
    sitename = models.CharField(max_length=128, unique=True)
    internal_id = models.IntegerField(default=0)

    def __str__(self):
        return self.sitename
