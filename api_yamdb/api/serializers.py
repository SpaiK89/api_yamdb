from rest_framework import serializers

from reviews.models import User, Category, Genre, Title


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "role", "bio"
        )


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


    class Meta:
        model = User
        fields = ("username", "email")

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        if username == "me":
            raise serializers.ValidationError(
                "Нельзя создать пользователя с таким 'username'"
            )
        if User.objects.filter(
            username=username
        ) and User.objects.get(username=username) != email:
            raise serializers.ValidationError(
                "Указанный 'username' уже занят, используйте другой"
            )
        if User.objects.filter(
            email=email
        ) and User.objects.get(email=email) != username:
            raise serializers.ValidationError(
                "Указанный адрес электронной почты уже занят, используйте "
                "другой"
            )
        return data


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "confirmation_code")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    # добавить дополнительное поле raiting

    class Meta:
        model = Title
        fields = ('name', 'year', 'description', 'genre', 'category', 'rating')