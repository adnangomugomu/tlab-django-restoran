from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Resep
from .serializers import ResepSerializers

class ResepViewset(GenericAPIView):
    def get(self, request, id=None):
        if id is not None:
            data = Resep.objects.filter(id=id)
            if not data:
                return Response({
                    'message': 'Data tidak ditemukan',
                }, 404)
            serializer = ResepSerializers(data, many=True)            
            return Response({
                'message': 'OK',
                'data': serializer.data,
            }, 200)
        else:
            data = Resep.objects.all()
            serializer = ResepSerializers(data, many=True)
            return Response({
                'message': 'OK',
                'data': serializer.data,
            }, 200)

    def post(self, request):
        data=request.data
        data['created'] = timezone.now()
        serializer = ResepSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Data berhasil dibuat',
                'data': serializer.data,
            }, 201)
        return Response(serializer.errors, 400)

    def put(self, request, id):
        data = Resep.objects.filter(id=id).first()
        if not data:
            return Response({
                'message': 'Data tidak ditemukan',
            }, 404)

        data_new=request.data
        data_new['updated'] = timezone.now()
        serializer = ResepSerializers(data, data=data_new)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Data berhasil diperbarui',
                'data': serializer.data,
            }, 200)
        return Response(serializer.errors, 400)

    def delete(self, request, id):
        data = Resep.objects.filter(id=id).first()
        if not data:
            return Response({
                'message': 'Data tidak ditemukan',
            }, 404)

        data.soft_delete()
        return Response({
            'message': 'Data berhasil dihapus',
        }, 204)

class CariResepViewset(GenericAPIView):

    def get(self,request):
        query = Q()
        nama = self.request.GET.get('nama')
        bahan = self.request.GET.get('bahan')
        kategori = self.request.GET.get('kategori')
        
        if nama: query &= Q(makanan__icontains=nama)        
        if bahan: query &= Q(bahan__komponen__icontains=bahan)
        if kategori: query &= Q(kategori__nama__icontains=kategori)
        
        data_filter = Resep.objects.filter(query)
        serializer = ResepSerializers(data_filter, many=True)            
        return Response({
            'message': 'OK',
            'data': serializer.data,
        }, status=200)