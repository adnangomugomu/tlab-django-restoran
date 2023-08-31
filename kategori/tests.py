from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Kategori

class KategoriViewsetTestCase(APITestCase):
    def setUp(self):
        self.kategori = Kategori.objects.create(nama='Main Course')

    def test_get_single_kategori(self):
        url = reverse('kategori-id', kwargs={'id': self.kategori.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_kategori(self):
        url = reverse('kategori')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_kategori(self):
        url = reverse('kategori')
        data = {'nama': 'Minuman'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_kategori(self):
        url = reverse('kategori-id', kwargs={'id': self.kategori.id})
        data = {'nama': 'Makanan Ringan'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_kategori(self):
        url = reverse('kategori-id', kwargs={'id': self.kategori.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
