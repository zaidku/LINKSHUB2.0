# viewer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload_model/', views.upload_model, name='upload_model'),
    path('model_view/', views.model_list, name='model_list'),
    path('models/<int:model_id>/', views.view_model, name='view_model'),
    path('cases/', views.cases, name='cases'),
    path('cases/create/', views.create_case, name='create_case'),
    path('calls/', views.calls, name='calls'),
    path('accounting/', views.accounting, name='accounting'),
    path('sales/', views.sales, name='sales'),
    path('lab-product/', views.lab_product, name='lab_product'),
    path('outsource/', views.outsource, name='outsource'),
    path('settings/', views.settings, name='settings'),
    path('accounts/', views.accounts, name='accounts'),
    path('cases/search/', views.search_cases, name='search_cases'),
    path('designer-dashboard/', views.designer_dashboard, name='designer_dashboard'),

    path("outsource/", views.outsource, name="outsource"),

    path("create-case/", views.create_case, name="create_case"),  # Add this line
    path("send-to-outsource/<int:case_id>/", views.send_to_outsource, name="send_to_outsource"),
]



