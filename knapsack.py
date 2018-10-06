from collections import namedtuple


Item = namedtuple('Item', 'name weight value')


def pack(items, max_weight):
    res_items = []
    value = 0
    used = 0
    objects = sorted(items,
                     key=lambda x: float(x.value) / x.weight, reverse=True)
    for obj in objects:
        if obj.weight + used <= max_weight:
            res_items.append(obj)
            used += obj.weight
            value += obj.value
    return res_items, value, used


if __name__ == "__main__":
    items = [
        Item("map", 9, 150),
        Item("compass", 13, 35),
        Item("water", 153, 200),
        Item("sandwich", 50, 160),
        Item("glucose", 15, 60),
        Item("tin", 68, 45),
        Item("banana", 27, 60),
        Item("apple", 39, 40),
        Item("cheese", 23, 30),
        Item("beer", 52, 10),
        Item("suntan cream", 11, 70),
        Item("camera", 32, 30),
        Item("T - shirt", 24, 15),
        Item("trousers", 48, 10),
        Item("umbrella", 73, 40),
        Item("waterproof trousers", 42, 70),
        Item("waterproof overclothes", 43, 75),
        Item("note - case", 22, 80),
        Item("sunglasses", 7, 20),
        Item("towel", 18, 12),
        Item("socks", 4, 50),
        Item("book", 30, 10)
    ]
    weight = 400
    packed_items, packed_value, packed_weight = pack(items, weight)
    print("Total value: ", packed_value)
    print("Total value: ", packed_weight)
    for item in packed_items:
        print(item[0])
