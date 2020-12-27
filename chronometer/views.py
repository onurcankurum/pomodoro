from django.shortcuts import render
from django.views.generic import View
from chronometer.models import Timer,TimerResumeException
from django.http import JsonResponse, Http404
class TimerView(View):

    def get_json_response(self):
        if not hasattr(self, 'timer') or not self.timer:
            raise Http404
        self.timer.totalTime=self.timer.duration().total_seconds()
        self.timer.save()
        return {
               'status': self.timer.status,
               'duration': self.timer.duration().total_seconds()
              }

    def post(self, request, pk=None,args='seçilmedi'):
        self.timer= Timer.objects.get(user=request.user)
        self.action(request, pk,args)
        return self.get_json_response()

    def get_timer(self, pk):
        try:
            return Timer.objects.get(pk=pk)
        except:
            pass
    def action(self, request, pk):
        raise NotImplementedError('{} has to define an action method.'.format(self.__class__))

class Start(TimerView):

    def action(self, request, pk,args):
        
        self.timer.start(args)
    
class Pause(TimerView):

    def action(self, request, pk,args):
        self.timer.pause(args)
            
class Resume(TimerView):

    def action(self, request, pk,args):
        try:
            self.timer.resume(args)
        except TimerResumeException:
            pass
        
class Stop(TimerView):

    def action(self, request, pk,args):
        self.timer.stop(args)