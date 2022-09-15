"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива)
```
выведет сообщение "проехали ... километров"
в результате поездки потратится бензин и увеличится пробег
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""


class Car:

    def __init__(self, gas=0, mileage=0, capacity=40, gas_per_km=4):

        self.gas = gas  # сколько бензина в баке
        self.mileage = mileage  # пробег
        self.capacity = capacity   # вместимость бака
        self.gas_per_km = gas_per_km  # расход топлива на 100 км

    def fill(self, add_gas: int):

        full_gas = self.gas + add_gas

        if full_gas >= self.capacity:

            self.gas = self.capacity

            print(f'Лишних литров: {full_gas - self.capacity}')

        else:

            self.gas = full_gas

    def ride(self, ride_km: int):

        gas_per_1_km = self.gas_per_km / 100  # расход топлива на 1 км

        gas_for_ride = ride_km * gas_per_1_km

        if gas_for_ride >= self.gas:

            real_ride_km = round(self.gas / gas_per_1_km, 2)

            self.gas = 0

            self.mileage += real_ride_km

            print(f'Проехали {real_ride_km} километров')

        else:

            self.gas -= round(gas_per_1_km * ride_km, 2)

            self.mileage += ride_km

            print(f'Проехали {ride_km} километров')

    def info(self):

        print(f'Количество бензина в баке, л: {self.gas}\nПробег, км: {self.mileage}')
