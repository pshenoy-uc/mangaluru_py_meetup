
def modulo_print(number):
    func = lambda n: number % n
    if not (func(3) or func(5)):
        return 'fizzbuzz'
    elif not func(3):
        return 'fizz'
    elif not func(5):
        return 'buzz'
    else:
        return number

n = input()
for number in range(1, n+1):
    print modulo_print(number)
