from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    Covers CRUD, permissions, filtering, searching, and ordering.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        This method is run once for the entire test class.
        """
        # --- Step 2: Set Up Testing Environment ---
        # Create a user for authentication-required tests
        cls.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Create authors
        cls.author1 = Author.objects.create(name='George Orwell')
        cls.author2 = Author.objects.create(name='J.R.R. Tolkien')

        # Create books
        cls.book1 = Book.objects.create(title='1984', publication_year=1949, author=cls.author1)
        cls.book2 = Book.objects.create(title='Animal Farm', publication_year=1945, author=cls.author1)
        cls.book3 = Book.objects.create(title='The Hobbit', publication_year=1937, author=cls.author2)

    def test_list_books(self):
        """
        Ensure any user can list all books.
        Tests the ListView functionality.
        """
        url = reverse('book-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book(self):
        """
        Ensure any user can retrieve a single book by its ID.
        Tests the DetailView functionality.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a book.
        Tests permissions on the CreateView.
        """
        url = reverse('book-create')
        data = {'title': 'Brave New World', 'publication_year': 1932, 'author': self.author1.pk}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a book.
        Tests the CreateView functionality.
        """
        self.client.login(username='testuser', password='testpassword123')
        url = reverse('book-create')
        data = {'title': 'Brave New World', 'publication_year': 1932, 'author': self.author1.pk}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, 'Brave New World')

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        Tests the UpdateView functionality.
        """
        self.client.login(username='testuser', password='testpassword123')
        url = reverse('book-update', kwargs={'pk': self.book2.pk})
        updated_data = {'title': 'The Orwell Farm', 'publication_year': 1945, 'author': self.author1.pk}
        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.title, 'The Orwell Farm')
        
    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        Tests the DeleteView functionality.
        """
        self.client.login(username='testuser', password='testpassword123')
        url = reverse('book-delete', kwargs={'pk': self.book3.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_year(self):
        """
        Test filtering the book list by publication_year.
        """
        url = f"{reverse('book-list')}?publication_year=1945"
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_search_books_by_title(self):
        """
        Test searching the book list by title.
        """
        url = f"{reverse('book-list')}?search=Hobbit"
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_order_books_by_title(self):
        """
        Test ordering the book list by title.
        """
        url = f"{reverse('book-list')}?ordering=title"
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that '1984' comes first
        self.assertEqual(response.data[0]['title'], '1984')
