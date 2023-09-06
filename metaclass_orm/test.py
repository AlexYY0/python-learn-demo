from metaclass_orm.field import IntegerField, StringField
from metaclass_orm.model import Model


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u.save()
