from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def create_jwt_pair_for_user(user: User):
    refresh = RefreshToken.for_user(user)
    #probar el tiempo de vida.
    tokens = {"access": str(refresh.access_token), "refresh": str(refresh), "lifetime": refresh.lifetime }
    
    return tokens