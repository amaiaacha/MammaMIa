from django.test import TestCase

# Create your tests her


from MammaMia.models import Masa

class MasaTest(TestCase):
    @classmethod
    def test_nameMa(self):
        masa=Masa.object.get(id=1)
        field_label=masa._meta.get_field('nameMa').verbose_name
        self.assertEquals(field_label,'nameMa')
