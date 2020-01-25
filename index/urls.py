from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('article/create/', views.ArticleCreateView.as_view(success_url='/'),
         name="create_article"),
    path('showarticles/',views.ArticlesListView.as_view(),name="show_articles"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(),name="article_detail"),
    path('doctors/',views.ShowDoctors.as_view(),name='association'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(),name="doctor_details"),
    path('fitpalmaps/', views.MapView,name="maps"),
]+static(settings.MEDIA_URL, document_root=settings. MEDIA_ROOT)