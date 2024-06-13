from app.scrapy.LoaderManager import LoaderManager
from app.models import clothes


class BEAMSLoader(LoaderManager):

    def __init__(self):
        pass
    def load(self, posts):
        print(posts)
        print('#'*30, "load", '#'*30)
        for post in posts:
            model = clothes(
                sex = post.sex,
                color = post.color,
                category = post.category,
                image_url = post.image_url,
                post_url = post.post_url,
            )

            model.save()

