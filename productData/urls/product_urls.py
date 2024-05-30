from django.urls import path

from productData.views import product_views as views

urlpatterns=[
     path('', views.FetchProducts.as_view()),
     path('create',views.MakeProduct.as_view()),
     path('<str:id>', views.GetProductByID.as_view()),
     path('update/<int:id>', views.ProductUpdateByID.as_view(), name='update_product'),  
     path('delete/<int:id>', views.DeleteProductByID.as_view(), name='delete_product'),  
]