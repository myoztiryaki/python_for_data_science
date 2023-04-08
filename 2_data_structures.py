###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set


###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
##############################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float ondalıklı ifadeler
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)  "key": value
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple (demet)
x = ("python", "ml", "ds")
type(x)

# Set (kümeler) Sözlüklerden farklı olarak : yani key ve value yok.
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.


###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2  # iki tane yıldız ** karesini almak için kullanılır.

# aralarında boşluk bırakıyoruz. Python kuralları öyle istiyor.

#######################
# Tipleri değiştirmek
#######################

int(b)  # ondalıklı sayısı int'a çevirdi.
float(a) # int sayıyı ondalıklı sayıya çevirdi.

int(a * b / 10)

c = a * b / 10

int(c)


###############################################
# Karakter Dizileri (Strings)
###############################################

print("John")
print('John')

"John"
name = "John"
name = 'John'

#######################
# Çok Satırlı Karakter Dizileri
#######################

"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name
name[0]   # köşeli paranteze sayı yazıp yazının elemanlarına ulaşabiliriz.
name[3]   # 0 dan başladığını hatırla!
name[2]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2]       # Burada 0 dan ikiye kadar olanları gösteriyor. 2 hariç.
long_str[0:10]  # 2 yi de göstersin istiyorsan 3 yazman gerek.

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str  # bu yazı içinde veri var mı diye sordu. Ancak false dedi.
                    #çünkü python büyük küçük harf sensitive. Dikkat!

"Veri" in long_str

"bool" in long_str

## \ ters slash (Backslash) olarak gördüğümüz alt satıra geçildiğini ifade ediyor.
# alt gr ? ile \

###############################################
# String (Karakter Dizisi) Metodları
###############################################

dir(str)

#######################
# len  içerisine gelen ifadenin boyut bilgisini veriyor. fonk.
#######################

name = "john"
type(name)
type(len)

len(name)
len("vahitkeskin")  # karakter sayısını verdi çıktı olarak.
len("miuul")

#######################
# upper() & lower(): küçük-büyük dönüşümleri / metod
#######################

"miuul".upper()  # küçük harfle girilmiş yazıyı komple büyük yaptı.
"MIUUL".lower()  # büyüğü küçük yaptı.

# type(upper)
# type(upper())


#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l", "p")  # Heppo AI Era oldu çıktı.

#######################
# split: böler
#######################

"Hello AI Era".split()  #  Boşluğa göre böldü.

#######################
# strip: kırpar
#######################

" ofofo ".strip()    # boşluğa göre kırpar.
"ofofo".strip("o")   # o ya göre kırpması istendi. 'fof' oldu çıktı.


#######################
# capitalize: ilk harfi büyütür
#######################

"foo".capitalize()

dir("foo")

"foo".startswith("f")  # neyle başladığını öğrenmek için kullanılır.

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır. Birden fazla veri elemanıyla çalışılabilir.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])

type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]

notes[0:2] # artık yeni değeri ile gelir.

###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes)

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler
#######################

notes
notes.append(100)

#######################
# pop: indexe göre siler
#######################

notes.pop(0) # 0 da ne varsa onu siler.

#######################
# insert: indexe ekler
#######################

notes.insert(2, 99)  # 2.indexe 99 değeri yerleştirilir.


###############################################
# Sözlük (Dictonary)
###############################################

# Değiştirilebilir.
# Sırasız. (3.7 sonra sıralı.)
# Kapsayıcı.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["CART"][1]

#######################
# Key Sorgulama
#######################

"YSA" in dictionary

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary["REG"]
dictionary.get("REG")

#######################
# Value Değiştirmek
#######################

dictionary["REG"] = ["YSA", 10]

#######################
# Tüm Key'lere Erişmek
#######################
dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()


#######################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#######################

dictionary.items()

#######################
# Key-Value Değerini Güncellemek
#######################

dictionary.update({"REG": 11})

#######################
# Yeni Key-Value Eklemek  # varsa günceller yoksa yeni olarak ekler
#######################

dictionary.update({"RF": 10})

###############################################
# Demet (Tuple)
###############################################

# - Değiştirilemez. # listeye çevirince değiştirilebilir.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)



###############################################
# Set
###############################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

#######################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
#######################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


#######################
# isdisjoint(): İki kümenin kesişimi boş mu? başında is olunca true false
                # cevap beklenen bir durum içinde oluyor.
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#######################
# isdisjoint(): Bir küme diğer kümenin alt kümesi mi?
#######################

set1.issubset(set2)
set2.issubset(set1)

#######################
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#######################

set2.issuperset(set1)
set1.issuperset(set2)

#######
# QUİZ
#######

name = "VBO_Bootcamp"
type = "new_term"
f"Name:{name} type:{type}"

total = 3.4 + 2.6
print(total)

a = 9 ** (1/2)
b = 10 / 5
a-b








