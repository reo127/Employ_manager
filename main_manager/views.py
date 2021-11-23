from django.shortcuts import render, HttpResponse, redirect
from main_manager.models import Employe, ChildEmploye
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator



# Create your views here.

def home(request):
    employs = Employe.objects.all().order_by('timeStamp')
    employsCount = Employe.objects.all().count()

    paginator = Paginator(employs, 3) #Show 3 employe par 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    params = {'employs':page_obj,'user': request.user, 'employe_count': employsCount}
    return render(request, 'main/index.html', params)


def employs(request, employ_sno):
    employ = Employe.objects.get(sno=employ_sno)
    params = {'employ':employ}
    return render(request, 'main/employe_details.html', params)

@csrf_protect
def Eaditemploys(request, employ_name):  
    employ = Employe.objects.get(name=employ_name)
    params = {'employ':employ}
    return render(request, 'main/eaditEmploy.html', params)

@csrf_protect
def UpdateEmploys(request, employ_name):

    if request.method == "POST":          
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        sells = request.POST.get('sells')  
        print(name, date, email, phone, address, sells)

    ue = Employe.objects.get(name=employ_name)
    ue.name = name
    ue.date = date
    ue.email = email
    ue.phone = phone
    ue.address = address
    ue.sells = sells
    ue.save()
    messages.success(request, 'Employee Detail has been successfuly Updated')

    return redirect('/')

@csrf_protect
def AddEmploys(request):

    if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        sells = request.POST.get('sells')

        employs = Employe(name=name, date=date, email=email, phone=phone, address=address, sells=sells)
        employs.save()
        messages.success(request, 'Now Employee has been add successfuly')

    return redirect('/')


def employsDel(request, employ_sno):
    em = Employe(sno=employ_sno)
    em.delete()
    messages.success(request, 'Employee has been Deleted successfuly')
    return redirect('/')