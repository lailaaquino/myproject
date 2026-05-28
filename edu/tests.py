
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Autor, Editora
from .forms import SignUpForm
from .serializers import AutorSerializer

#Teste de Model
class AutorModelTest(TestCase):
	def setUp(self):
		self.autor = Autor.objects.create(nome="Machado de Assis")

	def test_autor_criacao(self):
		self.assertEqual(self.autor.nome, "Machado de Assis")
		self.assertTrue(isinstance(self.autor, Autor))

	def test_autor_str(self):
		self.assertEqual(str(self.autor.nome), self.autor.nome)

	def test_nome_max_length(self):
		max_length = self.autor._meta.get_field('nome').max_length
		self.assertEqual(max_length, 100)

#Teste de View
class HomeViewTest(TestCase):
	def setUp(self):
		self.client = Client()

	def test_home_view_status_code(self):
		response = self.client.get(reverse('edu:home'))
		self.assertEqual(response.status_code, 200)

#Teste de Form
class SignUpFormTest(TestCase):
	def setUp(self):
		self.form_data = {
			'username': 'testuser',
			'email': 'test@example.com',
			'password1': 'complexpassword123',
			'password2': 'complexpassword123',
		}

	def test_signup_form_valid(self):
		form = SignUpForm(data=self.form_data)
		self.assertTrue(form.is_valid())

#Teste de Serializer
class AutorSerializerTest(TestCase):
	def setUp(self):
		self.autor = Autor.objects.create(nome="Cecilia Meireles")
		self.serializer = AutorSerializer(self.autor)

	def test_autor_serializer_nome(self):
		self.assertEqual(self.serializer.data['nome'], "Cecilia Meireles")

#Teste de API REST
class AutorAPITest(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.autor1 = Autor.objects.create(nome="Carlos Drummond")
		self.autor2 = Autor.objects.create(nome="Clarice Lispector")

	def test_list_autores_api_status(self):
		try:
			url = reverse('edu:autores-list')
		except Exception:
			url = '/edu/api/autores/'
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_list_autores_api_count(self):
		try:
			url = reverse('edu:autores-list')
		except Exception:
			url = '/edu/api/autores/'
		response = self.client.get(url)
		self.assertGreaterEqual(len(response.data), 2)
