from django.shortcuts import render,get_object_or_404
from models import UniversityModel
from .serializer import UniversitySer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class CreateuniversityView(APIView):
    def post(self,request):
        if request.user != 'AnonymousUser':
            if request.user.roles == 3:

                serializer = UniversitySer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'you can not add'})
        return Response({'you can not add'})
    
class ListuniversityView(APIView):
    def get(self,request):
        if request.user != 'AnonymousUser':
            all = UniversityModel.objects.all()
            serializer = UniversitySer(all,many= True)
            return Response(serializer.data)
        return Response('please log in ')
    
class UpdateuniversityView(APIView):
    def patch(self,request,*args,**kwargs):
        if request.user != 'AnonymousUser':
            if request.user.roles == 3:
                info = get_object_or_404(UniversityModel,id=kwargs['university_id'])
                serializer = UniversitySer(info,data=request.data,partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response('you cannot these')
        return Response('you cannot these')
    
    
    