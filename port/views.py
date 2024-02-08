from django.shortcuts import render,redirect
from .models import profile

# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        pname = request.POST['pname']
        psurname = request.POST['psurname']
        pcontact = request.POST['pcontact']
        pemail = request.POST['pemail']
        pskills1 = request.POST['pskills1']
        pskills2 = request.POST['pskills2']
        pskills3 = request.POST['pskills3']
        pachieve = request.POST['pachieve']
        psummary = request.POST['psummary']
        pproject = request.POST['pproject']
        pexp = request.POST['pexp']
        pexpdetails = request.POST['pexpdetails']
        punv1 = request.POST['punv1']
        pco1 = request.POST['pco1']
        pcgpa1 = request.POST['pcgpa1']
        punv2 = request.POST['punv2']
        pco2 = request.POST['pco2']
        pcgpa2 = request.POST['pcgpa2']


        obj = profile.objects.create(pname=pname,psurname=psurname,pcontact=pcontact,pemail=pemail,pskills1=pskills1,pskills2=pskills2,pskills3=pskills3,pachieve=pachieve,psummary=psummary,pproject=pproject,pexp=pexp,pexpdetails=pexpdetails,punv1=punv1,pco1=pco1,pcgpa1=pcgpa1,punv2=punv2,pco2=pco2,pcgpa2=pcgpa2)
        obj.save()
        return redirect('/')
    return render(request,'index.html')
def retrieve(request):
    details = profile.objects.all()
    return render(request, 'index.html', {'details': details})