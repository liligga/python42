from time import sleep, perf_counter


def cook_pasta():
    print("Готовлю пасту")
    sleep(7)
    print("Паста готова")

def cook_sauce():
    print("Готовлю соус")
    sleep(4)
    print("Соус готов")

def set_table():
    print("Накрываю на стол")
    sleep(2)
    print("Стол накрыт")

def prepare_lunch():
    cook_pasta()
    cook_sauce()
    set_table()


if __name__ == "__main__":
    start = perf_counter()
    prepare_lunch()
    time_taken = perf_counter() - start
    print("Все заняло ", time_taken, "с.")