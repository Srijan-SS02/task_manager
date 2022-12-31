from .models import Addtask
from django.forms import ModelForm

class Addform(ModelForm):
    class Meta:
        model = Addtask
        fields = '__all__'