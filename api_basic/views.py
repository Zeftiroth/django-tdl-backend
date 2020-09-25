from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Task
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
           return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializers = TaskSerializer(tasks, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = TaskSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetails(APIView):
    def get_object(self, id):
        breakpoint
        try:
            return Task.objects.get(id=id)

        except Task.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = self.get_object(id)
        serializers = TaskSerializer(task, data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])

# def task_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializers = TaskSerializer(tasks, many=True)
#         return Response(serializers.data)

#     elif request.method == 'POST':
#         # data =JSONParser().parse(request)
#         serializers = TaskSerializer(data=request.data)

#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
        
#     except Task.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializers = TaskSerializer(data=request.data)

#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

