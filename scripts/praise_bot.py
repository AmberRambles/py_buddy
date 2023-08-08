import random
random.seed()
print('Welcome to Praise-Bot, The nicest bot around!')
print('Can I just say?', end=' ')
praise_list = ['You are looking amazing!', 'I love what you are doing with your hair!',
        'A mind like yours could fix a lot of badness.', 'You\'re a good user! Yes you are!',
        'Does your mamma let you date?', 'Don\'t forget to be awesome!']
rand_val = random.randint(0, len(praise_list) - 1)
print(praise_list[rand_val])
