
from django.contrib import admin
from django.urls import path,include
from patient import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    #path to access the frontend page
    path('',views.Frontend, name="frontend"),
    
    #path to login/ logout    
    path('login/', include('django.contrib.auth.urls')),
    
    #path to access backend page
    path('backend/',       views.Backend,         name="backend"),
    # url on browser       function in views.py    url inside templates
    
    #path to access backend page
    path('add_patient', views.Add_Patient, name="add_patient"),
    
    #path to access the patient individually
     path('patient/<str:pk>/', views.patient, name="patient"),

     #path to edit  patient
     path('edit_patient', views.edit_patient, name="edit_patient"),

     #path to delete patient
     path('delete_patient/<str:pk>/', views.delete_patient, name="delete_patient")    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
