from django.test import TestCase
from django.utils import timezone
from .models import Nota
import datetime

# Create your tests here.
class NotaModelTests(TestCase):

    def test_es_reciente_con_fecha_futura(self):
        """
        es_reciente() 
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Nota(creado=time)
        self.assertIs(future_question.es_reciente(), False)
