from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django import template
register = template.Library()

from app.models import *
from app.forms import *

@register.inclusion_tag('base.html', takes_context=True)
def my_avatar(request, id_perfil):
	user = Perfil.objects.get(pk = id_perfil)
	return {'user': user}

def home(request):
	return render(request, 'index.html')

class Registro(CreateView):
	model = User
	template_name = 'registro.html'
	form_class = UserForm
	success_url = reverse_lazy('login')

class Actualizar(CreateView):
	model = Perfil
	template_name = 'actualizar.html'
	form_class = PerfilForm
	success_url = reverse_lazy('home')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Actualizar, self).dispatch(*args, **kwargs)  


	def form_valid(self, form):
		self.act = form.save(commit=False)

		form.instance.usuario = self.request.user
		self.act.nombre = form.cleaned_data['nombre']
		self.act.apellido_paterno = form.cleaned_data['apellido_paterno']
		self.act.apellido_materno = form.cleaned_data['apellido_materno']
		self.act.edad = form.cleaned_data['edad']
		self.act.estado = form.cleaned_data['estado']
		self.act.municipio = form.cleaned_data['municipio']
		self.act.colonia = form.cleaned_data['colonia']
		self.act.calle = form.cleaned_data['calle']
		self.act.numero = form.cleaned_data['numero']
		self.act.codigo_postal = form.cleaned_data['codigo_postal']
		self.act.telefono = form.cleaned_data['telefono']
		self.act.avatar = form.cleaned_data['avatar']
		self.act.save()

		return super(Actualizar, self).form_valid(form)

class PerfilView(DetailView):
	model = Perfil
	template_name = 'perfil.html'
	context_object_name = 'perfil'
