import numpy as np

def calculate(l):
    try:
        #reshape
        x = np.reshape(l,(3,3))

        #mean
        mean1 = list(np.mean(x, axis=0, dtype=float))
        mean2 = list(np.mean(x, axis=1, dtype=float))
        mean3 = np.mean(x, dtype=float)
        mean = [mean1, mean2, mean3]

        #variance
        var1 = list(np.var(x, axis=0, dtype=float))
        var2 = list(np.var(x, axis=1, dtype=float))
        var3 = np.var(x, dtype=float)
        var = [var1, var2, var3]

        #standard deviation
        std1 = list(np.std(x, axis=0, dtype=float))
        std2 = list(np.std(x, axis=1, dtype=float))
        std3 = np.std(x, dtype=float)
        std = [std1, std2, std3]

        #max
        max1 = list(np.max(x, axis=0))
        max2 = list(np.max(x, axis=1))
        max3 = np.max(x)
        maxx = [max1, max2, max3]

        #min
        min1 = list(np.min(x, axis=0))
        min2 = list(np.min(x, axis=1))
        min3 = np.min(x)
        minn = [min1,min2, min3]

        #sum
        sum1 = list(np.sum(x, axis=0))
        sum2 = list(np.sum(x, axis=1))
        sum3 = np.sum(x)
        summ = [sum1, sum2, sum3]

        calculations = {
            'mean': mean,
            'variance': var,
            'standard deviation': std,
            'max': maxx,
            'min': minn,
            'sum': summ
        }
        return calculations
    except ValueError:
        x = "List must contain nine numbers."
        return x
    