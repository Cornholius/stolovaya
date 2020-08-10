from celery import task
from django.core.mail import send_mail
from .models import Feedback


@task
def order_created(order_id):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Feedback.objects.get(id=order_id)
    subject = 'Ваш заказ на сайте <...> успешно оформлен'
    message = 'Здравствуй {},\n' \
              'Тебе хватило мозгов оформить заказ, поздравляю!\n' \
              'Твой заказ под номером {} ждёт тебя.\n ' \
              'Приди и забери свой хавчик.'

    mail_sent = send_mail(subject,
                          message,
                          'yar.corn@yandex.ru',
                          [order.email])

    return mail_sent