Установка:

фйал requiments.txt лежит в корне проекта

дополнительно надо установить:
RabbitMQ

дополнительно надо запустить:
RabbitMQ rabbitmq-server
celery celery -A stolovaya worker -l info -P gevent


Supervisor:
sudo apt install supervisor
создаём файл настроек
sudo sh -c 'echo_supervisord_conf > /etc/supervisor/supervisord.conf'

для запуска супервизора вместе с системой создаём файл:
sudo touch /etc/systemd/system/supervisord.service
"""
[Unit]
Description=Supervisor daemon
Documentation=http://supervisord.org
After=network.target
[Service]
ExecStart=/usr/local/bin/supervisord -n -c /etc/supervisor/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=42s
[Install]
WantedBy=multi-user.target
Alias=supervisord.service
"""
запускаем супервизор ак службу
sudo systemctl start supervisord.service
(проверяем работу)
ps aux | grep super

для добавления служб добавляем в файл конфигурации:
sudo nano /etc/supervisor/supervisord.conf
[include]
files=conf.d/*.conf
files=conf.d/*.ini
;files = relative/directory/*.ini
