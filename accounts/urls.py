from django.urls import path
from .views import RegisterView, LoginView, ProfileView, OrderHistoryView, my_page, get_user_info, get_profile, get_order_history, get_login


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('orders/', OrderHistoryView.as_view(), name='order-history'),
    path('', my_page, name='my_page'),

    # Функциональные представления
    path('user-info/', get_user_info, name='user-info'),
    path('user-profile/', get_profile, name='user-profile'),
    path('order-history-func/', get_order_history, name='order-history-func'),
]