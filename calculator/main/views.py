from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, "main/home.html", {"name":"Calculator"})

def base(request):
    return render(request, "main/base.html")

def operation(request):

 result = ''
 if request.method == "GET":
  n1 =int(request.GET['num1']) 
 n2 = int(request.GET['num2'])
 opr = request.GET.get('opr')

 if opr == "+":
       result = n1 + n2
 elif opr == "-":
       result = n1 - n2
 elif opr == "*":
       result = n1 * n2
 elif opr == "/":
       result = n1 / n2
 else:
       result = " Invalid Operation..."
    
   
 name = "The computed result is:"
 calc  = "CALCULATOR"
 return render(request, "main/result.html", {"result": result,"name": name, "calc":calc})
    