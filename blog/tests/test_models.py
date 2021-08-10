from django.test import TestCase
from blog.models import Post

class PostModelTests(TestCase):
    def test_is_empty(self):
        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    #def test_is_count_one(self):
        #"""1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
        #post = Post(title='test_title', text='test_text')
        #post.save()
        #saved_posts = Post.objects.all()
        #self.assertEqual(saved_posts.count(), 1)