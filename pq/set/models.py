from django.db import models
from django.urls import reverse

# Create your models here.

class cust(models.Model):

    CustID = models.CharField(primary_key=True, max_length=15, verbose_name = "CustID") 
    Fullname = models.CharField(max_length=150, blank=True, null=True,verbose_name = "Full name")
    Address = models.CharField(max_length=100, blank=True, null=True,verbose_name = "Address")
    SignT = models.CharField(max_length=50, blank=True, null=True,verbose_name = "SignT")
    Sign1 = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Sign1")
    Sign2 = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Sign2")
    Sign3 = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Sign3")
    Notes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "SignT")
    LastUser = models.CharField(max_length=50, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")

    def __str__(self):
        return self.Fullname

class pipegrade(models.Model):
     
    PipeGrade = models.CharField(primary_key=True, max_length=50, verbose_name = "Pipe Grade") 
    
    Index = models.FloatField(max_length=20, blank=True, null=True,verbose_name = "Index")
    # T = models.FloatField(max_length=20, blank=True, null=True,verbose_name = "T")
    Notes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Note")
    TS = models.CharField(max_length=30, blank=True, null=True,verbose_name = "TS")
    YP = models.CharField(max_length=30, blank=True, null=True,verbose_name = "YP")
    EL = models.CharField(max_length=30, blank=True, null=True,verbose_name = "EL")
    Hardness = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Hardness")
    Other = models.CharField(max_length=30, blank=True, null=True,verbose_name = "Other")
    ChC = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChC")
    ChSi = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChSi")
    ChMn = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChMn")
    ChP = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChP")
    ChS = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChS")
    ChAL = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChAL")
    ChNi = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChNi")
    ChCr = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChCr")
    ChMo = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChMo")
    ChTi = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChTi")
    ChNb = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChNb")
    ChZr = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChZr")
    ChN = models.CharField(max_length=30, blank=True, null=True,verbose_name = "ChN")

    Flaring = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flaring")
    Flattening = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flattening 0")
    Flattening90 = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Flattening 90")
    Straightness = models.CharField(max_length=50, blank=True, null=True,verbose_name = "Straightness")
     

    LastUser = models.CharField(max_length=50, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")

    def __str__(self):
        return self.PipeGrade
    
    

    def get_absolute_url(self):
        return reverse("pgrade-detail", args=[str(self.PipeGrade)])
    
class coilgrade(models.Model):
     
    CoilGrade = models.CharField(primary_key=True, max_length=50, verbose_name = "Coil Grade") 
    Notes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Note")
    
    LastUser = models.CharField(max_length=50, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")

    def __str__(self):
        return self.CoilGrade
    
    def get_absolute_url(self):
        return reverse("cgrade-detail", args=[str(self.CoilGrade)])
    

class surflevel(models.Model):
     
    SurfLevel = models.CharField(primary_key=True, max_length=10, verbose_name = "Surface level") 
    ENotes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "English Note")
    VNotes = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Vietnamese Note")

    
    LastUser = models.CharField(max_length=50, blank=True, null=True,verbose_name = "LastUser")
    LastimeUser = models.DateTimeField(blank=True, null=True,verbose_name = "LastimeUser")

    def __str__(self):
        return self.SurfLevel
    
    # def get_absolute_url(self):
    #     return reverse("cgrade-detail", args=[str(self.CoilGrade)])

class EmailReport(models.Model):

    ActChoise = (
            ('SAAppNote', 'Receive SA approved notice'), # SA Approved notice
            ('CSDeadline', 'The deadline for the CS is approaching'), # CS deadline notice
            ('Other', 'Other notice'),
        )
    ActionName = models.CharField(max_length=10, blank=True, null=True, choices = ActChoise,verbose_name = "Action")
    ReciEmail = models.EmailField(verbose_name = "Email address of receiver")
    Remarks = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Remarks")

    def __str__(self):
        return self.ActionName

class tmp(models.Model):
    PipeGrade = models.CharField(max_length=50,blank=True, null=True, verbose_name = "Pipe Grade") 
    Index = models.FloatField(max_length=20, blank=True, null=True,verbose_name = "Index")
# class test(models.Model):
#     testname = models.CharField(max_length=500, blank=True, null=True,verbose_name = "Test Name")
