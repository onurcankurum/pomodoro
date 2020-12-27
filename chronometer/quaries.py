from chronometer.models import Timer,Segment
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import timedelta
def query(user):
    timer = Timer.objects.get(user=user)
    p =Segment.objects.filter(timer=timer).order_by('-onfocus').values_list('onfocus').distinct()
    p=[''.join(a) for a in list(p)]
    return p

def totalTime(user):
    timerObject =Timer.objects.get(user=user)
    dersler=query(user=user)
    totalTime=list(map(lambda x :[timerObject.focusedItem(x).total_seconds(),x],dersler))
    return totalTime
def ranking():
    timerObjects =Timer.objects.order_by('-totalTime')
    liste=list()
    for i in timerObjects:
        user= User.objects.get(pk=i.user_id)
        a=timedelta(seconds=(int(i.totalTime)))
        liste.append([a,user.username])
        print(a,user.username)
        print("--------------------")
        print(i)
    return liste
def details(user):
    timer=Timer.objects.get(user=user)
    liste=list()
    liste= Segment.objects.filter(timer=timer).order_by('-onfocus').values_list('start_time').distinct()
    print(liste)
   
    
    



