from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
     bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

print('sending...')
producer.send('topic_test', value={'counter': 1})
