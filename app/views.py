from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

def display_dept(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html')


def display_emp(request):
    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'display_emp.html')


def display_salgrade(request):
    QLSO=SalGrade.objects.all()
    d={'salgrade':QLSO}
    return render(request,'display_salgrade.html')


def display_bonus(request):
    QLBO=Bonus.objects.all()
    d={'bonus':QLBO}
    return render(request,'display_bonus.html')


def insert_dept(request):
    dno=int(input('enter dept number'))
    dn=input('enter dept name')
    l=input('enter location')
    NDO=Dept.objects.get_or_create(deptno=dno,deptname=dn,location=l)[0]
    NDO.save()
    return render(request,'display_dept.html')


def insert_emp(request):
    dno=int(input('enter dept number'))
    eno=int(input('enter empnumber'))
    en=input('enter name')
    j=input('enter job')
    mgr=int(input('enter mgr'))
    hd=input('enter hiredate')
    s=int(input('enter sal'))
    c=input('enter comm')
    DO=Dept.objects.get(deptno=dno)
    NEO=Emp.objects.get_or_create(deptno=DO,empno=eno,ename=en,job=j,mgr=mgr,hiredate=hd,sal=s,comm=c)[0]
    NEO.save()
    return render(request,'display_emp.html')


def insert_salgrade(request):
    gd=int(input('enter grade'))
    ls=int(input('enter lowsal'))
    hs=int(input('enter highsal'))
    NSO=SalGrade.objects.get_or_create(grade=gd,lowsal=ls,highsal=hs)[0]
    NSO.save()
    return render(request,'display_salgrade.html')


def insert_bonus(request):
    gd=int(input('enter grade'))
    s=int(input('enter sal'))
    NBO=Bonus.objects.get_or_create(grade=gd,sal=s)[0]
    NBO.save()
    return render(request,'display_bonus.html')