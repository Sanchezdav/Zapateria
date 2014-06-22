from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	estado = models.CharField(max_length=255)
	municipio = models.CharField(max_length=255)
	colonia = models.CharField(max_length=255)
	calle = models.CharField(max_length=255)
	numero = models.IntegerField()
	codigo_postal = models.IntegerField()
	telefono = models.CharField(max_length=15)

class Tipo(models.Model):
	tipo = models.CharField(max_length=255)

	def __unicode__(self):
		return self.tipo

class Color(models.Model):
	color = models.CharField(max_length=255)

	def __unicode__(self):
		return self.color

class Material(models.Model):
	material = models.CharField(max_length=255)
	color = models.ForeignKey(Color)

	def __unicode__(self):
		return '%s %s' % (self.material, self.color)

class Adorno(models.Model):
	adorno = models.CharField(max_length=255)
	color = models.ForeignKey(Color)

	def __unicode__(self):
		return '%s %s' % (self.adorno, self.color)

