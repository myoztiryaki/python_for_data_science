# CASE 1

#######################
# Görev 1
#######################

"""Verilen değerlerin veri yapılarını inceleyiniz."""

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

type(tipler[0])

type(x)
type(y)

tipler = [x, y, z, a, b, c, l, d, t, s]

for tip in tipler:
    print(tip)

for index, tip in enumerate(tipler):
    print(index, tip)

def tipfonk(tip):
    for i in tip:
        print(type(i))
    for i in enumerate(tip):
        print(i[0], type(i[1]))

tipfonk(tipler)

#######################
# Görev 2
#######################

"""Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
kelime kelime ayırınız."""

text = "The goal is to turn data into information, and information into insight."

text_2 = text.upper()

text_3 = text_2.replace(",", " ").replace(".", " ")

text_3.split()

#######################
# Görev 3
#######################

"""Verilen listeye aşağıdaki adımları uygulayınız."""

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

len(lst)
lst[0]
lst[10]

type(lst)

lst[0:4]

lst.pop(8)
print(lst)

lst.append("K")

lst.insert(8,"N")

#######################
# Görev 4
#######################

"""Verilen sözlük yapısına aşağıdaki adımları uygulayınız."""

dict = {"Christian" : ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

dict.keys()
dict.values()

dict["Daisy"]=["England",13]
print(dict)

dict.update({"Ahmet": ["Turkey", 24]})
print(dict)

dict.pop("Antonio")

#######################
# Görev 5
#######################

"""Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız."""

l = [2,3,18,93,22]

def ayrilacak_listeler(l):
    even_list = []
    odd_list = []
    for sayi in l:
        if sayi % 2 == 0:
            even_list.append(sayi)
        else:
            odd_list.append(sayi)
    return even_list, odd_list

even_list, odd_list = ayrilacak_listeler(l)

print("Çift sayılar:", even_list)
print("Tek sayılar:", odd_list)

ayrilacak_listeler(l)

#######################
# Görev 6
#######################

"""Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız."""

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for ogrenci in ogrenciler:
    print(ogrenci)

def ayrilacak_ogrenciler(ogrenciler):
    Muhendislik_Fakultesi = []
    Tip_Fakultesi = []
    for index, ogrenci in enumerate(ogrenciler):

        if index <=2:
            Muhendislik_Fakultesi.append(ogrenci)
            print("Mühendislik Fakültesi", (index +1), ". öğrenci:", ogrenci)
        else:
            Tip_Fakultesi.append(ogrenci)
            print("Tıp Fakültesi:", (index -2), ". öğrenci:", ogrenci)

ayrilacak_ogrenciler(ogrenciler)

#######################
# Görev 7
#######################

"""Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
almaktadır. Zip kullanarak ders bilgilerini bastırınız."""

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu,kredi, kontenjan))

for i in list(zip(ders_kodu,kredi, kontenjan)):

    print(f""" Kredisi {i[1]} olan {i[0]} kodlu dersin kontenjanı {i[2]} kişidir""")

#######################
# Görev 8
#######################

"""Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir."""

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume1.issuperset(kume2)
kume2.difference(kume1)

def kumelerim(x,y):
    if x in y:
        print(x.symmetric_difference(y))
    else:
        print(y.difference(x))

kumelerim(x=kume1, y=kume2)

#######################
# Mülakat Sorusu
#######################

"""Amaç: Çift sayıların karesi alınarak bir sözlüğe eklemek"""

numbers = range(10)
new_dict = {}

{k: v**2 if k in numbers % 2 = 0, for (k,v) in new_dict{}}

##############################################
##############################################

# CASE 2

#######################
# Görev 1
#######################

"""List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
harfe çeviriniz ve başına NUM ekleyiniz."""

import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

#######################
# Görev 2
#######################

"""List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız."""

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

#######################
# Görev 3
#######################

"""List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz."""

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]   #yani dataframe
new_df.head()

#######################
# PANDAS GÖREVLER
#######################

import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#######################
# GÖREV 1
#######################

"""Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız."""

df = sns.load_dataset("titanic")
df.head()
df.shape

#######################
# GÖREV 2
#######################
""" Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz. """

df.head()
df["sex"].head()
df["sex"].value_counts()

# male      577
# female    314

#######################
# GÖREV 3
#######################

"""Her bir sutuna ait unique değerlerin sayısını bulunuz."""

df.nunique()

#######################
# GÖREV 4
#######################

"""pclass değişkeninin unique değerlerinin sayısını bulunuz."""

df["pclass"].unique()

#######################
# GÖREV 5
#######################

""" pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz."""

df[["pclass", "parch"]].nunique()

#######################
# GÖREV 6
#######################

"""embarked değişkeninin tipini kontrol ediniz. 
Tipini category olarak değiştiriniz ve tekrar kontrol ediniz."""

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

#######################
# GÖREV 7
#######################

"""embarked değeri C olanların tüm bilgelerini gösteriniz."""

df[df["embarked"] == "C" ].head()

#######################
# GÖREV 8
#######################

"""embarked değeri S olmayanların tüm bilgelerini gösteriniz."""

df[df["embarked"] != "S" ].head()

#######################
# GÖREV 9
#######################

"""Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz."""

df[(df["sex"] == "female") & (df["age"] < 30)].head()

#######################
# GÖREV 10
#######################

"""Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz."""

df[(df["fare"] > 500) | (df["age"] > 70)].head(10)

# veya yı gösteren | bu işaret

#######################
# GÖREV 11
#######################

"""Her bir değişkendeki boş değerlerin toplamını bulunuz."""

df.isnull().sum()

#######################
# GÖREV 12
#######################

"""who değişkenini dataframe’den çıkarınız."""

df.drop("who", axis=1, inplace=True)

# axis ile sutun olduğunu 1 ile belirttik. inplace ile değişikliği kalıcı hale getirdik.

#######################
# GÖREV 13
#######################

"""deck değikenindeki boş değerleri deck değişkenin en çok 
tekrar eden değeri (mode) ile doldurunuz."""

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()


#######################
# GÖREV 14
#######################

"""age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz."""

df["age"].isnull().sum()
df["age"].median()
df["age"].fillna(df["age"].median(), inplace=True)

#######################
# GÖREV 15
#######################

"""survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, 
count, mean değerlerini bulunuz."""

df.groupby(["pclass","sex"]).agg({"survived": ["sum", "count", "mean"]})

#######################
# GÖREV 16
#######################

"""30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon 
yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir 
değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)"""

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))

# ayrı fonksiyon kullanmadan kısa yol
df["age_flag"] = df["age"].apply(lambda x : 1 if x < 30 else 0)

df.head()

#######################
# GÖREV 17
#######################

"""Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız."""

import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = sns.load_dataset("tips")
df.head()
df.shape

#######################
# GÖREV 18
#######################

"""Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, 
min, max ve ortalamasını bulunuz."""

df.groupby(["time"]).agg({"total_bill": ["sum","min","mean","max"]})

#######################
# GÖREV 19
#######################

"""Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz."""

df.groupby(["day", "time"]).agg({"total_bill": ["sum","min","mean","max"]})

#######################
# GÖREV 20
#######################

"""Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını,
min, max ve ortalamasını bulunuz."""

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","mean","max"],
                                                                "tip": ["sum","min","mean","max"]})

#######################
# GÖREV 21
#######################

"""size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? 
(loc kullanınız)"""

df.loc[(df["size"] < 3 ) & (df["total_bill"] > 10), "total_bill"].mean()

#######################
# GÖREV 22
#######################

"""total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği
totalbill ve tip in toplamını versin."""

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

#######################
# GÖREV 23
#######################

"""total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi 
yeni bir dataframe'e atayınız."""


new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape
new_df.head()

#####################################################################
#####################################################################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df["sex"].describe([0.25,0.50,0.75])

#####################################################################
######################################################
# Bitirme soruları


number = input()

type(number)

123//34
23/9
21//0

def calc(wage, hour):
    return int(wage * hour)

calc(10,40)-200

import random

def toss_coin():
    T = random.randrange(0,2)
    H = random.randrange(0,2)
    return T, H
toss_coin()


def sqr_root(x):
    sqr_r = x ** (1/2)

sqr_root(16)

import numpy as np
from functools import reduce

num_list = np.arange(10)

filter_list = list(filter(lambda x: x % 3 == 0, num_list))
final_list = reduce(lambda x, y: x * y, filter_list)

final_list

import numpy as np
serie = np.arange(1,10)

x = [3, 4, 5]

serie[x]

import seaborn as sns
df = sns.load_dataset("titanic")

df[["sex", "survived"]].groupby("sex")

sns.violinplot()

#####################################################################
#############################################################

# CASE STUDY 3

#####################################################################
#############################################################
    # Kural Tabanlı Sınıflandırma ile
# Potansiyel Müşteri Getirisi Hesaplama

import pandas as pd
import seaborn as sns
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

########################
# Görev 1   ############
########################

# 1

df = pd.read_excel("miuul_gezinomi.xlsx")
df.head()
df.value_counts()
df["SaleId"].value_counts()

# 2

df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# 3

df["ConceptName"].nunique()

# 4

df["ConceptName"].value_counts()


# 5

df["SaleCityName"].value_counts()
df.groupby("SaleCityName").agg({"Price": ["sum"]})

# 6

df["ConceptName"].value_counts()
df.groupby("ConceptName").agg({"Price": ["sum"]})

#  7

df.groupby("SaleCityName").agg({"Price": ["mean"]})

#  8

df.groupby("ConceptName").agg({"Price": ["mean"]})

# 9

df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": ["mean"]})

########################
# Görev 2   ############
########################


bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

df.head()

