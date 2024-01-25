from django.db import models

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.deptname

    
class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()

    def __str__(self):
        return self.ename


class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.IntegerField()
    highsal=models.IntegerField()

    def __str__(self):
        return self.grade
    

class Bonus(models.Model):
    grade=models.ForeignKey(SalGrade,on_delete=models.CASCADE,primary_key=True)
    sal=models.IntegerField()

    def __str__(self):
        return self.sal