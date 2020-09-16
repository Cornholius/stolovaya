from celery import task
from django.core.mail import send_mail
from .models import Feedback
from django.conf import settings

@task
def feedback_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Feedback.objects.get(id=order_id)
    subject = 'Новый отзыв от {}'.format(order.name)
    message = """
    На сайте оставлен новый отзыв\n
    Имя: {}\n
    Email: {}\n
    Дата: {}\n
    Отзыв:\n
    {}    
    """.format(order.name, order.email, order.created_date.strftime("%d.%m.%Y %H:%m"), order.message)
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, ['y.layshkin@gmail.com'])
    return mail_sent
