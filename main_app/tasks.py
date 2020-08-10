from celery import task
from django.core.mail import send_mail
from .models import Feedback


@task
def feedback_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Feedback.objects.get(id=order_id)
    subject = '31231231'
    message = '312312'

    mail_sent = send_mail(subject,
                          message,
                          'yar.corn@yandex.ru',
                          [order.email])

    return mail_sent