STATUS_CHOICES = {

    ('send','send'),
    ('accepted','accepted'),
    ('default','default')

}

DEFAULT = 'default'
SEND = 'send'
ACCEPT = 'accepted'

STATUS_CHOICES = [
        (DEFAULT, 'default'),
        (SEND, 'send'),
        (ACCEPT, 'accepted'),
    ]

print(type(STATUS_CHOICES))
print(STATUS_CHOICES['default'])