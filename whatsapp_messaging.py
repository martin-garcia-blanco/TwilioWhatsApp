from twilio.rest import Client

def msg(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'AC50406f7a035d2bf5904c176a76cdac96'
    auth_token = 'f256b006bcb215a863e197ba63dabe32'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Martin':'+34123456789'}

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'good morning {} !'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,
            )

        print(msg_loved_ones.sid)
