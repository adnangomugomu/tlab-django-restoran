from django.shortcuts import render
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Bahan
from .serializers import BahanSerializers

class BahanViewset(GenericAPIView):
    def get(self, request, id=None):
        if id is not None:
            data = Bahan.objects.filter(id=id)
            if not data:
                return Response({
                    'message': 'Data tidak ditemukan',
                }, 204)
            serializer = BahanSerializers(data, many=True)
            return Response({
                'message': 'OK',
                'data': serializer.data,
            }, 200)
        else:
            data = Bahan.objects.all()
            serializer = BahanSerializers(data, many=True)
            return Response({
                'message': 'OK',
                'data': serializer.data,
            }, 200)

    def post(self, request):
        data=request.data
        data['created'] = timezone.now()
        serializer = BahanSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Data berhasil dibuat',
                'data': serializer.data,
            }, 201)
        return Response(serializer.errors, 400)

    def put(self, request, id):
        data = Bahan.objects.filter(id=id).first()
        if not data:
            return Response({
                'message': 'Data tidak ditemukan',
            }, 204)

        data_new=request.data
        data_new['updated'] = timezone.now()
        serializer = BahanSerializers(data, data=data_new)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Data berhasil diperbarui',
                'data': serializer.data,
            }, 200)
        return Response(serializer.errors, 400)

    def delete(self, request, id):
        data = Bahan.objects.filter(id=id).first()
        if not data:
            return Response({
                'message': 'Data tidak ditemukan',
            }, 204)

        data.soft_delete()
        return Response({
            'message': 'Data berhasil dihapus',
        }, 200)
