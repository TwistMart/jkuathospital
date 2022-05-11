from django.shortcuts import render,redirect

# my imports
from django.contrib.auth.decorators import login_required
# used to not use back button after logout to  access the information in the system
from django.views.decorators.cache import cache_control 
from patient.models import Patient
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# functions to render the frontend page

def Frontend(request):
    return render(request, "frontend.html")

#-----------Backend section------------|

# functions to render the backend page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def Backend(request):

    if 'q' in request.GET:
        q=request.GET['q']
        all_patient_list=Patient.objects.filter(
            Q(name__icontains=q)| 
            Q(phone__icontains=q)|
            Q(email__icontains=q)|
            Q(age__icontains=q) | 
            Q(gender__icontains=q)).order_by('-created_at')

    else:        
        all_patient_list=Patient.objects.all().order_by('-created_at')
    paginator= Paginator(all_patient_list, 5)
    page=request.GET.get('page')    
    all_patient_list=paginator.get_page(page)        
            
    return render(request, "backend.html", {"patients": all_patient_list})

#function to insert new patient
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def Add_Patient(request):
    if request.method=="POST":
        patient= Patient(
               
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],            
            age=request.POST['age'],
            gender=request.POST['gender'],
            note=request.POST['note']

        )
        patient.save()
        messages.success(request, "patient added successfully")
        return redirect('/backend')
    return render(request,'add.html')

#function to access patients individually
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def patient(request, pk):    
    patient= Patient.objects.get(id=pk)
    if patient !=None: 
        return render(request, "edit.html", {"patient": patient})
 
        
    
# function to edit patient
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_patient(request):
    if request.method=='POST':       

        patient= Patient.objects.get(id=request.POST.get('id')) 
        if patient!=None:
            patient.name=request.POST.get('name')
            patient.phone=request.POST.get('phone')
            patient.email=request.POST.get('email')
            patient.gender=request.POST.get('gender')
            patient.age=request.POST.get('age')
            patient.note=request.POST.get('note')
            patient.save()

            messages.success(request, "patient updated successfully")
            return redirect('/backend' )

#function to delete
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_patient(request, pk):
    patient=Patient.objects.get(id=pk)
    patient.delete()
    messages.success(request, "patient deleted successfully")
    return redirect('/backend' )
    

  





    
    
     
