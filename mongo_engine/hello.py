import mongoengine
MONGODB_PARAMS = {
    'service': {
        'name': 'trans',
        'host': '192.168.11.191',
        'port': 27017,
    }
}

mongoengine.register_connection(alias='trans', **MONGODB_PARAMS.get('service'))


class UserInfo(mongoengine.Document):
    user_id = mongoengine.StringField()
    user_name = mongoengine.StringField()

    meta = {
        'db_alias': 'trans',
        'collection': 'user_info',
        'indexes': [
            'user_id'
        ],
    }


class Page(mongoengine.DynamicDocument):
    title = mongoengine.StringField()

    meta = {
        'db_alias': 'trans',
        'collection': 'page'
    }


def page_add():
    page = Page(
        title=""
    )
    page.tage = ["1","2"]
    page.save()


def add():
    user = UserInfo(
        user_id="00001",
        user_name="tom"
    )
    user.save()


if __name__ == '__main__':
    page_add()
