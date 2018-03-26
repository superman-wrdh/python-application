import mongoengine

MONGODB_PARAMS = {
    'service': {
        'name': 'trans',
        'host': '192.168.11.191',
        'port': 27017,
    }
}

mongoengine.register_connection(alias='mongo_trans', **MONGODB_PARAMS.get('service'))


class UserInfo(mongoengine.Document):
    user_id = mongoengine.StringField()
    user_name = mongoengine.StringField()

    meta = {
        'db_alias': 'mongo_trans',
        'collection': 'user_info',
        'indexes': [
            'user_id'
        ],
    }


def add():
    user = UserInfo(
        user_id="00001",
        user_name="tom"
    )
    user.save()


if __name__ == '__main__':
    add()