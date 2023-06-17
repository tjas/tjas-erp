import json
from unittest import mock, skip
from http import HTTPStatus

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from django.http import HttpResponse

from erp.models import Funcionario, Produto, Venda


# Home
        
@skip("Not implemented yet")
class HomeViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(HomeViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(HomeViewTest, cls).tearDownClass()


# Login

class ErpLoginViewTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(ErpLoginViewTest, cls).setUpClass()
        cls.superuser = User.objects.create_superuser(username="admin", password="admin")
        cls.login_url = reverse("erp:login")
        cls.dashboard_url = reverse("erp:dashboard")
    
    
    def test_anonymous_user_page_access(self):
        # Garante que o usuário não está logado
        self.client.logout()
        
        response: HttpResponse = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
    
    
    def test_authenticated_user_page_access(self):
        # Garante que o usuário está logado
        self.client.force_login(self.superuser)
        
        response: HttpResponse = self.client.get(self.login_url)
        self.assertRedirects(response, self.dashboard_url)
    
    
    def test_user_login_success(self):
        # Garante que o usuário não está logado
        self.client.logout()
        
        data = {
            "username": self.superuser.username,
            "password": self.superuser.password
        }
        response: HttpResponse = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.superuser.is_authenticated)
    
    
    def test_user_login_fail(self):
        # Garante que o usuário não está logado
        self.client.logout()
        
        data = {
            "username": "anonymous",
            "password": "1234567890"
        }
        response: HttpResponse = self.client.post(self.login_url, data)
        self.assertFalse(response.context['user'].is_authenticated)
        
        response: HttpResponse = self.client.get(self.dashboard_url)
        self.assertRedirects(response, f"{self.login_url}?next={self.dashboard_url}")
        
  
    @classmethod
    def tearDownClass(cls):
        super(ErpLoginViewTest, cls).tearDownClass()
        cls.superuser.delete()


@skip("Not implemented yet")      
class ErpLogoutViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ErpLogoutViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(ErpLogoutViewTest, cls).tearDownClass()

  
@skip("Not implemented yet")      
class DashboardViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(DashboardViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(DashboardViewTest, cls).tearDownClass()
     

# Funcionarios
  
@skip("Not implemented yet")      
class FuncionarioCreateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(FuncionarioCreateViewTest, cls).setUpClass()
        
        cls.funcionario = Funcionario.objects.create(
            nome="John", 
            sobrenome="Doe",
            cpf="12345678900",
            email_funcional="email@example.com",
            remuneracao=15985.19
        )
        
        cls.superuser = User.objects.create_superuser(
            username="admin", password="admin", email="admin@example.com"
        )
        
    @classmethod
    def tearDownClass(cls):
        super(FuncionarioCreateViewTest, cls).tearDownClass()
        cls.funcionario.delete()
        cls.superuser.delete()
        
        
@skip("Not implemented yet")      
class FuncionarioListViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(FuncionarioListViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(FuncionarioListViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class FuncionarioDetailViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(FuncionarioDetailViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(FuncionarioDetailViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class FuncionarioUpdateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(FuncionarioUpdateViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(FuncionarioUpdateViewTest, cls).tearDownClass()


# Produtos
  
@skip("Not implemented yet")      
class ProdutoCreateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ProdutoCreateViewTest, cls).setUpClass()
        
        cls.produto = Produto.objects.create(
            nome="Mouse Logitech MX 3S",
            descricao="Resolução máxima de 8000 DPI. Até 70 dias com uma carga completa. Bateria recarregável (500mAh). Conexão com até 3 dispositivos. 3 horas de uso com uma carga de 1 minuto. Tecnologia sem fio avançada de 2,4 GHz. Tracking em qualquer superfície.",
            preco=641.45,
            imagem=None
        )
        
        cls.superuser = User.objects.create_superuser(
            username="admin", password="admin", email="admin@example.com"
        )
    
    @classmethod
    def tearDownClass(cls):
        super(ProdutoCreateViewTest, cls).tearDownClass()
        cls.produto.delete()
        cls.superuser.delete()
        
        
@skip("Not implemented yet")      
class ProdutoListViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ProdutoListViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(ProdutoListViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class ProdutoDetailViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ProdutoDetailViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(ProdutoDetailViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class ProdutoUpdateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ProdutoUpdateViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(ProdutoUpdateViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class ProdutoDeleteViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ProdutoDeleteViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(ProdutoDeleteViewTest, cls).tearDownClass()


# Vendas

@skip("Not implemented yet")      
class VendaCreateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(VendaCreateViewTest, cls).setUpClass()
        
        cls.funcionario = Funcionario.objects.create(
            nome="John", 
            sobrenome="Doe",
            cpf="12345678900",
            email_funcional="email@example.com",
            remuneracao=15985.19
        )
        
        cls.produto = Produto.objects.create(
            nome="Mouse Logitech MX 3S",
            descricao="Resolução máxima de 8000 DPI. Até 70 dias com uma carga completa. Bateria recarregável (500mAh). Conexão com até 3 dispositivos. 3 horas de uso com uma carga de 1 minuto. Tecnologia sem fio avançada de 2,4 GHz. Tracking em qualquer superfície.",
            preco=641.45,
            imagem=None
        )
        
        cls.venda = Venda.objects.create(
            funcionario = cls.funcionario,
            produto = cls.produto
        )
        
        cls.superuser = User.objects.create_superuser(
            username="admin", password="admin", email="admin@example.com"
        )
    
    @classmethod
    def tearDownClass(cls):
        super(VendaCreateViewTest, cls).tearDownClass()
        cls.venda.delete()
        cls.produto.delete()
        cls.funcionario.delete()
        cls.superuser.delete()
        
        
@skip("Not implemented yet")      
class VendaListViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(VendaListViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(VendaListViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class VendaDetailViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(VendaDetailViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(VendaDetailViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class VendaUpdateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(VendaUpdateViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(VendaUpdateViewTest, cls).tearDownClass()


@skip("Not implemented yet")      
class VendaDeleteViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(VendaDeleteViewTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(VendaDeleteViewTest, cls).tearDownClass()
