from django.contrib import admin
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)

admin.site.register(Basket)


@admin.register(Product)
class AdminProducts(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'image', 'description', 'short_descriptions', ('price', 'quantity'), 'category']
    readonly_fields = ['short_descriptions']
    ordering = ['-price']
    search_fields = ['name']


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ['product', 'created_timestamp']
    extra = 0
