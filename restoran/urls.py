from django.urls import path, include
from django.http import JsonResponse


def hello(request):
    data = {
        'message': 'Aplikasi Pendataan Resep dan Bahan Restoran',
        'status': 'success',
    }
    return JsonResponse(data, status=200)

urlpatterns = [
    path('', hello),
    path('api/', include('kategori.urls')),
    path('api/', include('bahan.urls')),
    path('api/', include('resep.urls')),
]
