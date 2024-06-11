# conftest.py
import pytest

# Импортируем класс клиента.
from django.test.client import Client

# Импортируем модель заметки, чтобы создать экземпляр.
from news.models import News, Comment


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')

@pytest.fixture
def not_author(django_user_model):  
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    return news

@pytest.fixture
def pk_news(news):
    return (news.pk,)

@pytest.fixture
def comment(author, news):
    comment = Comment.objects.create(
        news=news,
        author=author,
        text='Текст',
    )
    return comment

@pytest.fixture
def pk_comment(comment):
    return (comment.pk,)


# @pytest.fixture
# def form_data():
#     return {
#         'title': 'Новый заголовок',
#         'text': 'Новый текст',
#         'slug': 'new-slug'
#     }