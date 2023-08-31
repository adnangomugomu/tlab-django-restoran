from django.urls import path
from .views import ResepViewset, CariResepViewset

urlpatterns = [
    path('resep', ResepViewset.as_view(),name='resep'),
    path('resep/<int:id>', ResepViewset.as_view(),name='resep-id'),
    path('resep/cari', CariResepViewset.as_view(),name='resep-cari'),
]