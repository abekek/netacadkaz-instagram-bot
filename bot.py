from instapy import InstaPy
from config import username, password

session = InstaPy(username=username, password=password)
session.login()
session.set_relationship_bounds(enabled=True, max_followers=5000)
session.like_by_tags(["курсыпрограммирования", "программирование"], amount=5)
session.like_by_feed(amount=20, randomize=True, unfollow=True, interact=False)
session.set_dont_like(["naked", "nsfw"])
session.end()