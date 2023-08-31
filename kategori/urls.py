from django.urls import path
from .views import KategoriViewset

urlpatterns = [
    path('kategori', KategoriViewset.as_view(),name='kategori'),
    path('kategori/<int:id>', KategoriViewset.as_view(),name='kategori-id'),
]