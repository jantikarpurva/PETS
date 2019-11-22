from django.db import models


# Create your models here.


class DogBreedInfo(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed


class DogInfo(models.Model):
    pet_breed = models.ForeignKey(DogBreedInfo, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    gender = models.BooleanField()
    height = models.IntegerField()
    weight = models.IntegerField()
    price = models.IntegerField(default=3000)
    username = models.CharField(max_length=50, default="john")

    def __str__(self):
        return self.pet_name + "" + str(self.id)


class CatBreedInfo(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed


class CatInfo(models.Model):
    pet_breed = models.ForeignKey(CatBreedInfo, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    gender = models.BooleanField()
    height = models.IntegerField()
    weight = models.IntegerField()
    username = models.CharField(max_length=50, default="john")

    def __str__(self):
        return self.pet_name + "" + str(self.id)


class RabbitBreedInfo(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed


class RabbitInfo(models.Model):
    pet_breed = models.ForeignKey(RabbitBreedInfo, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    gender = models.BooleanField()
    height = models.IntegerField()
    weight = models.IntegerField()
    username = models.CharField(max_length=50, default="john")

    def __str__(self):
        return self.pet_name + "" + str(self.id)


class HamsterBreedInfo(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed


class HamsterInfo(models.Model):
    pet_breed = models.ForeignKey(HamsterBreedInfo, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    gender = models.BooleanField()
    height = models.IntegerField()
    weight = models.IntegerField()
    username = models.CharField(max_length=50, default="john")

    def __str__(self):
        return self.pet_name + "" + str(self.id)













