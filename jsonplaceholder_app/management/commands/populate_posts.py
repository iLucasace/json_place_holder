from django.core.management.base import BaseCommand
import requests
from jsonplaceholder_app.models import Post

class Command(BaseCommand):
    help = 'Populate the database with data from JSONPlaceholder API'

    def handle(self, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)
        data = response.json()

        for post_data in data:
            Post.objects.create(
                userId=post_data['userId'],
                id=post_data['id'],
                title=post_data['title'],
                body=post_data['body']
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))
