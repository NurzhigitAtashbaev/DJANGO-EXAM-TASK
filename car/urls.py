from django.urls import path
from .views import main_page, sales_sheet, test_page

urlpatterns = [
    path('', main_page),
    path('test/', test_page),
    path('cars/', sales_sheet)
]

# path('posts/<int:id>/', post_detail_view)
