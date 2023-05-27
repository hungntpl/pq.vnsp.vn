from django import forms
import datetime
from cs.models import cs




class ReloadDatabase(forms.Form):
    confirm = forms.CharField(label='Confirm to reload', max_length=100)

class CSModelForm(forms.ModelForm):
    class Meta:
        model = cs
        fields = '__all__'
        # template_name = 'pq/home_cssa.html'

# iterable
CHART_CHOICES =(
    ("line", "line"),
    ("bar", "bar"),
    ("radar", "radar"),
    ("doughnut and pie", "d&p"),
    ("polar area", "polar area"),
    ("bubble", "bubble"),
    ("scatter", "scatter"),
)
class NameForm(forms.Form):
    pro_date = forms.DateField(label="Date", widget=forms.DateInput(attrs=dict(type='date')))
    chart_type = forms.ChoiceField(choices = CHART_CHOICES) 


