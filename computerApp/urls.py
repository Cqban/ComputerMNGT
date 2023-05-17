from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('machines/', views.machine_list_view, name='machines'),
	path('personnels/', views.personnel_list_view, name='personnels'),
    path('infrastructures/', views.infra_list_view, name='infrastructures'),
	path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('machine/<int:pk>/change-state/', views.toggle_machine, name='toggle_machine'),
    path('personnel/<pk>', views.personnel_detail_view, name='personnel-detail'),
    path('add-infra/', views.infra_add_form, name='add-infra'),
	path('add-machine/', views.machine_add_form, name='add-machine'),
	path('add-personnel/', views.personnel_add_form, name='add-personnel'),
    path('infrastructure/delete/<int:infrastructure_id>/', views.delete_infra, name='delete_infrastructure'),
	path('machine/delete/<int:machine_id>/', views.delete_machine, name='delete_machine'),
	path('personnel/delete/<str:personnel_id>/', views.delete_personnel, name='delete_personnel'),
	path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
	path('pluton-chat/', views.chat_bot, name='chatbot'),
]
