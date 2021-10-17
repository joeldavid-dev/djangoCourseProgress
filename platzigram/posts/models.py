"""Posts models."""

#Django
from django.db import models

class User(models.Model):
	"""User model."""

	#Dato único.
	email = models.EmailField(unique=True)

	#Tamaño máximo de 100 caracteres.
	password = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	#Datos boleanos. Por defecto serán falsos.
	is_admin = models.BooleanField(default=False)

	#La biografía puede estar vacía.
	bio = models.TextField()

	#Permite que birthdate este en blanco o sea null.
	birthdate = models.DateField(blank=True, null=True)

	#Guarda automáticamente la fecha de creación.
	create = models.DateTimeField(auto_now_add=True)

	#Guarda automáticamente la fecha de edición.
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return email."""
		return self.email