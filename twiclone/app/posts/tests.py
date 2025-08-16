from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post

class PostTests(TestCase):
    def test_create_text_only(self):
        Post.objects.create(text='hello')
        self.assertEqual(Post.objects.count(), 1)

    def test_create_with_image(self):
        img = SimpleUploadedFile('t.png', b'\x89PNG\r\n\x1a\n', content_type='image/png')
        p = Post.objects.create(text='img', image=img)
        self.assertTrue(bool(p.image))
