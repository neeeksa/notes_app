from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('all_notes', views.all_notes, name='all_notes'),
    path('<int:pk>', views.NotesDetailView.as_view(), name='notes_view'),
    path('<int:pk>/update', views.NotesUpdateView.as_view(), name='notes_update'),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes_delete')
]

