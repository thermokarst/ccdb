from django.db import migrations
from django.forms import modelform_factory


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        Species = apps.get_model('species', 'Species')
        SpeciesForm = modelform_factory(Species, fields='__all__')

        species = [
            ('Alaska whitefish', 'Coregonus', 'nelsonii'),
            ('Alaskan brook lamprey', 'Lampetra', 'alaskense'),
            ('American river lamprey', 'Lampetra', 'ayresii'),
            ('American shad', 'Alosa', 'sapidissima'),
            ('Arctic char', 'Salvelinus', 'alpinus'),
            ('Arctic cisco', 'Coregonus', 'autumnalis'),
            ('Arctic cod', 'Boreogadus', 'saida'),
            ('Arctic flounder', 'Pleuronectes', 'glacialis'),
            ('Arctic grayling', 'Thymallus', 'arcticus'),
            ('Arctic lamprey', 'Lampetra', 'camtschatica'),
            ('Atlantic salmon', 'Salmo', 'salar'),
            ('Bering cisco', 'Coregonus', 'laurettae'),
            ('broad whitefish', 'Coregonus', 'nasus'),
            ('brook trout', 'Salvelinus', 'fontinalis'),
            ('Bull frog', 'Rana', 'catesbeiana'),
            ('burbot', 'Lota', 'lota'),
            ('char-unspecified', 'Salvelinus', ''),
            ('Chinook salmon', 'Oncorhynchus', 'tshawytscha'),
            ('chorus frog', 'Pseudacris', 'regilla'),
            ('chum salmon', 'Oncorhynchus', 'keta'),
            ('cod-unspecified', 'Gadidae', ''),
            ('coho salmon', 'Oncorhynchus', 'kisutch'),
            ('columbia spotted frog', 'Rana', 'lutieventris'),
            ('cutthroat trout', 'Oncorhynchus', 'clarkii'),
            ('eulachon', 'Thaleichthys', 'pacificus'),
            ('general fish observation, no species information', '', ''),
            ('green sturgeon', 'Acipenser', 'medirostris'),
            ('herrings-unspecified', 'Clupeidae', ''),
            ('humpback whitefish', 'Coregonus', 'pidschian'),
            ('lake chub', 'Couesius', 'plumbeus'),
            ('lake trout', 'Salvelinus', 'namaycush'),
            ('lake whitefish', 'Coregonus', 'clupeaformis'),
            ('lamprey-unspecified', 'Lampetra', ''),
            ('least cisco', 'Coregonus', 'sardinella'),
            ('Leopard Frog', 'Rana', 'pipiens'),
            ('longfin smelt', 'Spirinchus', 'thaleichthys'),
            ('longnose sucker', 'Catostomus', 'catostomus'),
            ('long-toed salamander', 'Ambystoma', 'macrodactylum'),
            ('northwestern salamander', 'Ambystoma', 'gracile'),
            ('Pacific cod', 'Gadus', 'macrocephalus'),
            ('Pacific herring', 'Clupea', 'pallasii'),
            ('Pacific lamprey', 'Lampetra', 'tridentata'),
            ('Pacific salmon-unspecified', 'Semelparous Oncorhynchus', ''),
            ('Pacific Sandlance', 'Ammodytes', 'hexapterus'),
            ('pink salmon', 'Oncorhynchus', 'gorbuscha'),
            ('pond smelt', 'Hypomesus', 'olidus'),
            ('pygmy whitefish', 'Prosopium', 'coulteri'),
            ('rainbow smelt', 'Osmerus', 'mordax'),
            ('rainbow trout', 'Oncorhynchus', 'mykiss'),
            ('red-legged frog', 'Rana', 'aurora'),
            ('righteye flounders-unspecified', 'Pleuronectidae', ''),
            ('roughskin newt', 'Taricha', 'granulosa'),
            ('round whitefish', 'Prosopium', 'cylindraceum'),
            ('saffron cod', 'Eleginus', 'gracilis'),
            ('sharpnose sculpin', 'Clinocottus', 'acuticeps'),
            ('sheefish', 'Stenodus', 'leucichthys'),
            ('shiner perch', 'Cymatogaster', 'aggregata'),
            ('smelt-unspecified', 'Osmeridae', ''),
            ('sockeye salmon', 'Oncorhynchus', 'nerka'),
            ('starry flounder', 'Platichthys', 'stellatus'),
            ('stickleback-unspecified', 'Gasterosteidae', ''),
            ('sturgeon-unspecified', 'Acipenser', ''),
            ('surf smelt', 'Hypomesus', 'pretiosus'),
            ('trout-perch', 'Percopsis', 'omiscomaycus'),
            ('trout-unspecified', 'Iteroparous Oncorhynchus', ''),
            ('western brook lamprey', 'Lampetra', 'richardsoni'),
            ('western floater mussel', 'Anodontia', 'kennerlyi'),
            ('western pearlshell mussel', 'Margarita', 'falcata'),
            ('western toad', 'Bufo', 'boreas'),
            ('white sturgeon', 'Acipenser', 'transmontanus'),
            ('whitefish-unspecified', 'Coregoninae', ''),
            ('wood frog', 'Rana', 'sylvatica'),
            ('yellow perch', 'Perca', 'flavescens'),
            ('Yukon floater mussel', 'Anodontia', 'beringia'),
        ]

        for s in species:
            form = SpeciesForm(dict(common_name=s[0], genus=s[1],
                                    species=s[2]))
            if form.is_valid():
                Species.objects.create(**form.cleaned_data)
            else:
                print('species', form.errors.as_data())

    dependencies = [
        ('species', '0005_replace_sex_fields'),
    ]

    operations = [
        migrations.RunPython(migrate),
    ]
