from src.homework_day_1.car import Car


def test_check_default_arg():

    car = Car()

    assert car.gas == 0
    assert car.capacity == 40
    assert car.mileage == 0
    assert car.gas_per_km == 4


def test_check_custom_arg():

    car = Car(gas=10, capacity=65, gas_per_km=6, mileage=250)

    assert car.gas == 10
    assert car.capacity == 65
    assert car.gas_per_km == 6
    assert car.mileage == 250


def test_fill():

    car = Car(capacity=50)

    # Проверяем, что бак не переполняется
    car.fill(10)
    assert car.gas == 10

    # Добавляем еще 30, бак не переполняется
    car.fill(30)
    assert car.gas == 40

    # Добавляем еще 30, бак достигает максимльного значения, лишних литров - 20
    car.fill(30)
    assert car.gas == 50


def test_ride():

    car = Car(gas=50, capacity=50, gas_per_km=5, mileage=0)

    car.ride(100)

    assert car.gas == 45
    assert car.mileage == 100

    car.ride(200)

    assert car.gas == 35
    assert car.mileage == 300

    car.ride(800)  # автомобиль проедет только 700

    assert car.gas == 0
    assert car.mileage == 1000

    car.ride(800)  # попробуем проехать еще. Пробег и топливо не изменятся

    assert car.gas == 0
    assert car.mileage == 1000


def test_info():

    car = Car(gas=50, capacity=50, gas_per_km=5, mileage=1000)

    car.info()
