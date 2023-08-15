from django.urls import path
from core.erp.views.category.views import CategoryListView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView, CategoryFormView
from core.erp.views.client.views import ClientView
from core.erp.views.dashboard.views import DashboardView
from core.erp.views.product.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductFormView
from core.erp.views.tests.views import TestView

app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/dalete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),

    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/dalete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/form/', ProductFormView.as_view(), name='product_form'),

    #client
    path('client/', ClientView.as_view(), name='client'),

    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # test
    path('test/', TestView.as_view(), name='dashboard'),
]
