from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Para o cálculo do fatorial utilizar o comando curl no endereço <URL>/fact e para o cálculo do fibonacci, no endereço <URL>/fib.'

@app.route('/fact', methods=['POST', 'GET'])
def fact(data):
    n = int(data["fact"])
    if n < 0:
        return "O número não pode ser negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = n
        while n > 1:
            n = n - 1
            fact = fact*n
        return fact

@app.route('/fib', methods=['POST', 'GET'])
def fib(data):
    n = int(data["fib"])
    a = 0
    b = 1
    if n < 0:
        return "O número não pode ser negativo."
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

if __name__ == '__main__':
    app.run()
