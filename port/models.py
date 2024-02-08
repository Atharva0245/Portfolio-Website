from django.db import models
from pyexpat import model


class profile(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50, null=True)
    psurname = models.CharField(max_length=30, null=True)
    pcontact = models.CharField(max_length=10, null=True)
    pemail = models.EmailField()
    pskills1 = models.CharField(max_length=100, null=True)
    pskills2 = models.CharField(max_length=100, null=True)
    pskills3 = models.CharField(max_length=100, null=True)
    pachieve = models.CharField(max_length=100, null=True)
    psummary = models.CharField(max_length=100, null=True)
    pproject = models.CharField(max_length=100, null=True)
    pexp = models.CharField(max_length=100, null=True)
    pexpdetails = models.CharField(max_length=100, null=True)
    punv1 = models.CharField(max_length=100, null=True)
    pco1 = models.CharField(max_length=100, null=True)
    pcgpa1 = models.CharField(max_length=100, null=True)
    punv2 = models.CharField(max_length=100, null=True)
    pco2 = models.CharField(max_length=100, null=True)
    pcgpa2 = models.CharField(max_length=100, null=True)


    def __int__(self):
        return self.pid



