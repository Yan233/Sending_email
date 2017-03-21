# -*- coding: utf-8 -*-

# basic script to send an email

# add attachment



import requests



# loading the info

from keys import *



key = 'key-f44193c05fedf0cb47e6c7d6d6d1b8cc'

Sandbox = 'sandboxc3cc6e77be2f42c492060a77b3b360c1.mailgun.org'

                                       
# email particulars

recipient = 'chenyan91uk@gmail.com'

sender = 'twitterfreeze@gmail.com'



subject = 'Tweets Analysis'



at_file = "text2.txt"

body_t = """
Hi there, you just downloaded your tweets and here is your analysis!
Have Fun!

Best wishes,
Twitter Freeze
"""

# formattting and sending message

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(Sandbox)

request = requests.post(request_url, auth=('api', key),

    files=[("attachment", open(at_file))],

    data={

    'from': sender,

    'to': recipient,

    'subject': subject,

    'text': body_t})



# checking the status

print ('Status: {0}'.format(request.status_code))

print ('Body:   {0}'.format(request.text))



    