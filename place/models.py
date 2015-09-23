from django.db import models

# Create your models here.

Tastes = (('sweet','sweet'),('hot and spicy','hot and spicy'),('hot','hot'))
Eat_type = (('drink','drink'),('meal','meal'),('snack','snack'),('fruit','fruit'))
Weather_type = (('freezing','freezing'),('moderate','moderate'),('very hot','very hot'),('Rainy','Rainy'))
Age = (('children','children'),('young','young'),('old','old'))

class Place(Base):
    name = models.CharField(max_length = 50)
    address = models.ForeignKey(Address)
    

class Food(Base):
    name = models.CharField(max_length = 50)
    taste = models.CharField(max_length = 20, choices = Tastes) #choices
    mode_of_eating = models.CharField(max_length = 10, choices = Eat_type )  #choices
    cost = models.IntegerField()
    best_place = models.ForeignKey(Place)
    pronounciation = models.CharField(max_length = 20, null = True ,blank = True)
    user_rating = models.ForeignKey(Rating)
    locale_rating = models.ForeignKey(Rating)

class Shopping(Base):
    type_of_shopping = models.ForeignKey(ShoppingType) 
    famous_for = models.ForeignKey(ShoppingCategory) #relation is many to many or foriegnkey ??


class Safety(Base):
    place = models.ForeignKey(Place)
    water = models.BooleanField()
    weather = models.CharField(max_length = 10, choices = Weather_type) #choices
    age_group = models.CharField(max_length = 10,choices = Age) #choices or age
    crime = models.ForeignKey(Crime)     




