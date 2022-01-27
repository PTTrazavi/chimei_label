from django.urls import include, path
from . import views

urlpatterns = [
    # path('', views.patient, name='patient'),
    path('Pdetail/<int:pk>', views.patient_detail, name='patient_detail'),
    path('loadcsv', views.load_csv, name='load_csv'),
    path('exportcsv', views.export_patient_csv, name='export_patient_csv'),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
