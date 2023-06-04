from django.contrib import admin

from erp.models import Funcionario, Produto, Venda


class FuncionarioAdmin(admin.ModelAdmin):
    pass


class ProdutoAdmin(admin.ModelAdmin):
    pass


class VendaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
