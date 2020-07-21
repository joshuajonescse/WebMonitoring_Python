# https://www.youtube.com/watch?v=yqm6MBt-yfY&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=15
# Please note that i am commenting out reboot server function below because i dont have api token to do that

import os
import smtplib
import requests
# import logging
from linode_api4 import LinodeClient, Instance

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

# logging.basicConfig(filename='PATH_TO_DESIRED_LOG_FILE',
#                     level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()   # identifies ourselves with the mail server we are using
        smtp.starttls()   # encrypts our message
        smtp.ehlo()       # again need to identify ourselves as an encrypted connection

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Joshua, YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'

        # logging.info('Sending Email...')
        smtp.sendmail(EMAIL_ADDRESS, 'INSERT_RECEIVER_ADDRESS', msg)


def reboot_server():  # please note that this function is very much linode company specific, the mothods and calls may vary based on ur service provider
    client = LinodeClient(LINODE_TOKEN)
    my_server = client.load(Instance, 376715)
    my_server.reboot()
    # logging.info('Attempting to reboot server...')


try:
    r = requests.get('https://www.youtube.com/', timeout=5)

    if r.status_code != 200:
        # logging.info('Website is DOWN!')
        notify_user()
        #reboot_server()
    else:
        print("your server is fine and running")
        #logging.info('Website is UP')
except Exception as e:
    # logging.info('Website is DOWN!')
    notify_user()
    #reboot_server()