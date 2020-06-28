Установка:

фйал requiments.txt лежит в корне проекта

дополнительно надо установить:
RabbitMQ

дополнительно надо запустить:
RabbitMQ rabbitmq-server
celery celery -A stolovaya worker -l info -P gevent
