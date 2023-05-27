from django.db import models
from set.models import cust, pipegrade, coilgrade
from django.utils import timezone
# Create your models here.
class sa(models.Model):
    SANo = models.CharField(primary_key=True, max_length=100, verbose_name = "SA No") 
    SAStatus = models.CharField(max_length=50, blank=True, null=True,verbose_name = "SAStatus")
    IDate = models.DateTimeField(default=timezone.now,verbose_name = "Date")
    SAVer = models.CharField(max_length=2, blank=True, null=True,verbose_name = "SA Version")
    SAVerNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Version note") 

    CustID = models.ForeignKey(cust ,max_length=15, on_delete=models.SET_NULL, blank=True, null=True,verbose_name = "Customer")
    # CustID = models.CharField(max_length=15, blank=True, null=True,verbose_name = "Customer ID")
    PartNo = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Part No")
    PartName = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Part Name")
    PartMaker = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Part Maker")

    Model = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Model")
    PipeStd = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Standard")
    SKind = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Shape")
    PKind = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Kind")

    OD = models.CharField(max_length=5, blank=True, null=True,verbose_name = "OD")
    ID = models.CharField(max_length=5, blank=True, null=True,verbose_name = "ID")
    WT = models.CharField(max_length=5, blank=True, null=True,verbose_name = "WT")
    L = models.CharField(max_length=9, blank=True, null=True,verbose_name = "L")
    
    AdjOD = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. OD")
    AdjID = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. ID")
    AdjWT = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. WT")
    AdjL = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. L")

    # PipeGrade = models.CharField(max_length=50, blank=True, null=True,verbose_name = "PipeGrade")
    PipeGrade = models.ForeignKey(pipegrade,max_length=50, on_delete=models.CASCADE, blank=True, null=True,verbose_name = "Pipe Grade")
    
    InBead = models.CharField(max_length=10, blank=True, null=True,verbose_name = "Inside Bead")
    InBeadH = models.CharField(max_length=10, blank=True, null=True,verbose_name = "IB Height")
    SurfLevel = models.CharField(max_length=10, blank=True, null=True,verbose_name = "Surface Level")

    SurfTreat = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Surface Treat")
    Straight = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Straight")
    Bending = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Bending")
    Flaring = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flaring")
    Flattening90 = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flattening90")
    Flattening = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flattening")

    SQWSPost = models.CharField(max_length=30, blank=True, null=True,verbose_name = "SQWSPost")
    SQConR = models.CharField(max_length=30, blank=True, null=True,verbose_name = "SQConR")
    PPunch = models.CharField(max_length=30, blank=True, null=True,verbose_name = "PPunch")
    
    PipeEdgeNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pipe Edge")
    PipeEdgeNoteT = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pipe E Tole.")
    Notes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Notes")


    TS = models.CharField(max_length=30, blank=True, null=True,verbose_name = "TS")
    YP = models.CharField(max_length=30, blank=True, null=True,verbose_name = "YP")
    EL = models.CharField(max_length=30, blank=True, null=True,verbose_name = "EL")
    Tensile = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Tensile")
    Hardness = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Hardness")
    Other = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Other")

    ChC = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Carbon")
    ChSi = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Silicon")
    ChMn = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Manganese")
    ChP = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Phosphorus")
    ChS = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Sulphur")
    ChAL = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Aluminium")

    ChNi = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Nickel")
    ChCr = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Chromium")
    CHMo = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Molybdenum")
    ChTi = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Titanium")
    ChNb = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Niobium")
    ChZr = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Zinc")
    ChN = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Nitrogen")
    ChOthers = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChOthers")

    Others = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Others")
    HeatTreat = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Heat Treatment")
    NDI = models.CharField(max_length=150, blank=True, null=True,verbose_name = "NDI")
    SurfCondE = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Surface Condition English")
    SurfCondV = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Surface Condition Vietnamese")
    Coatching = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Coatching")
    PackStd = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Packing Std.")
    Marking = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Marking")

    CHOICES = (
        ('OK', 'OK'),
        ('NG', 'NG'),
        ('Remark', 'Remark'),
    )

    QAManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "QA Judg.")
    QAManDate = models.DateTimeField(blank=True, null=True,verbose_name = "QAManDate")
    QCManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "QC Judg.")
    QCManDate = models.DateTimeField(blank=True, null=True,verbose_name = "QCManDate")
    DGDJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "AO Judg.")
    DGDManDate = models.DateTimeField(blank=True, null=True,verbose_name = "DGDManDate")
    QCRecNo = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Record No")
    LastUser = models.CharField(max_length=500, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")

    ImageSPEC = models.ImageField(upload_to='SAImangeSPEC/', blank=True, null=True,verbose_name = "drawing reference")
    
    # CSAp = models.FileField(upload_to ='CSApproval/',verbose_name = "Upload CS")
    SAApp = models.FileField(upload_to ='SAApproved/', null=True, blank=True, verbose_name = "Approved SA")
    AppDate = models.DateTimeField(null=True, blank=True, verbose_name = "Approved Date")

    def __str__(self):
        return self.SANo
