from django.test import TestCase

# Create your tests her


from MammaMia.models import Masa

class MasaTest(TestCase):
    @classmethod
    def test_nameMa(self):
        masa=Masa.object.get(id=1)
        field_label=masa._meta.get_field('nameMa').verbose_name
        self.assertEquals(field_label,'nameMa')

class PhotoTestCase(TestCase):

    def test_add_photo(self):
        image = Masa()
        image.imagen= SimpleUploadedFile(name='masaTradicional.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        image.save()
        self.assertEqual(Masa.objects.count(), 1)