from django.urls import path
from .views import BahanViewset

urlpatterns = [
    path('bahan', BahanViewset.as_view(), name='bahan'),
    path('bahan/<int:id>', BahanViewset.as_view(), name='bahan-id'),
]
