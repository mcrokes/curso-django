from django.urls import path
from core.erp.views.category.views import CategoryListView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView, CategoryFormView
from core.erp.views.dashboard.views import DashboardView

app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/dalete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),

    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
