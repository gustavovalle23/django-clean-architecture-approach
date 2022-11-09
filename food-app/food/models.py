from json import dumps
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from confluent_kafka import Producer


class Food(models.Model):
    name: str = models.CharField(max_length=255)
    price: float = models.FloatField()

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'


@receiver(post_save, sender=Food)
def send_to_book_system(sender, instance, created, using, **kwargs):
    p = Producer({"bootstrap.servers": 'kafka:9092'})
    msg = dumps(model_to_dict(instance))
    p.produce('topic_test', msg)
    p.flush()
