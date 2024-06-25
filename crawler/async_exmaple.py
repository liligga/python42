import asyncio
from time import perf_counter


async def cook_pasta():
    print("Готовлю пасту")
    await asyncio.sleep(7)
    print("Паста готова")
    return "Паста готова"

async def cook_sauce():
    print("Готовлю соус")
    await asyncio.sleep(4)
    print("Соус готов")
    return "Соус готов"

async def set_table():
    print("Накрываю на стол")
    await asyncio.sleep(2)
    print("Стол накрыт")
    return "Стол накрыт"

async def prepare_lunch():
    pasta_task = asyncio.create_task(cook_pasta())
    sauce_task = asyncio.create_task(cook_sauce())
    table_task = asyncio.create_task(set_table())

    results = await asyncio.gather(pasta_task, sauce_task, table_task)
    print("Обед готов: ", *results)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(prepare_lunch())
    time_taken = perf_counter() - start
    print("Все заняло ", time_taken, "с.")