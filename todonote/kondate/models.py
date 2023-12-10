from django.db import models
from django.utils import timezone

CATEGORY = (("Monday", "月曜日"), ("Tuesday", "火曜日"), ("Wednesday", "水曜日"),("Thursday", "木曜日"), ("Friday", "金曜日"), ("Saturday", "土曜日"), ("Sunday", "日曜日"))

class Kondate(models.Model):
    category = models.CharField(
        max_length=30,
        choices = CATEGORY
    )   
    breakfast = models.TextField("朝食", blank=True) 
    lunch = models.TextField("昼食", blank=True) 
    dinner = models.TextField("夕食", blank=True) 
    snacking = models.TextField("間食", blank=True)
    eatday = models.DateField("食事日",default=timezone.now)
    created = models.DateTimeField("記録日時",default=timezone.now)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()            
        return super(Kondate,self).save(*args, **kwargs)
    

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ["eatday"]

