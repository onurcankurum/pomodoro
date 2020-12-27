from django.forms import ModelForm
from chronometer.models import Timer
class SegmentForm(ModelForm):
    class Meta:
        model: Timer
        fields = ['status']