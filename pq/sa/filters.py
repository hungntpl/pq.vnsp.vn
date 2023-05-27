from django.contrib.auth.models import User
import django_filters
from .models import sa
from set.models import coilgrade, pipegrade



class SAFilter(django_filters.FilterSet):
    
    # CSNo = django_filters.CharFilter(label='CS No', lookup_expr='icontains')
    SANo = django_filters.CharFilter(label='SA No', lookup_expr='icontains')
    # CustID_id = django_filters.CharFilter(label='Customer', lookup_expr='icontains')
    CustID_id = django_filters.CharFilter(label='Cust. Name', lookup_expr='icontains')  # Filter by fullname
    CustIDV = django_filters.CharFilter(label='Cust. ID',field_name='CustID_id__CustID',lookup_expr='icontains') # Filter by ID
    
    # PipeGrade = django_filters.CharFilter(label='Pipe Grade',field_name='PipeGrade_id__PipeGrade', lookup_expr='icontains')

    PipeGradeV = django_filters.CharFilter(label='Pipe Grade',field_name='PipeGrade_id__PipeGrade', lookup_expr='icontains')
    PipeGrade_id = django_filters.CharFilter(label='Pipe Grade',field_name='PipeGrade_id__PipeGrade', lookup_expr='icontains')
    # CoilGrade = django_filters.CharFilter(label='Coil Grade',field_name='coilprocess__CGrade_id__CoilGrade', lookup_expr='icontains')
    CoilMaker = django_filters.CharFilter(label='Coil Maker', lookup_expr='icontains')
    
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
    SurfLevel = django_filters.CharFilter(label='Surface Level',lookup_expr='icontains')

    ASManNote = django_filters.CharFilter(label='AS Note',lookup_expr='icontains')
    PIManNote = django_filters.CharFilter(label='PI Note',lookup_expr='icontains')
    QAManNote = django_filters.CharFilter(label='QA Note',lookup_expr='icontains')
    QCManNote = django_filters.CharFilter(label='QC Note',lookup_expr='icontains')

    PCManNote = django_filters.CharFilter(label='PC Note',lookup_expr='icontains')
    DGDNote = django_filters.CharFilter(label='DGD Note',lookup_expr='icontains')
    PRManNote = django_filters.CharFilter(label='PR Note',lookup_expr='icontains')
    ImageSPEC = django_filters.CharFilter(field_name='ImageSPEC', lookup_expr='icontains')
    # testname = django_filters.CharFilter(field_name='testname_id__testname',lookup_expr='icontains')
    CustSignT = django_filters.CharFilter(label='Cust ST',field_name='CustID_id__SignT',lookup_expr='icontains')
    
    # CoilGrade = django_filters.CharFilter(label='Coil Grade',field_name='coilprocess__CGrade_id__CoilGrade',lookup_expr='icontains')
    
    
    ChC = django_filters.CharFilter(label='ChC',lookup_expr='icontains')
    ChSi = django_filters.CharFilter(label='ChSi',lookup_expr='icontains')
    ChMn = django_filters.CharFilter(label='ChMn',lookup_expr='icontains')
    ChP = django_filters.CharFilter(label='ChP',lookup_expr='icontains')
    ChS = django_filters.CharFilter(label='ChS',lookup_expr='icontains')

    ChAL = django_filters.CharFilter(label='ChAL',lookup_expr='icontains')
    ChNi = django_filters.CharFilter(label='ChNi',lookup_expr='icontains')
    ChCr = django_filters.CharFilter(label='ChCr',lookup_expr='icontains')
    CHMo = django_filters.CharFilter(label='CHMo',lookup_expr='icontains')
    ChTi = django_filters.CharFilter(label='ChTi',lookup_expr='icontains')

    ChNb = django_filters.CharFilter(label='ChNb',lookup_expr='icontains')
    ChZr = django_filters.CharFilter(label='ChZr',lookup_expr='icontains')
    ChN = django_filters.CharFilter(label='ChN',lookup_expr='icontains')
    Others = django_filters.CharFilter(label='Others',lookup_expr='icontains')

    SAApp = django_filters.CharFilter(field_name='SAApp', lookup_expr='icontains')

    class Meta:
        model = sa
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
        
        
        




