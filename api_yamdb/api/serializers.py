from django.core.validators import RegexValidator
from rest_framework.generics import get_object_or_404
from rest_framework import serializers

from reviews.models import User, Category, Genre, Title, Review, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role"
        )


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, max_length=150,
        validators=[RegexValidator(regex=r"^[\w.@+-]+$")]
    )
    # В модели AbstracUser уже используется необходимая валидация
    # username_validator, но pytest требует еще, то же самое с длиной email
    email = serializers.EmailField(required=True, max_length=254)

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
        if (User.objects.filter(username=username)
                and User.objects.get(username=username).email != email):
            raise serializers.ValidationError(
                "Указанный 'username' уже занят, используйте другой"
            )
        if (User.objects.filter(email=email)
                and User.objects.get(email=email).username != username):
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
    rating = serializers.IntegerField(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = "__all__"


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        many=True, slug_field="slug", queryset=Genre.objects.all()
    )

    class Meta:
        fields = "__all__"
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method == 'POST':
            if Review.objects.filter(title=title, author=author).exists():
                raise serializers.ValidationError(
                    'Вы не можете добавить более одного отзыва на произведение'
                )
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
