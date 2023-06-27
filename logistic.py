def logistic(x,r):
    return r * x * (1-x)

def iterate_f(it, x, r):
    xs=[]
    x0=logistic(x,r)
    #xs.append(x0)
    for i in range(it):
        xs.append(logistic(x0,r))
        x0=xs[i]
    return xs

    
if __name__ == '__main__':
    print(logistic())