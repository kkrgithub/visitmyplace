from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from thumbs import ImageWithThumbsField

# Create your models here.

Crime_type = (('Robbery','Robbery'),('cheating','cheating'),('crime against women','crime against women'),('voilence','voilence'))

class Base(models.Model):
    active = models.PositiveIntegerField(default = 2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True



class Country(Base):
    name = models.CharField(_("Country *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class State(Base):
    country = models.ForeignKey(Country)
    name = models.CharField(_("State *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class City(Base):
    state = models.ForeignKey(State)
    name = models.CharField(_("City *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)

class Rating(Base):
    value = models.IntegerField()

class ShoppingType(Base):
    name = models.CharField(max_length = 20)  

class ShoppingCategory(Base):
    shopping_type = models.ForeignKey(ShoppingType)
    name = models.CharField(max_length = 20)


class Address(Base):

    city = models.ForeignKey(City)
    address1 = models.CharField(max_length=500, blank = True, null = True)
    address2 = models.CharField(max_length=500, blank = True, null = True)
    pincode = models.CharField(max_length=500, blank = True, null = True)
    content_type = models.ForeignKey(ContentType,verbose_name=('content type'),
                related_name='content_type_set_for%(cla''ss)s')
    object_id = models.TextField(_('object ID'))
    relatedTo = generic.GenericForeignKey(ct_field='content_type',
                fk_field='object_id')
    address_type = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.name

class Transport(Base):
    name = models.CharField(max_length = 20) 
    
    

class Transportclass(Base):
    transport = models.ForeignKey(Transport)
    name =  models.CharField(max_length = 20)
    cost_per_km1 = models.IntegerField()
    cost_per_km2 = models.IntegerField()
    cost_per_km2 = models.IntegerField()


class Crime(Base):
    name = models.CharField(max_length = 20 choices = Crime_type) #choices





