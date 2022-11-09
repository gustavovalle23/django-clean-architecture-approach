from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from json import dumps
from kafka import KafkaProducer
from datetime import datetime



class Food(models.Model):
    name: str = models.CharField(max_length=255)
    price: float = models.FloatField()

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'


@receiver(post_save, sender=Food)
def send_to_book_system(sender, instance, created, using, **kwargs):
    print(sender, instance, kwargs, datetime.now())
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    producer.send('food.changes', value=model_to_dict(instance))
