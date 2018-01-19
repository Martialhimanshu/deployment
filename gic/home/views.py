from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer

# Create your views here.
def home(request):
    return HttpResponse('<h2>Welcome to GIC 2018 </h2>')

class employeeList(APIView):
	def get(self,*args):
		employees1 = employees.objects.all()
		serializer = employeesSerializer(employees1, many=True)
		return Response(serializer.data)


	def post(self):
		pass