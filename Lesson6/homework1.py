from time import sleep


class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зеленый']


    def running(self):
        i=0
        while i < 3:
            print(f'{TrafficLight._color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i+=1



traffic  = TrafficLight()
traffic.running()