from django.views.generic.edit import UpdateView
from django import forms
from .models import cs, CSApproved, Child, Parent, coilprocess, custprocess,CSPI,csqc
from django.forms.widgets import *
from django.forms import inlineformset_factory, widgets
from django.contrib.auth.models import User
# from django.contrib.auth import user
# from bootstrap_datepicker_plus import DatePickerInput

ChildrenFormset = inlineformset_factory(Parent, Child, fields=('name',))

class CSListEditForm(forms.ModelForm):
    
    class Meta:
        model = cs
        fields = '__all__'

        widgets = {
            
            'CVerDate': widgets.DateInput(attrs={'type': 'date'}),
            'IDate': widgets.DateInput(attrs={'type': 'date'}),
            'DLine': widgets.DateInput(attrs={'type': 'date'}),
        }

# class CSApprovedSimpleForm(forms.ModelForm):
#     class Meta:
#         model = cs
#         fields = '__all__'

class CSUpdateForm(forms.ModelForm):

    GotoSAKey = forms.CharField(label='Search SA No', required=False , widget=forms.TextInput(attrs={'placeholder': 'Search SA No'}))
    GotoCSKey = forms.CharField(label='Search CS No', required=False, widget=forms.TextInput(attrs={'placeholder': 'Search CS No'}))
    class Meta:
        
        model = cs
        fields = '__all__'

        widgets = {
            # 'CVerDateTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'CVerDate': widgets.DateInput(attrs={'type': 'date'}),
            'IDateTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # 'DLineDateTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'DLine': widgets.DateInput(attrs={'type': 'date'}),
            'Notes': widgets.Textarea(attrs={'rows': 5, 'cols': 40}),
            # 'NewInq': Select(CHOICES)
        }
        # if user.groups.filter(name='QC').exists():
        #     widgets = {
        #     'DLine': widgets.DateInput(attrs={'disabled': True}),
           
         
        # }
        CHOICES = (
            ('OK', 'OK'),
            ('NG', 'NG'),
            ('Remark', 'Remark'),
        )
    # def __init__(self, *args, **kwargs):
    #     super(CSUpdateForm, self).__init__(*args, **kwargs)       
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['readonly'] = True
    def __init__(self, *args, **kwargs):
        group_names = kwargs.pop('group_names', None)
        super().__init__(*args, **kwargs)

        # for field_name, field in self.fields.items():
            
        #     field.widget.attrs['readonly'] = True
        # self.fields['ImageSPEC'].widget.attrs['disabled'] = 'disabled'

        # if group_names:
        #     if 'QC' in group_names:
        #         for field_name, field in self.fields.items():
        #             field.widget.attrs['readonly'] = False


class CSQCForm(forms.ModelForm):

    class Meta:
        model = csqc
        fields = '__all__'
        widgets = {
            
            'Description': widgets.Textarea(attrs={'rows': 3, 'cols': 40}),
            'Notes': widgets.Textarea(attrs={'rows': 5, 'cols': 40}),
            # 'NewInq': Select(CHOICES)
        }
    
    # def __init__(self, *args, **kwargs):
    #     request = kwargs.pop(self.request, None)
    #     super(CSQCForm, self).__init__(*args, **kwargs)

    #     if request and request.user.is_authenticated:
    #         requested_user_name = request.user.username
    #         # Use the requested_user_name as needed in the form initialization
    #         self.fields['field_name1'].initial = requested_user_name

    # def __init__(self, *args, **kwargs):
    #     request = kwargs.pop('request', None)  # Retrieve the request object
    #     super(CSQCForm, self).__init__(*args, **kwargs)
        
    #     if request and request.user.groups.filter(name='QC').exists():  #
    #         self.fields['Description'].widget.attrs['readonly'] = 'readonly'

CSQCInlineFormSet = inlineformset_factory(
    cs,
    csqc,
    form=CSQCForm,
    extra=1,
    can_delete_extra=True,
    can_delete=True,
    max_num=1,
)




class CSPIForm(forms.ModelForm):

    class Meta:
        model = CSPI
        fields = '__all__'
    
    # def __init__(self, *args, **kwargs):
        
    #     super(CSPIForm, self).__init__(*args, **kwargs)
    #     if self.instance.id:
    #         self.fields['Leadtime'].widget.attrs['readonly'] = True
    #         self.fields['TPlug'].widget.attrs['readonly'] = True
        
        widgets = {
            
            'Notes': widgets.Textarea(attrs={'rows': 5, 'cols': 40}),
            # 'NewInq': Select(CHOICES)
        }

CSPIInlineFormSet = inlineformset_factory(
    cs,
    CSPI,
    form=CSPIForm,
    extra=1,
    can_delete_extra=True,
    can_delete=True,
    max_num=1,
)
 

class CSCustProForm(forms.ModelForm):

    class Meta:
        model = custprocess
        fields = '__all__'


CSCustProInlineFormSet = inlineformset_factory(
    cs,
    custprocess,
    form=CSCustProForm,
    extra=1,
    can_delete_extra=True,
    can_delete=True,
)


class CSCoilProForm(forms.ModelForm):

    class Meta:
        model = coilprocess
        fields = '__all__'


CSCoilProInlineFormSet = inlineformset_factory(
    cs,
    coilprocess,
    form=CSCoilProForm,
    extra=1,
    can_delete_extra=True,
    can_delete=True,
)

class CSApprovedForm(forms.ModelForm):

    class Meta:
        model = CSApproved
        fields = '__all__'

CSAprInlineFormSet = inlineformset_factory(
    cs, 
    CSApproved, 
    form=CSApprovedForm,
    extra=1,
    can_delete_extra=True,
    can_delete=True,
    )
    # inlineformset_factory(
    # parent_model, 
    # model, 
    # form=ModelForm, 
    # formset=BaseInlineFormSet, 
    # fk_name=None, 
    # fields=None, 
    # exclude=None, extra=3, can_order=False, can_delete=True, max_num=None, formfield_callback=None, widgets=None, validate_max=False, localized_fields=None, labels=None, help_texts=None, error_messages=None, min_num=None, validate_min=False, field_classes=None, absolute_max=None, can_delete_extra=True, renderer=None, edit_only=False)

ImageFormSet = inlineformset_factory(
    cs, CSApproved, form=CSApprovedForm, extra=1, can_delete=True, can_delete_extra=False
)
# MyInlineFormSet = inlineformset_factory(
#     cs, CSApproved, form=CSApprovedForm,
#     extra=1, can_delete=True, can_delete_extra=True
# )