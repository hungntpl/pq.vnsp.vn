from django import forms
from .models import sa
from django.forms import inlineformset_factory, widgets

from django.core.mail import send_mail
from django.urls import reverse
from django.utils import timezone
from set.models import EmailReport

class SASearchForm(forms.Form):

    SANo = forms.CharField(label='SA No', required=False)
    CustID = forms.CharField(label='Cust ID', required=False)
    Model = forms.CharField(label='Model', required=False)
    PipeStd = forms.CharField(label='Pipe Std', required=False)

    OD = forms.CharField(label='OD', required=False)
    ID = forms.CharField(label='ID', required=False)
    WT = forms.CharField(label='WT', required=False)
    L = forms.CharField(label='L', required=False)

class SAUpdateForm(forms.ModelForm):

    GotoSAKey = forms.CharField(label='Search SA No', required=False , widget=forms.TextInput(attrs={'placeholder': 'Search SA No'}))
    GotoCSKey = forms.CharField(label='Search CS No', required=False, widget=forms.TextInput(attrs={'placeholder': 'Search CS No'}))
    class Meta:
        
        model = sa
        fields = '__all__'

        widgets = {
            'CVerDate': widgets.DateInput(attrs={'type': 'date'}),
            'IDate': widgets.DateInput(attrs={'type': 'date'}),
            'DLine': widgets.DateInput(attrs={'type': 'date'}),
            
            'NDI': widgets.Textarea(attrs={'rows': 6, 'cols': 40}),
            'Others': widgets.Textarea(attrs={'rows': 6, 'cols': 40}),
            'Marking': widgets.Textarea(attrs={'rows': 6, 'cols': 40}),
            'SurfCondE': widgets.Textarea(attrs={'rows': 6, 'cols': 40}),
            'SurfCondV': widgets.Textarea(attrs={'rows': 6, 'cols': 40}),
        }

    def __init__(self, *args, **kwargs):
        group_names = kwargs.pop('group_names', None)
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Do something with each field
            # print(field_name)
            # print(field.label)
            # print(field.widget)
            # ...
            # field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
        self.fields['QAManJudgment'].widget.attrs['style'] = 'pointer-events: none;'
        self.fields['QCManJudgment'].widget.attrs['style'] = 'pointer-events: none;'
        self.fields['DGDJudgment'].widget.attrs['style'] = 'pointer-events: none;'
        self.fields['CustID'].widget.attrs['style'] = 'pointer-events: none;'
        self.fields['PipeGrade'].widget.attrs['style'] = 'pointer-events: none;'

        self.fields['ImageSPEC'].widget.attrs['disabled'] = 'disabled'
        self.fields['SAApp'].widget.attrs['disabled'] = 'disabled'
        
        if group_names:
            if 'QC' in group_names:
                for field_name, field in self.fields.items():
                    field.widget.attrs['readonly'] = False
                    # self.fields['ImageSPEC'].widget.attrs['style'] =''
                    # self.fields['SAApp'].widget.attrs['style'] =''
                self.fields['ImageSPEC'].widget.attrs.pop('disabled', None)
                self.fields['SAApp'].widget.attrs.pop('disabled', None)
                del self.fields['CustID'].widget.attrs['style']
                del self.fields['PipeGrade'].widget.attrs['style']
            if 'QCMan' in group_names:
                del self.fields['QCManJudgment'].widget.attrs['style']
            if 'QAMan' in group_names:
                del self.fields['QAManJudgment'].widget.attrs['style']
            if 'DGD' in group_names:
                del self.fields['DGDJudgment'].widget.attrs['style'] 
                # self.fields['OD'].widget.attrs['disabled'] = True
            
                
                # for field_name, field in self.fields.items():
                #     field.widget.attrs['disabled'] = False
                # self.fields['SANo'].widget.attrs['disabled'] = False
                # self.fields['IDate'].widget.attrs['disabled'] = False
                # self.fields['Marking'].widget.attrs['disabled'] = False
                # self.fields['NDI'].widget.attrs['disabled'] = False
                # self.fields['Others'].widget.attrs['disabled'] = False
                # self.fields['SurfCondE'].widget.attrs['disabled'] = False
                # self.fields['SurfCondV'].widget.attrs['disabled'] = False
                # self.fields['ImageSPEC'].widget.attrs['disabled'] = False

    # def clean_my_field(self):
    #     old_value = self.initial.get('SAApp')
    #     new_value = self.cleaned_data.get('SAApp')

    #     if old_value and new_value and old_value != new_value:
    #         # Field value has changed
    #         # Perform additional validation or actions here
            
           
    #         url = reverse('sa-update', kwargs={'pk': self.cleaned_data.get('SANo')})
    #         self.object.AppDate = timezone.now()
    #         subject = 'SPEC Agreement has been approved ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    #         message = 'SPEC Agreement No: ' + self.cleaned_data.get('SANo') + ' is approved: ' + self.request.build_absolute_uri(url)
    #         sender = 'support@vnsp.vn'
    #         recipients = EmailReport.objects.values_list('ReciEmail', flat=True)
    #         send_mail(subject, message, sender, recipients)

    #     return new_value