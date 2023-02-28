from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework_simplejwt.tokens import AccessToken

from reviews.models import Category, Genre, Title, User
from .permisions import (
    IsAdmin, IsAuthorOrAdminOrModerator, IsAdminOrReadOnly
)
from .serializers import (
    SignUpSerializer,
    TokenSerializer,
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    lookup_field = "username"

    @action(methods=["patch", "get"], detail=False,
            permission_classes=(permissions.IsAuthenticated,))
    def me(self, request):
        user = self.request.user
        if request.method == "GET":
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserSerializer(
            user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(role=user.role, partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    # добавить Поиск по названию категории
    # проверить работу пагинации
    # добавить permissions IsAdminOrReadOnly
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    # добавить Поиск по названию жанра
    # проверить работу пагинации
    # добавить permissions IsAdminOrReadOnly
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    # добавить возможность фильтрации по категории, жанру, году и названию произведения
    # добавить permissions IsAdminOrReadOnly
    # возможно, придется добавить IsAuthenticatedOrReadOnly из базовых,нонужно затестить
    # добавить валидацию по году выпуска
    # проверить работу пагинации
    # добавить get_queryset, в котором высчитывается и выводится rating
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def get_signup(request):
    """Функция регистрации нового пользователя, генерации кода подтверждения
    отправление данного кода по указанному электронному адресу."""
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get("username")
    email = request.data.get("email")
    user, create = User.objects.get_or_create(username=username, email=email)
    confirmation_code = default_token_generator.make_token(user)

    send_mail("Код подтверждения,",
              f"Ваш код подтверждения: {confirmation_code}",
              "test@test.ru",
              (email,))
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def get_token(request):
    """Функция генерации JWT-токена на основе кода подтверждения,
    возвращает ответ с token."""
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get("username")
    confirmation_code = request.data.get("confirmation_code")
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)
        return Response({f"token: {token}"}, status=status.HTTP_200_OK)
    return Response(
        {"WRONG CODE": "Неверный код подтверждения"},
        status=status.HTTP_400_BAD_REQUEST
    )