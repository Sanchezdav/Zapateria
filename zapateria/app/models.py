from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	apellido_paterno = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	apellido_materno = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	edad = models.IntegerField()
	estado = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	municipio = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	colonia = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	calle = models.CharField(max_length=255, validators=[
			RegexValidator(
					regex = '^[a-zA-Z]*$',
					message = 'Este campo no debe contener numeros'
				)
		])
	numero = models.IntegerField()
	codigo_postal = models.IntegerField()
	telefono = models.CharField(max_length=15)
	avatar = models.ImageField(upload_to = 'avatares', default = 'avatares/None/no-img.jpg', blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Perfiles'

	def __unicode__(self):
		return self.usuario.username

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

