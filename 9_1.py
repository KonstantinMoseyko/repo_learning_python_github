from time import sleep


class TrafficLight:
    __color = 'Серобурый'

    def running(self):
        while True:
            print(f'red light')
            sleep(7)
            print(f'yellow light')
            sleep(2)
            print(f'green light')
            sleep(10)


user_light = TrafficLight()
user_light.running()
