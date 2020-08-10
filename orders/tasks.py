from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Ваш заказ на сайте <...> успешно оформлен'.format(order_id)
    message = 'Здравствуй {},\n' \
              'Тебе хватило мозгов оформить заказ, поздравляю!\n' \
              'Твой заказ под номером {} ждёт тебя.\n ' \
              'Приди и забери свой хавчик.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'y.layshkin@gmail.com',
                          [order.email])
    return mail_sent