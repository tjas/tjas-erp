
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from erp.forms import FuncionarioForm, ProdutoForm
from erp.models import Funcionario, Produto, Venda


# Home
class HomeView(TemplateView):
    template_name = 'erp/index.html'


# Login

class ErpLoginView(LoginView):
    template_name = 'erp/login.html'
    success_url = reverse_lazy('erp:dashboard')
    redirect_authenticated_user = True


class ErpLogoutView(LogoutView):
    template_name = 'erp/logout.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'erp/dashboard.html'


# Funcionarios

@login_required
def cria_funcionario(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        form = FuncionarioForm()
        
        return render(
            requisicao,
            template_name='erp/funcionarios/novo.html',
            context={'form': form}
        )
        
    elif requisicao.method == 'POST':
        form = FuncionarioForm(requisicao.POST)
        
        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)
            funcionario.save()
            
            return HttpResponseRedirect(redirect_to='/')


@login_required
def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()
        
        return render(
            requisicao,
            template_name='erp/funcionarios/lista.html',
            context={'funcionarios': funcionarios}
        )


@login_required
def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
            
        return render(
            requisicao,
            template_name='erp/funcionarios/detalhe.html',
            context={'funcionario': funcionario}
        )


@login_required
def atualiza_funcionario(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(isinstance=funcionario)
        
        return render(
            requisicao,
            template_name='erp/funcionarios/atualiza.html',
            context={'form': form}
        )

    elif requisicao.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(requisicao.POST, isinstance=funcionario)
        
        if form.is_valid():
            funcionario.save()
            
            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')


# Produtos

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'erp/produtos/lista.html'
    context_object_name = 'produtos'


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'erp/produtos/atualiza.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produtos'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produtos'
    success_url = reverse_lazy('erp:lista_produtos')
    
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


# Vendas

class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:lista_vendas')
    fields = ['funcionario', 'produto']


class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'


class VendaDetailView(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'vendas'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')
    
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = '__all__'
    success_url = reverse_lazy('erp:lista_vendas')
