
# from django.shortcuts import render
# from .models import Client, Site, FilterWord, Notification, Article

# def clients(request):
#     clients = Client.objects.all()
#     context = {'clients': clients}
#     return render(request, 'yourApplication/clients.html', context)

# def client_detail(request, client_id):
#     client = Client.objects.get(id=client_id)
#     sites = Site.objects.filter(client=client)
#     filterwords = FilterWord.objects.filter(client=client)
#     notifications = Notification.objects.filter(client=client)
#     articles = Article.objects.filter(client=client)
#     context = {'client': client, 'sites': sites, 'filterwords': filterwords, 'notifications': notifications, 'articles': articles}
#     return render(request, 'yourApplication/client_detail.html', context)