from multiprocessing import Pool

def f(n):
    sum = 0
    for x in range(100):
        sum += x*x
    return sum

if __name__ == "__main__":
    p = Pool(3)
    result=p.map(f, range(100))
    p.close()
    p.join()