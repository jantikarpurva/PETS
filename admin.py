from django.contrib import admin
from .models import DogBreedInfo, DogInfo, CatBreedInfo, CatInfo, RabbitBreedInfo, RabbitInfo, HamsterBreedInfo, HamsterInfo

# Register your models here.
admin.site.register(DogInfo)
admin.site.register(DogBreedInfo)
admin.site.register(RabbitInfo)
admin.site.register(RabbitBreedInfo)
admin.site.register(CatInfo)
admin.site.register(CatBreedInfo)
admin.site.register(HamsterInfo)
admin.site.register(HamsterBreedInfo)