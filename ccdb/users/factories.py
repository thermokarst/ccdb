from factory import DjangoModelFactory, Sequence

from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = Sequence(lambda n: 'user{}'.format(n))
    username = Sequence(lambda n: 'username{}'.format(n))
