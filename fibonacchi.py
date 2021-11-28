def fibonacchi(n, fibonacchi_list=None):
    """ recursive function to calculate a list of fibonacchi numbers up to n """
    if not n:
        return fibonacchi_list
    else:
        fibonacchi_list = [0, 1]
	    fibonacchi_list.append(fibonacchi_list[-1] + fibonacchi_list[-2])
        return fibonacchi(n - 1, fibonacchi_list)
