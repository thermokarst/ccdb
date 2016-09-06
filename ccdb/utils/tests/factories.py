from factory import DjangoModelFactory, Sequence, SubFactory

from ..models import AdminSection, AdminEntry


class AdminSectionFactory(DjangoModelFactory):
    class Meta:
        model = AdminSection

    name = Sequence(lambda n: 'section{}'.format(n))
    sort = Sequence(lambda n: n)


class AdminEntryFactory(DjangoModelFactory):
    class Meta:
        model = AdminEntry

    package = Sequence(lambda n: 'package{}'.format(n))
    model = Sequence(lambda n: 'section{}'.format(n))
    section = SubFactory(AdminSectionFactory)
    sort = Sequence(lambda n: n)
