import factory

from .models import Project, Grant, GrantReport


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: 'project{}'.format(n))
    code = factory.Sequence(lambda n: 'p{}'.format(n))
    iacuc_number = 'abc'
    description = 'lorem ipsum'
    sort_order = factory.Sequence(lambda n: n)


class GrantFactory(factory.DjangoModelFactory):
    class Meta:
        model = Grant

    title = factory.Sequence(lambda n: 'grant{}'.format(n))
    code = factory.Sequence(lambda n: 'g{}'.format(n))
    description = 'lorem ipsum'
    sort_order = factory.Sequence(lambda n: n)


class GrantReportFactory(factory.DjangoModelFactory):
    class Meta:
        model = GrantReport

    grant = 0
    title = factory.Sequence(lambda n: 'grant{}'.format(n))
    code = factory.Sequence(lambda n: 'g{}'.format(n))
    description = 'lorem ipsum'
    sort_order = factory.Sequence(lambda n: n)

