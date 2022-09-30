from django.contrib import admin
from .models import Car,Manager,OptionA,OptionB,OptionC,OptionD,MyCar,Cachedata
# Register your models here.

admin.site.register(Car)
admin.site.register(MyCar)
admin.site.register(Manager)
admin.site.register(OptionA)
admin.site.register(OptionB)
admin.site.register(OptionC)
admin.site.register(OptionD)
admin.site.register(Cachedata)
