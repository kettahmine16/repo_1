from address import Address
from mailing import Mailing

to_address = Address("104567", "Самара", "Куйбышева", "15", "2")
from_address = Address("101000", "Москва", "Тверская улица", "7", "5")

mailing = Mailing(to_address, from_address, "450", "TRK0010010")

print(mailing)
