# List - istalgan malumotni oziga qabul qiladi va uning tartib rqaqmi (0) dan boshlanadi.
number = [1,2, "Shox","Shox", True, False, [2,3,"Iscoo"]]
# List - metitlari faqat (.) bilan yoziladi.

# insert - malumotni ozimiz hohlagan joyga qoya olamiz.
number.insert(4, "Azamat")
# append - malumotni oxiriga qoshib beradi.
number.append("Hello")
# remove - "O'chirish" faqat nomi boyicha ochiradi.
number.remove("Shox")
number.remove("Shox")
# del - (Index) Orqali ochiiradi.
del number[5]
# pop - Indexdan ochirib oziga saqlab oladi yani (ctrl X) vazifasini bajaradi.
number.pop(1)
print(number)

num = [5, 4, 3, 2, 1,]
# sort - Tartibsiz raqamlarni tartiblab beradi.
num.sort()
# sort - 2- usuli tartiblab beradi.
name = [-1,2,1,3,4]
sort = sorted(name)
print(sort)
# reverse - Teskari tartiblab beradi.
num.reverse()
# copy - Nusxa olish uchun ishlatiladi yani (ctrl C) vazifasini bajaradi.
num.copy()
print(num)

ant = [3,5,]
c = ant.count(5)
# clear - Listni ichini tozalab beradi.
ant.clear()
# extend - Sozlarni orasini ochib tashlaydi: masalan (A  z  a  m  a  t) shunday.
ant.extend("Azamat")
print(ant)

nom = [1,2,3,4,5]
index = nom.index(5)
print(index)