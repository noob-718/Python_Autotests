from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "1", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский", "10", "5")
mailing = Mailing(to_address, from_address, 1200, "1234567890ABCDEF")

print(f"Отправление {mailing.track} из {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment} в {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} -{mailing.from_address.apartment}. Стоимость {mailing.cost} рублей.")