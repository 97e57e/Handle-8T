from django.db import models

class Province(models.Model):
    province_code = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=20)

    def __str__(self):
        return self.province_name
    
class Borough(models.Model):
    borough_code = models.IntegerField(primary_key=True)
    province_code = models.ForeignKey(Province, on_delete=models.CASCADE)
    borough_name = models.CharField(max_length=30)

    def __str__(self):
        return self.province_code.province_name + " " + self.borough_name