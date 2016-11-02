import asyncio, orm

from models import User, Blog, Comment

loop = asyncio.get_event_loop()


@asyncio.coroutine
def test():
    yield from orm.create_pool(loop, user='user', password='password', db='awesome',
                               host='168.160.185.113', port=3306)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


loop.run_until_complete(test())
loop.close()
# for x in test():
#    pass
