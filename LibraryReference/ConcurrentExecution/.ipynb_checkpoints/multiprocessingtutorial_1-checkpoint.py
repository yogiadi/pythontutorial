from multiprocessing import Process
def f(name):
    print('hello', name)
if __name__ == '__main__':
    print('Hi')
    p=Process(target=f, args=('bob',))
    p.start()
    p.join()