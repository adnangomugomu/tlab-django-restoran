from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Resep
from kategori.models import Kategori

class ResepViewsetTestCase(APITestCase):
    def setUp(self):        
        self.kategori = Kategori.objects.create(nama='Main Course')
        self.resep = Resep.objects.create(makanan='Nasi Goreng',kategori=self.kategori)

    def test_get_single_resep(self):
        url = reverse('resep-id', kwargs={'id': self.resep.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_resep(self):
        url = reverse('resep-cari')
        response = self.client.get(url, {'nama': 'Nasi'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['makanan'], 'Nasi Goreng')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_resep(self):
        url = reverse('resep')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_resep(self):
        url = reverse('resep')
        data = {'makanan': 'Mie Goreng','kategori':self.kategori.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_resep(self):
        url = reverse('resep-id', kwargs={'id': self.resep.id})
        data = {'makanan': 'Nasi Kuning'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_resep(self):
        url = reverse('resep-id', kwargs={'id': self.resep.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)