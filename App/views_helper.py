from django.core.mail import send_mail
from django.template import loader

from AXF.settings import EMAIL_HOST_USER, SERVER_HOST, SERVER_PORT
from App.models import Cart


def send_email(username, receive, u_token):
    '''
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    '''

    subject = 'AXF Active'

    message = '<h1>hello</h1>'

    fromeamil = EMAIL_HOST_USER

    recipientlist = [receive, ]

    data = {
        'username': username,
        'active_url': 'http://{}:{}/axf/activate/?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token)
    }

    html_message = loader.get_template('user/active.html').render(data)

    send_mail(subject=subject, message=message, html_message=html_message, from_email=fromeamil,
              recipient_list=recipientlist)


def get_total_price():
    carts = Cart.objects.filter(c_is_select=True)

    total = 0

    for cart in carts:
        total += cart.c_goods_num * cart.c_goods.price

    return "{:.2f}".format(total)