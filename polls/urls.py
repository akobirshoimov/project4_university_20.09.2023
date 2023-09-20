from django.urls import path
from .views import CreateuniversityView,UpdateuniversityView,ListuniversityView

urlpatterns = [
    path('all/',ListuniversityView.as_view()),
    path('create/',CreateuniversityView.as_view()),
    path('update/<int:university_id>/',UpdateuniversityView.as_view())
]