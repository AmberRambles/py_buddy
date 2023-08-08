import sys
import time
def sleep1():
    time.sleep(1.25)

def breathe_in(count = 4):
    print('Breathe In')
    for i in range(count):
        print(f'{i + 1}...')
        sleep1()
    print()

def breathe_out(count = 4):
    print('Breathe Out')
    for i in range(count):
        print(f'{i + 1}...')
        sleep1()
    print()

def hold(count = 4):
    print('Hold')
    for i in range(count):
        print(f'{i + 1}...')
        sleep1()
    print()

def square_breath():
    breathe_in()
    hold()
    breathe_out()
    hold()

if __name__ == '__main__':
    #if run from command line instead of imported (start here)
    if len(sys.argv) > 1:
        try:
            num_remaining = int(sys.argv[1])
        except:
            print('Input error: Integer expected.')
            print('Try: python square_breathing.py 4')
            exit(1)
        while num_remaining > 0:
            square_breath()
            num_remaining -= 1
    else:
        square_breath()
