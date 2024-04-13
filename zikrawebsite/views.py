# Create your views here.
from django. http import *
from django. shortcuts import render,redirect
from .urls import *
from .models import marquee,performance,programs,principal_message
from django.contrib import admin
from marquee.models import *
from performance.models import *
from programs.models import *
from principal_message.models import *
from diary.models import *




def home(request):
    news=marquee.objects.all()
    notices=notice_board.objects.all()
    sliderimage=image_slider.objects.all()
    message=principal_message.objects.all()
   # news=marquee.objects.filter()
   # print(notices)
   
       
   #
    return render (request,"index.html",{'new':news,'noticee':notices, 'slider_img':sliderimage, 'message':message,})

def program(request):
    #news=marquee.objects.all()
    #notices=notice_board.objects.all()
    return render (request,"program.html")


#def result(request):
    
       #return render (request, "contact.html", {'student':result})
  





       #result=performance.objects.all().values() 
       #result=performance.objects.get()
   # print(result)
   #return render (request, "contact.html",result(request))
def contact(request):
    result= performance.objects.all()
    student={
        
      }
    if request.method=='GET':
        st=request.GET.get('rollno')
        if st!=None:
            result=performance.objects.filter(rollno=st, fee_status=True)
            student={
            'student':result
              }
   
    
    
    
    
    #if request.GET:
     #  name = request.GET['name'];
      # rollno = request.GET['rollno'];
      # print(name);
       #print(rollno);
    #print(student)
    #print(result)    
    return render (request, "contact.html",student)
    #if request.GET:
     #  name = request.GET['name'];
      # rollno = request.GET['rollno'];
      # print(name);
      # print(rollno);
      # result=performance.objects.get(name=name)
      # return render (request, "contact.html", {'student':result})
    
        #if request.method=='POST':
       # result = request.POST.get('rollno')
    #result=performance.objects.all()
   # result={
    
    #   'name': name,
     #  'rollno': rollno,
     #  'grade':grade,
     #  'english':english,
     #  'urdu':urdu,
     #  'sst':sst,
     #  'math':math,
     #  'science':science,
     #  'computer':computer,
     #  'islamiyat':islamiyat,
     #  'kashmiri':kashmiri,
     #  'conduct':conduct,
     # }
   # rollhtml=request.GET.get('rollno')
   # if result.rollno == rollhtml:
    #    final=performance.objects.get('rollno')
    

    #result=performance.objects.get('rollno')
    




    #def performanceDetail(request,id):
       # result=performance.objects.all()
       # return render (request, "contact.html", {'result' : result})



def program(request):
    proram_videos= programs.objects.all()
    
    return render (request, "program.html",{'videos':proram_videos,})



#def principal_message(request):
 #   message=principal_message.objects.all()
  #  print("message")
   # return render(request, "index.html",{'mess':message,})

def downloads(request):
    
    #student={
        
     # }
    if request.method=='GET':
        st=request.GET.get('rollno')
        grade=request.GET.get('class')
        result= diary_fees.objects.filter(rollno=st,grade=grade,fee_status=True)
        check={
          'check':result
        }
        student={
                  
               }
        if st!=None and len(result)!=0:
          if grade=='nursary':
            result=diary_nursary.objects.all()
            student={
               'student':result
               }
          elif grade=='lkg':
            result=diary_lkg.objects.all()
            student={
               'student':result
               }
          elif grade=='ukg':
            result=diary_ukg.objects.all()
            student={
               'student':result
               }
            student={
               'student':result
               }
          elif grade=='first':
            result=diary_first.objects.all()
            student={
               'student':result
               }
          elif grade=='second':
            result=diary_second.objects.all()
            student={
               'student':result
               }
          elif grade=='third':
             result=diary_third.objects.all()
             student={
               'student':result
               }
          elif grade=='fourth':
             result=diary_fourth.objects.all()
             student={
               'student':result
               }
   
    
    
    
    
    #if request.GET:
     #  name = request.GET['name'];
      # rollno = request.GET['rollno'];
      # print(name);
       #print(rollno);
    #print(student)
    #print(result)    
    
    return render (request, "downloads.html",student)