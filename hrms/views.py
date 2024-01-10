from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Employee
from .serializers import EmployeeSerializer


class HomeView(View):
    
    def get(self, request):
        return render(request, "home.html")


class EmployeeView(View):
    
    def get(self, request, pk=None):
        """Retrieve data of employee"""
        if pk:
            #Retrieves a particular employee
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee)
            return render()
            return JsonResponse(serializer.data)
        
        #Retrieves a all employee
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    @csrf_exempt
    def post(self, request):
        serializer = EmployeeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect("home")

        print(serializer._errors)
        return JsonResponse({"message": "Please provide valid data"}, status=403)
        
        


class EmployeeFormView(View):
    
    def get(self, request):
        return render(request, "employeeform.html")
        
            
            
    
