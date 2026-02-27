from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_invoice_email(invoice_id):
    # placeholder task: in real app fetch invoice and patient email
    # send_mail('Invoice', 'Your invoice is ready', 'from@example.com', ['to@example.com'])
    return f'sent-invoice-{invoice_id}'
