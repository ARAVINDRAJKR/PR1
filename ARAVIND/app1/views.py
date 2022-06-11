from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def hi(request):
    return HttpResponse("Hiii....")

def obj(request):
    product=Product.objects.all()
    return render(request,'product.html',{'pages':product})

def aabasoft(request):
    soft=Aabasoft.objects.all()
    return render(request,'aabasoft.html',{'aabasoft':soft})

def aravind(request):
    return render(request,'aravind.html',{'name':'aravind raj'})

def student(request):
    std=Student.objects.all()
    return render(request,'aravind.html',{'name':std})

def fl(request):
    f=Student.objects.exclude(age=22)
    return render(request,'aravind.html',{'filter':f})
def g(request):
    ge=Student.objects.get(id=2)
    return render(request,'aravind.html',{'name':ge})
def c(request):
    val=Student.objects.values('name')
    return render(request,'aravind.html',{'name':val})
def en(request):
    e=Student(name='deepa',age=25).save()
    c=Student.objects.all()
    return render(request,'aravind.html',{'name':c})
def od(request):
    s=Student.objects.filter(age="22")
    return render(request,'aravind.html',{'name':s})

def order(request):
    o=Student.objects.order_by("-name")
    return render(request,'aravind.html',{'name':o})
def updt(request):
    up =Student.objects.filter(name='ARAVIND')
    up.update(name='ARAVIND RAJ KR')
    up1=Student.objects.all()
    return render(request,'aravind.html',{'name1':up1})

def delete(request):
    delt=Student.objects.filter(name='CHINCHU').delete()
    delt1=Student.objects.all()
    return render(request,'aravind.html',{'name':delt1})

def mail(request):
    send_mail('subject','hai','athenaerudition1@gmail.com',['anchuannmani@gmail.com'],fail_silently=False)
    return HttpResponse("send")
def mail2(request):
    EmailMessage('subject','hai','athenaerudition1@gmail.com',to=['anchuannmani@gmail.com','kraravindraj2001@gmail.com']).send()
    return HttpResponse("send")
def mail3(request):
    mail=request.POST.get('email')
    subject=request.POST.get('sub')
    message=request.POST.get('mess')
    E= EmailMessage(subject,message,'athenaerudition1@gmail.com',[mail])
    E.content_subtype='html'
    file = open('ARAVIND.txt', 'r')
    E.attach('ARAVIND.txt',file.read(),'text/plain')
    E.send()
    return render(request,'mail.html')

def mail4(request):
    if request.method=='POST':
        email=request.POST.get('mail')
        sub=request.POST.get('sub')
        mess=request.POST.get('mess')
        f=request.FILES['file']
        E = EmailMessage(sub, mess, 'athenaerudition1@gmail.com', [email])
        E.content_subtype='html'
        E.attach(f.name,f.read(),f.content_type)
        E.send()
    return render(request,'mail.html')

def page(request):
    page = Pagnation.objects.all()
    spl=Paginator(page,2)
    pnumber=request.GET.get('page')
    page_content=spl.get_page(pnumber)
    return render(request,'page.html',{'pages':page_content})


























