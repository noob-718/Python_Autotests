from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "iPhone 15", "+79201234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79001234567"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79301234567"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79101234567"))
catalog.append(Smartphone("Google", "Pixel 8", "+79001234568"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")