from django.urls import include, path
from .views import ProductCreate, ProductList, ProductDetail, ProductUpdate, ProductDelete


urlpatterns = [
    path('create/', ProductCreate.as_view(), name='create-Product'),
    path('', ProductList.as_view()),
    path('<int:pk>/', ProductDetail.as_view(), name='retrieve-Product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update-Product'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete-Product')
]
