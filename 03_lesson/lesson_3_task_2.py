from smartphone import Smartphone

Catalog = [
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79123456789"),
    Smartphone("Apple", "iPhone 15 Pro Max", "+79987654321"),
    Smartphone("Xiaomi", "13T Pro", "+79555112233"),
    Smartphone("Huawei", "P60 Pro", "+79333777999"),
    Smartphone("Honor", "Magic 5 Pro", "+79001010202")
]

for smartphone in Catalog:
    print(f"{smartphone.brand} - {smartphone.model}. "
          f"{smartphone.number}")
