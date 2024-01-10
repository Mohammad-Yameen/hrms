from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Employee
from .serializers import EmployeeSerializer



def index(request):
    return HttpResponse("welcome to Human Resource Management System")

@csrf_exempt
def create_employee(request):
    serializer = EmployeeSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Employee created"})

    return JsonResponse({"message": "Please provide valid data"}, status=403)


def get_employee(request, pk=None):
    if pk:
        #Retrieves a particular employee
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)
        
    #Retrieves a all employee
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)


        
            
            
    
