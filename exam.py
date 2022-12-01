#1 exam
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs321.log',
                    filemode='w',
                    format='We have some logging message:%(asctime)s:%(levelname)s - %(message)s')

logging.debug('debug')
logging.info('info')


try:
    class Human:
        money = 100
        power = 78
        health = 87
        gladness = 50
        age = 43

        def __init__(self):
            self.gladness += 9
            self.power -= 8

    class Worker(Human):
        money = 100
        power = 91
        health = 87
        age = 21
        gladness = 50

        def __init__(self):
            self.age += 5
            self.power -= 10
            self.money -= 20
            self.health -= 5
            self.gladness += 20


        def allmethods(self):
            print(f'Worker power = {worker.power}')
            print(f'Worker health = {worker.health}')
            print(f'Worker age = {worker.age}')
            print(f'Worker gladness = {worker.gladness}')
            print(f'Worker money = {worker.money}')


    human = Human()
    worker = Worker()
    worker.allmethods()


except:
    print("Something went wrong")

else:
    print("everything is good")
    
#2 exam
import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/currencies/ethereum/markets/")
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)


ethereum_exchange_rate = res_parse_list[0]
print(f"Курс Ethereum = {ethereum_exchange_rate}")
