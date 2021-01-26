from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from manager.models import Book


class TestMyAppPlease(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test_name")
        self.user1 = User.objects.create_user("test_name1")
        self.user2 = User.objects.create_user("test_name2")

    def test_add_book(self):
        self.client.force_login(self.user1)
        url = reverse("add-book")
        data = {
            'slug': 'test_title',
            'title': "test title",
            'text': 'test text'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302, msg="is not redirected")
        self.assertTrue(Book.objects.exists(), msg="book is not created")
        book = Book.objects.first()
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.text, data['text'])
        self.assertEqual(book.slug, data['slug'])
        self.assertEqual(book.authors.first(), self.user1)
        self.client.logout()
        data = {
            'slug': 'test_title2',
            'title': "test title2",
            'text': 'test text'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302, msg="is not redirected")
        self.assertEqual(Book.objects.count(), 1, msg="created book without author")
    
    def test_book_delete(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(slug='test_title1', title='test_title1')
        self.book1.authors.add(self.user)
        self.book1.save()
        self.book2 = Book.objects.create(slug='test_title2', title='test_title2')
        self.assertEqual(Book.objects.count(), 2)
        url = reverse('delete-book', kwargs=dict(slug=self.book1.slug))
        self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)
        url = reverse('delete-book', kwargs=dict(slug=self.book2.slug))
        self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)
        self.client.logout()
        self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)