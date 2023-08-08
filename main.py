import random

quit_menu = '\nPrint "q" or "quit" to exit\n+++++++++++++\n'
DEBUG = True
loop_count = 0
prompt = 'How are you feeling today?'
prompt_list = ['You can tell me anything.', 'What\'s new? I\'m stuck in a box.', 'Any hot gossip? Spill.',
               'What up, Bestie?!']
response_list = ['That\'s dope! Thanks for telling me!', 'Very interesting. Is this normal?',
                 'Could you tell me a bit more about that?', 'Whoa!',
                 'I don\'t have any experience with that sort of thing.']

if __name__ == '__main__':
    #TODO #02 create if/else to pass name as a cmd arg
    print('Hello, Amber!')
    random.seed()
    user_input = ''
    while user_input != -1:
        if loop_count > 0:
            r_int = random.randint(0, (len(prompt_list) - 1))
            prompt = prompt_list[r_int]
        if DEBUG:
            prompt += quit_menu
        user_input = input(prompt)
        if user_input == 'Q' or user_input == 'q' or user_input == 'Quit' or user_input == 'quit':
            user_input = -1
        else:
            if loop_count == 0:
                #TODO #01 output an appropriate emotional response instead of a random one
                if DEBUG:
                    print("TODO #01: add emotional response")
            else:
                r_int = random.randint(0, (len(response_list) - 1))
                print(response_list[r_int])
            loop_count += 1
