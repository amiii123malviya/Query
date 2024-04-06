from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    # stu_contact=models.IntegerField()
    # stu_add=models.CharField(max_length=100)
    stu_city=models.CharField(max_length=50,null=True)

    class Meta:
        db_table='Student'
        verbose_name_plural='Student'

    def __str__(self):
        return self.stu_name