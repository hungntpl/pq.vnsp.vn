from django.db import models
from django.urls import reverse
from set.models import cust, pipegrade, coilgrade, surflevel
from sa.models import sa
from django.utils import timezone


    
# Create your models here.
class cs(models.Model):

    CHOICES = (
        ('OK', 'OK'),
        ('NG', 'NG'),
        ('Remark', 'Remark'),
    )

    CHOICESIn = (
        ('New', 'New'),
        ('Modify', 'Modify'),
    )
    CSNo = models.CharField(primary_key=True, max_length=100, verbose_name = "CS Number") 
    SANo = models.CharField(max_length=100, blank=True, null=True,verbose_name = "SA Number")
    # SANo = models.ForeignKey(sa, on_delete=models.SET_NULL, blank=True, null=True,verbose_name = "SA Number")
    IDate = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name = "Initial date")
    DLine = models.DateTimeField(verbose_name = "Dead line")
    CVer = models.CharField(max_length=2, blank=True, null=True,verbose_name = "Ver")
    CVerDate = models.DateTimeField(default=timezone.now, blank=True, null=True,verbose_name = "Issue date")
    CVerNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Version note") 
    PVer = models.CharField(max_length=2, blank=True, null=True,verbose_name = "Pervious version")
    PVerDate = models.DateTimeField(blank=True, null=True,verbose_name = "PreVersion date")
    PVerNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "PreVersion Note")

    NewInq = models.CharField(max_length=15, blank=True, null=True, choices = CHOICESIn,verbose_name = "Inquiry")
    ModiC1 = models.BooleanField(blank=True, null=True,verbose_name = "Modi C1")
    ModiC2 = models.BooleanField(blank=True, null=True,verbose_name = "Modi C2")
    PreBy = models.CharField(max_length=50, blank=True, null=True, default='Lâm',verbose_name = "Pre by")
    RecBy = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Rec by")
    # CustID = models.CharField(max_length=15, blank=True, null=True,verbose_name = "Cust. ID")

    CustID = models.ForeignKey(cust ,max_length=15, on_delete=models.SET_NULL, blank=True, null=True,verbose_name = "Customer")
    Enduser = models.CharField(max_length=50, blank=True, null=True,verbose_name = "End User")
    Event = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Event")
    # Demand = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Demand")

    PartNo = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Part No")
    PartName = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Part Name")
    PartMaker = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Part Maker")

    Model = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Model")
    EstQty = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Demand")
    EstTime = models.CharField(max_length=50, blank=True, null=True,verbose_name = "E.Tim")
    EstFDeli = models.CharField(max_length=50, blank=True, null=True,verbose_name = "E. Deli.")
    EstFQty = models.CharField(max_length=50, blank=True, null=True,verbose_name = "EF.Qty")

    SKChoise = (
        ('Round', 'Round'),
        ('Square', 'Square'),
        ('Oval', 'Oval'),
        ('Ellipse', 'Ellipse'),
    )

    SKind = models.CharField(max_length=50, blank=True, choices = SKChoise, null=True,verbose_name = "Shape")

    PKChoise = (
        ('EG', 'EG'),
        ('CD', 'CD'),
    )
    PKind = models.CharField(max_length=50, blank=True, null=True, choices = PKChoise,verbose_name = "Process")
    
    OD = models.CharField(max_length=5, blank=True, null=True,verbose_name = "OD")
    ID = models.CharField(max_length=5, blank=True, null=True,verbose_name = "ID")
    WT = models.CharField(max_length=5, blank=True, null=True,verbose_name = "WT")
    L = models.CharField(max_length=9, blank=True, null=True,verbose_name = "L")
    AdjOD = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. OD")
    AdjID = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. ID")
    AdjWT = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. WT")
    AdjL = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Tol. L")
    
    # PipeGrade = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pipe Grade")

    PipeGrade = models.ForeignKey(pipegrade,max_length=50, on_delete=models.CASCADE, blank=True, null=True,verbose_name = "Pipe Grade")
    
    Notes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Note/Other")
    CoilMaker = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Coil Maker")
    CProcess = models.CharField(max_length=25, blank=True, null=True,verbose_name = "C Process")

    IBChoise = (
        ('IBC', 'IBC'),
        ('NON-IBC', 'NON-IBC'),
        ('IB-P', 'IB-P'),
    )

    InBead = models.CharField(max_length=10, blank=True, null=True, choices = IBChoise,verbose_name = "IBC")
    SLChoise = (
        ('A', 'A'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C', 'C'),
    )
    # SurfLevel = models.CharField(max_length=10, blank=True, null=True, choices = SLChoise,verbose_name = "Surface level")
    
    SurfLevel = models.ForeignKey(surflevel ,max_length=10, on_delete=models.SET_NULL, blank=True, null=True,verbose_name = "Surface level")
    # Shape = models.CharField(max_length=10, blank=True, null=True, choices = SKChoise,verbose_name = "Shape")

    SurfTreat = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Surface Treat")
    Straight = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Straight")
    Flaring = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flaring")
    Flattening90 = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flattening 90")

    Flattening = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flattening 0")
    SQWSPost = models.CharField(max_length=30, blank=True, null=True,verbose_name = "SQWSPost")
    SQConR = models.CharField(max_length=30, blank=True, null=True,verbose_name = "SQConR")
    PPunch = models.CharField(max_length=30, blank=True, null=True,verbose_name = "PPunch")
    PackASQty = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pack AS Qty")
    PackPCQty = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pack PC Qty")

    Density = models.CharField(max_length=25, blank=True, null=True,verbose_name = "Kg/pc")
    
    PackUnit = models.CharField(max_length=25, blank=True, null=True,verbose_name = "Pack U.")
    PackASNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pack AS Note")
    PackPCNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Pack PC Note")
    ASPICNote = models.CharField(max_length=200, blank=True, null=True,verbose_name = "AS P.I.C.Note")

    PEdgeChoise = (
        ('AS', 'AS'),
        ('Br', 'Br'),
        ('CF', 'CF'),
        ('Facer', 'Facer'),
    )

    PipeEdgeValue = models.CharField(max_length=5, blank=True, choices = PEdgeChoise, null=True,verbose_name = "Pipe Edge")
    PipeEdgeNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "PipeEdgeNote")

    ASManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "AS Judg.")
    ASManNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "AS Note")
    ASManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")
    
    PIManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "PI Judg.")
    PIManNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "PI Note")


    QAManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "QA Judg.")
    QAManNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "QA Note")
    QAManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")

    QCManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "QC Judg.")
    QCManNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "QC Note")
    QCManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")

    PRManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "PR Judg.")
    PRManNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "PR Note")
    PRManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")

    DGDJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "AO Judg.")
    DGDNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "AO Note")
    DGDManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")

   
    PCManJudgment = models.CharField(max_length=15, blank=True, null=True, choices = CHOICES,verbose_name = "PC Judg.")
    PCManNote = models.CharField(max_length=150, blank=True, null=True,verbose_name = "PC Note")
    PCManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")

    # CSAp = models.FileField(upload_to ='CS/',verbose_name = "Upload CS")
    ImageSPEC = models.ImageField(upload_to='CSImangeSPEC/', blank=True, null=True,verbose_name = "drawing reference")

    # CSAp = models.FileField(upload_to ='CSApproval/',verbose_name = "Upload CS")
    # CSAp = models.FileField(upload_to ='CSApproved/', null=True, blank=True, verbose_name = "Approved CS")
    PIManDate = models.DateTimeField(blank=True, null=True,verbose_name = "Date")

    LastUser = models.CharField(max_length=500, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")

    # testname = models.ForeignKey(test, on_delete=models.SET_NULL, blank=True, null=True,verbose_name = "Test Name")

    def get_absolute_url(self):
        return reverse('cs-update', kwargs={'pk': self.pk})

    # def response_change(self, request, obj):
    #     if "_continue" in request.POST:
    #         return super().response_change(request, obj)
	

    def __str__(self):
        return self.CSNo

class csqc(models.Model):

    CSNo = models.ForeignKey(cs, on_delete=models.CASCADE, null=True, verbose_name = "CS No")
    AdjOD= models.CharField(max_length = 20, blank=True, null=True,verbose_name = "Tol. OD")
    AdjID= models.CharField(max_length = 20, blank=True, null=True,verbose_name = "Tol. ID")
    AdjWT= models.CharField(max_length = 20, blank=True, null=True,verbose_name = "Tol. WT")
    AdjL= models.CharField(max_length = 20, blank=True, null=True,verbose_name = "Tol. L")
    InBead= models.CharField(max_length = 10, blank=True, null=True,verbose_name = "InBead")
    SurfLevel= models.CharField(max_length = 10, blank=True, null=True,verbose_name = "Surface Level")
    SurfTreat= models.CharField(max_length = 20, blank=True, null=True,verbose_name = "Surface Treat")
    Straight= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "Straightness")
    Flaring= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "Flaring")
    Flattening90= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "Flat 90")
    Flattening= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "Flat 0")
    SQWSPost= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "SQWSPost")
    SQConR= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "SQConR")
    PPunch= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "PPunch")
    PipeEdgeNote= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "Pipe Edge")
    Notes= models.CharField(max_length = 500, blank=True, null=True,verbose_name = "Notes")
    TS= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "TS(N/mm2)")
    YP= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "YP(%)")
    EL= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "EL")
    Hardness= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Hardness")
    Other= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Other")
    ChC= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Carbon")
    ChSi= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Silicon")
    ChMn= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Manganese")
    ChP= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Phosphorus")
    ChS= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Sulphur")
    ChAL= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Aluminium")
    ChNi= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Nickel")
    ChCr= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Chromium")
    ChMo= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Molybdenum")
    ChTi= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Titanium")
    ChNb= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Niobium")
    ChZr= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Zinc")
    ChN= models.CharField(max_length = 30, blank=True, null=True,verbose_name = "Nitrogen")
    QAManJudgment= models.CharField(max_length = 15, blank=True, null=True,verbose_name = "QA Judg.")
    QAManNote= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "QA Note")
    Description= models.CharField(max_length = 150, blank=True, null=True,verbose_name = "Description")
    
    
    LastUser= models.CharField(max_length = 50, blank=True, null=True,verbose_name = "LastUser")

    def __str__(self):
        return str(self.CSNo)


class custprocess(models.Model):
    
    # class Meta:
    #     unique_together = (('CSNo', 'No'),)

    CSNo = models.ForeignKey(cs, on_delete=models.CASCADE, null=True, verbose_name = "CS No")
    # No = models.SmallIntegerField(default = 1, verbose_name = "No") 
    CProcess = models.CharField(max_length=25, blank=True, null=True,verbose_name = "CProcess")
    QCNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "QCNote")
    Description = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Description")

class coilprocess(models.Model):
    
    # class Meta:
    #     unique_together = (('CSNo', 'No'),)

    CSNo = models.ForeignKey(cs, on_delete=models.CASCADE, null=True, verbose_name = "CS No")
    # No = models.SmallIntegerField(default = 1, verbose_name = "No") 
    CMaker = models.CharField(max_length=25, blank=True, null=True,verbose_name = "Coil Maker")
    CSPEC = models.CharField(max_length=50, blank=True, null=True,verbose_name = "SPEC")
    # CGrade = models.CharField(max_length=50, blank=True, null=True,verbose_name = "CGrade")
    CGrade = models.ForeignKey(coilgrade, on_delete=models.SET_NULL, blank=True, null=True,verbose_name = "Coil Grade")
    
    CWTOrder = models.CharField(max_length=25, blank=True, null=True,verbose_name = "Coil WT")
    SCoilWidth = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Coil Width")
    MLineQC = models.CharField(max_length=15, blank=True, null=True,verbose_name = "MLine QC")
    Description = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Description")
    SCoilWidthPI = models.CharField(max_length=50, blank=True, null=True,verbose_name = "SCoilWidthPI")
    
    MLinePI = models.CharField(max_length=15, blank=True, null=True,verbose_name = "MLine PI")
    
    def __str__(self):
        return self.CGrade

class CSApproved(models.Model):
    CSNo = models.ForeignKey(cs, on_delete=models.CASCADE, null=True,verbose_name = "CS No")
    # Note = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Note")
    CSAp = models.FileField(upload_to ='CSApproved/', null=True, verbose_name = "Upload CS")
    # image = models.ImageField(upload_to='CSApproved/images', blank=True, null=True)

    def __str__(self):
        return str(self.CSNo)
    
    def get_absolute_url(self):
        return "/CSApproved/" + self.CSAp
    

class CSPI(models.Model):
    CSNo = models.ForeignKey(cs, on_delete=models.CASCADE, null=True,verbose_name = "CS No")

    RBreakdown = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Breakdown")
    RFinpass = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Finpass")
    RSGR = models.CharField(max_length=20, blank=True, null=True,verbose_name = "SGR")
    RSQ = models.CharField(max_length=20, blank=True, null=True,verbose_name = "SQ")
    RSizeH = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Size horizonal")
    RSizeV = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Size vertical")
    RTH1 = models.CharField(max_length=20, blank=True, null=True,verbose_name = "T/H-1")
    RTH2 = models.CharField(max_length=20, blank=True, null=True,verbose_name = "T/H-2")
    TIBCHold = models.CharField(max_length=20, blank=True, null=True,verbose_name = "IBC Hold")
    TIBCTool = models.CharField(max_length=20, blank=True, null=True,verbose_name = "IBC Tool")
    TInpeder = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Inpeder")
    TCutClamp = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Cut off Clamp")
    TFaceClamp = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Face Clamp")
    TDelClamp = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Delimpler Clamp")
    TPlug = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Plug")
    TRing = models.CharField(max_length=20, blank=True, null=True,verbose_name = "Ring")
    Notes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Notes")
    PIManjudgment = models.CharField(max_length=15, blank=True, null=True,verbose_name = "PI jud")
    PIManNote = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Note")
    MLine = models.CharField(max_length=10, blank=True, null=True,verbose_name = "MLine")
    TtlInvest = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Ttl Invest ($)")
    Leadtime = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Leadtime")
    


    LastUser = models.CharField(max_length=50, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")


    def __str__(self):
        return str(self.CSNo)

class Parent(models.Model):
    name = models.CharField(max_length=255)


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    CSAp = models.FileField(upload_to ='CSApproved/test',blank=True, null=True, verbose_name = "Upload CS")