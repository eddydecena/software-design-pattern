import time

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

if __name__ == '__main__':
    try:
        fibs = fib()
        for f in fibs:
            print(f)
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping...')
        print('Stopped!')
