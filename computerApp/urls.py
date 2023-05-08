from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('machines/', views.machine_list_view, name='machines'),
	path('personnels/', views.personnel_list_view, name='personnels'),
	path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
	path('add-machine/', views.machine_add_form, name='add-machine'),
	path('add-personnel/', views.personnel_add_form, name='add-personnel'),
	path('personnel/<pk>', views.personnel_detail_view, name='personnel-detail'),
	path('machine/delete/<int:machine_id>/', views.delete_machine, name='delete_machine'),
	path('personnel/delete/<str:personnel_id>/', views.delete_personnel, name='delete_personnel'),
	path('pluton-chat/', views.chat_bot, name='chatbot'),
]
