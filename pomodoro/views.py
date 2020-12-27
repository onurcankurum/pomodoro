import datetime
from django.shortcuts import render
from django.http import HttpResponse
from chronometer.models import Timer
from django.views.generic import View
from chronometer.views import Start,Resume,Pause,Stop,TimerView
from .forms import SegmentForm
import json
import time
from chronometer.quaries import query,totalTime,ranking,details
from django.core.exceptions import ObjectDoesNotExist
import json
class Hometest(View):
    start =Start()
    pause=Pause()
    resume=Resume()
    stop=Stop()


    def lazim(self,request,choosen):
        try:
            self.timer = self.pause.post(request,request.user.pk,choosen)#devamm eden segment varsa durduralım
        except ObjectDoesNotExist : #kullanıcının timer nesnesi yoksa oluşturalım
            newUser = Timer(user=request.user,status='stopped') 
            newUser.save()
            self.timer = self.start.post(request,request.user.pk,choosen) #kullanıcı oluşturmadan girince hata veriyo çünkü user nesnesi boş
            self.timer = self.pause.post(request,request.user.pk,choosen)


    def get(self,request):
        
        context=self.loadata(self.request)
        print(context)
        return render(request,'hometest.html',context)

    def post(self,request):
        
        context=self.loadata(self.request)
        if 'add' in request.POST:
            self.timer = self.pause.post(request,request.user.pk,dict(request.POST)['add'][0])
            self.timer = self.resume.post(request,request.user.pk,dict(request.POST)['add'][0])#3 ü birden çalışıyo buna bir bak biara 
            self.timer = self.pause.post(request,request.user.pk,dict(request.POST)['add'][0])
            return render(request,'hometest.html',context)
            
        if 'start' in request.POST:
            self.lazim(request,dict(request.POST)['select'][0])
            self.timer = self.resume.post(request,request.user.pk,dict(request.POST)['select'][0])
        if 'stop' in request.POST:
            self.lazim(request,dict(request.POST)['select'][0])
            self.timer = self.pause.post(request,request.user.pk,dict(request.POST)['select'][0])
        
            
        
        return render(request,'hometest.html',context)

    def loadata(self,request):
        if (request.user.is_authenticated):
            try: 
                context={"dersler":query(request.user)}
            except ObjectDoesNotExist:
                self.lazim(request,'seçilmedi')
                context={"dersler":query(request.user)}
            print(context)
        else:
            print("giriş başarısız")
            context={"dersler":['derslerinizi','görmek için','giriş yapın']}
        return context

    def newTask(self,request):
        pass
    def isNew(self,user):
        timer = Timer.objects.get(user=suser)
    
        

        
class Statistics(View):
    context={}
    def post(self,request):
        return render(request,'statistics.html',{})
    def get(self,request):
        print(totalTime(request.user))
        self.context['ranking']=ranking()
        liste=totalTime(request.user)
        details = ','.join([str(i[0]) for i in liste])
        details2 = ','.join([str(i[1]) for i in liste])

        self.context['details']=details
        self.context['details2']=details2
        print(self.context)
        return render(request,'statistics.html',self.context)


def home(request):



    
    start =Start()
    pause=Pause()
    resume=Resume()
    stop=Stop()

    if (request.user.is_authenticated):
        print("giriş başarılı") 
        context={"dersler":query(request.user.pk)}


    if(request.method!='GET'):#get ile geldiysek sayfaya yeni giriş yapıyoruz ve ders seçilmediği için carlist boş olacak bu yüzdenbu blok çalışmayacak
        if(dict(request.POST)['add-task'][0]!=''):
            choosen=dict(request.POST)['add-task'][0]
        else:
            choosen=dict(request.POST)['carlist'][0]

        try:
            timer = pause.post(request,request.user.pk,choosen)#devamm eden segment varsa durduralım
        except AttributeError: #kullanıcının timer nesnesi yoksa oluşturalım
            newUser = Timer(user=request.user,status='stopped') 
            newUser.save()
            timer = start.post(request,request.user.pk,choosen) #kullanıcı oluşturmadan girince hata veriyo çünkü user nesnesi boş
            timer = pause.post(request,request.user.pk,choosen)
        timer['current']='start' 

        try:
            if(dict(request.POST)['current'][0]=='pause'):
            
                timer=pause.post(request,request.user.pk,choosen)
                timer['current']='start'

            else:
                timer = resume.post(request,request.user.pk,choosen)
                timer['current']='pause'
        except KeyError:
            timer['current']='start'
        timer['min']=time.gmtime(timer['duration']).tm_min
        timer['sec']=time.gmtime(timer['duration']).tm_sec
        #timer['selected']=dict(request.POST)['carlist'][0]
        timer['allders']=totalTime(request.user.pk)
        timer['focused']=query(request.user.pk)
    
        
    else:
        timer={"focused":query(request.user.pk)}
        timer['ranks']=ranking()
        timer['username']=request.user.username
    timer['username']=request.user.username    
    timer['ranks']=ranking()    
    
    return render(request,'home.html',timer)



    
