from django.contrib.auth.models import User
import django_filters
# from django_filters import ModelChoiceFilter
from .models import cs, coilprocess
from set.models import coilgrade, pipegrade, cust



class CPFilter(django_filters.FilterSet):
    
    SANo = django_filters.CharFilter(label='SANo',field_name='CSNo_id__SANo',lookup_expr='icontains') 
    CustID = django_filters.CharFilter(label='Cust. ID',field_name='CSNo_id__CustID_id__CustID',lookup_expr='icontains') 

    CustFullname = django_filters.ModelChoiceFilter(queryset=cust.objects.all(),label='Cust. Fullname',field_name='CSNo_id__CustID_id__Fullname',lookup_expr='icontains')
    
    OD = django_filters.CharFilter(label='OD',field_name='CSNo_id__OD',lookup_expr='icontains') 
    ID = django_filters.CharFilter(label='ID',field_name='CSNo_id__ID',lookup_expr='icontains') 
    WT = django_filters.CharFilter(label='WT',field_name='CSNo_id__WT',lookup_expr='icontains') 
    L = django_filters.CharFilter(label='L',field_name='CSNo_id__L',lookup_expr='icontains') 

    AdjOD = django_filters.CharFilter(label='Tol. OD',field_name='CSNo_id__csqc__AdjOD',lookup_expr='icontains') 
    AdjID = django_filters.CharFilter(label='Tol. ID',field_name='CSNo_id__csqc__AdjID',lookup_expr='icontains') 
    AdjWT = django_filters.CharFilter(label='Tol. WT',field_name='CSNo_id__csqc__AdjWT',lookup_expr='icontains') 
    AdjL = django_filters.CharFilter(label='Tol. L',field_name='CSNo_id__csqc__AdjL',lookup_expr='icontains') 

    InBead = django_filters.CharFilter(label='In Bead',field_name='CSNo_id__InBead',lookup_expr='icontains') 
    SurfLevel = django_filters.CharFilter(label='Surface Level',field_name='CSNo_id__SurfLevel',lookup_expr='icontains') 
    SurfTreat = django_filters.CharFilter(label='Surface Treat',field_name='CSNo_id__SurfTreat',lookup_expr='icontains')
    PipeGrade = django_filters.CharFilter(label='Pipe Grade',field_name='CSNo_id__PipeGrade_id__PipeGrade',lookup_expr='icontains')
    PipeGradeCmbBox = django_filters.ModelChoiceFilter(queryset=pipegrade.objects.all(),label='Pipe Grade',field_name='CSNo_id__PipeGrade_id__PipeGrade',lookup_expr='icontains')

    CGradeID = django_filters.CharFilter(label='Coil Grade',field_name='CGrade_id__CoilGrade',lookup_expr='icontains') 

    Model = django_filters.CharFilter(label='Model',field_name='CSNo_id__Model',lookup_expr='icontains')
    PartNo = django_filters.CharFilter(label='PartNo',field_name='CSNo_id__PartNo',lookup_expr='icontains')
    PartName = django_filters.CharFilter(label='PartName',field_name='CSNo_id__PartName',lookup_expr='icontains')
    PartMaker = django_filters.CharFilter(label='PartMaker',field_name='CSNo_id__PartMaker',lookup_expr='icontains')
    

    ASManNote = django_filters.CharFilter(label='ASManNote',field_name='CSNo_id__ASManNote',lookup_expr='icontains')
    PCManNote = django_filters.CharFilter(label='PCManNote',field_name='CSNo_id__PCManNote',lookup_expr='icontains')
    QCManNote = django_filters.CharFilter(label='QCManNote',field_name='CSNo_id__QCManNote',lookup_expr='icontains')
    QAManNote = django_filters.CharFilter(label='QAManNote',field_name='CSNo_id__QAManNote',lookup_expr='icontains')
    PIManNote = django_filters.CharFilter(label='PIManNote',field_name='CSNo_id__PIManNote',lookup_expr='icontains')
    PRManNote = django_filters.CharFilter(label='PRManNote',field_name='CSNo_id__PRManNotel',lookup_expr='icontains')
    DGDNote = django_filters.CharFilter(label='DGDNote',field_name='CSNo_id__DGDNote',lookup_expr='icontains')


    # CMaker = django_filters.CharFilter(label='Coil Maker',field_name='CMaker',lookup_expr='icontains') 
    # CGrade = django_filters.CharFilter(label='Coil Grade',field_name='CGrade',lookup_expr='icontains') 
    # CWTOrder = django_filters.CharFilter(label='Coil WT',field_name='CSNo_id__CWTOrder',lookup_expr='icontains') 
    # SCoilWidth = django_filters.CharFilter(label='Coil Width',field_name='CSNo_id__SCoilWidth',lookup_expr='icontains') 

    

    class Meta:
        model = coilprocess
        fields = '__all__'
        
class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class CSFilter(django_filters.FilterSet):
    
    CSNo = django_filters.CharFilter(label='CS No', lookup_expr='icontains')
    SANo = django_filters.CharFilter(label='SA No', lookup_expr='icontains')
    CustID_id = django_filters.CharFilter(label='Cust. Name', lookup_expr='icontains')  # Filter by fullname
    CustIDV = django_filters.CharFilter(label='Cust. ID',field_name='CustID_id__CustID',lookup_expr='icontains') # Filter by ID
    # CustID_id = django_filters.CharFilter(label='Cust. Fname',field_name='CustID_id',lookup_expr='icontains')
    
    PipeGradeV = django_filters.CharFilter(label='Pipe Grade',field_name='PipeGrade_id__PipeGrade', lookup_expr='icontains')
    PipeGrade_id = django_filters.CharFilter(label='Pipe Grade',field_name='PipeGrade_id__PipeGrade', lookup_expr='icontains')
    
    # CoilGrade = django_filters.CharFilter(label='Coil Grade',field_name='coilprocess__CGrade_id__CoilGrade', lookup_expr='icontains')
    # CoilMaker = django_filters.CharFilter(label='Coil Maker', lookup_expr='icontains')
    CoilMaker = django_filters.CharFilter(label='Coil Maker',field_name='coilprocess__CMaker',lookup_expr='icontains')
    
    
    CWTOrder = django_filters.CharFilter(label='Coil WT',field_name='coilprocess__CWTOrder',lookup_expr='icontains')
    SCoilWidth = django_filters.CharFilter(label='Coil Width',field_name='coilprocess__SCoilWidth',lookup_expr='icontains')
    
    OD = django_filters.CharFilter(label='OD', lookup_expr='icontains')
    ID = django_filters.CharFilter(label='ID',lookup_expr='icontains')
    WT = django_filters.CharFilter(label='WT',lookup_expr='icontains')
    L = django_filters.CharFilter(label='L',lookup_expr='icontains')

    AdjOD = django_filters.CharFilter(label='Tol. OD', lookup_expr='icontains')
    AdjID = django_filters.CharFilter(label='Tol. ID',lookup_expr='icontains')
    AdjWT = django_filters.CharFilter(label='Tol. WT',lookup_expr='icontains')
    AdjL = django_filters.CharFilter(label='Tol. L',lookup_expr='icontains')

    Straight = django_filters.CharFilter(label='Straight', lookup_expr='icontains')
    Flaring = django_filters.CharFilter(label='Flaring',lookup_expr='icontains')
    Flattening90 = django_filters.CharFilter(label='Flattening 90',lookup_expr='icontains')
    SurfTreat = django_filters.CharFilter(label='Surface Treat',lookup_expr='icontains')

    PartNo = django_filters.CharFilter(label='PartNo',lookup_expr='icontains')
    PartName = django_filters.CharFilter(label='PartName',lookup_expr='icontains')
    PartMaker = django_filters.CharFilter(label='PartMaker',lookup_expr='icontains')
    Model = django_filters.CharFilter(label='Model',lookup_expr='icontains')

    CProcess = django_filters.CharFilter(label='Process',lookup_expr='icontains')
    InBead = django_filters.CharFilter(label='InBead',lookup_expr='icontains')
    SurfLevel_id = django_filters.CharFilter(label='Surface Level',lookup_expr='icontains')

    ASManNote = django_filters.CharFilter(label='AS Note',lookup_expr='icontains')
    PIManNote = django_filters.CharFilter(label='PI Note',lookup_expr='icontains')
    QAManNote = django_filters.CharFilter(label='QA Note',lookup_expr='icontains')
    QCManNote = django_filters.CharFilter(label='QC Note',lookup_expr='icontains')

    PCManNote = django_filters.CharFilter(label='PC Note',lookup_expr='icontains')
    DGDNote = django_filters.CharFilter(label='DGD Note',lookup_expr='icontains')
    PRManNote = django_filters.CharFilter(label='PR Note',lookup_expr='icontains')
    ImageSPEC = django_filters.CharFilter(field_name='ImageSPEC', lookup_expr='icontains')
    # CSAp = django_filters.CharFilter(field_name='CSAp', lookup_expr='icontains')

    
    # testname = django_filters.CharFilter(field_name='testname_id__testname',lookup_expr='icontains')
    CustSignT = django_filters.CharFilter(label='Cust ST',field_name='CustID_id__SignT',lookup_expr='icontains')
    
    CoilGrade = django_filters.CharFilter(label='Coil Grade',field_name='coilprocess__CGrade_id__CoilGrade',lookup_expr='icontains')
    
    # CoilGrade = django_filters.ModelChoiceFilter(queryset=coilgrade.objects.all(), label='Coil Grade',field_name='coilprocess__CGrade_id__CoilGrade',lookup_expr='icontains')
    # CoilGrade = django_filters.ModelChoiceFilter(queryset=coilgrade.objects.all(), label='Coil Grade',field_name='coilprocess__CGrade_id__CoilGrade',lookup_expr='icontains')

    # related_model_field = django_filters.CharFilter(field_name='related_model__field_name',lookup_expr='icontains')
    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.filters['CoilGrade'].queryset = cs.objects.all()

    class Meta:
        model = cs
        fields = '__all__'
        
        # exclude = {
        #     "CSAp": None,
        # }

        # fields = ['CSNo','SANo','CustID','PipeGrade','CoilMaker',
        #           'OD','ID','WT','L',
        #           'PartNo','PartName','PartMaker','Model',
        #           'CProcess','InBead','SurfLevel','SurfTreat',
        #           'ASManNote','PIManNote','QAManNote','QCManNote',
        #           'PCManNote','DGDNote','PRManNote','CustSignT','CoilGrade']
        
        
        




