from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Bahan
from resep.models import Resep
from kategori.models import Kategori

class BahanViewsetTestCase(APITestCase):
    def setUp(self):
        self.kategori = Kategori.objects.create(nama='Main Course')
        self.resep = Resep.objects.create(makanan='Nasi Goreng',kategori=self.kategori)
        self.bahan = Bahan.objects.create(komponen='Gula', resep=self.resep)

    def test_get_single_bahan(self):
        url = reverse('bahan-id', kwargs={'id': self.bahan.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_bahan(self):
        url = reverse('bahan')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_bahan(self):
        url = reverse('bahan')
        data = {'komponen': 'Garam', 'resep': self.resep.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_bahan(self):
        url = reverse('bahan-id', kwargs={'id': self.bahan.id})
        data = {'komponen': 'Gula Pasir', 'resep': self.resep.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_bahan(self):
        url = reverse('bahan-id', kwargs={'id': self.bahan.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
