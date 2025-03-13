# 13.02.25

import numpy as np

# Randint
rint = np.random.randint(1, 5) #1 ve 4 arasi (5 daxil deyil) 1 integer eded
print(rint)

arr = np.random.randint(2, 6, size=[2, 3]) #2 ve 5 arasi 2x3 olculu array
print(arr)

arr1 = np.random.randint(5, size=6) #maksimum deyeri 4 olan 1x6 olculu array
print(arr1)

arr2 = np.random.randint(5, [8, 24, 52]) #her 3-unun min deyeri 5, muvafiq olaraq max deyerleri 7, 23, 51 olan 1x3 olculu array
print(f"arr2: {arr2}")


# --------------------------------------------
# Arange
#arange - mueyyen araliqlarla bir array yaradir. 
#arange(start, stop, step, dtype)
# start (optional) - default = 0 - daxildir
# stop (required) - daxil deyil
# step (optional) - default = 1 - float (0.2), menfi (-2) araliqlar da vermek olur.
# dtype (optional) - default = int

arng = np.arange(13) #0-dan 13-e qeder (13 daxil deyil) 1 vahid araliqlarla massiv
print(arng)

arng1 = np.arange(1, 13) #1-dan 13-e qeder (13 daxil deyil) 1 vahid araliqlarla massiv
print(arng1)

arng2 = np.arange(1, 13, 2) #1-den 13-e qeder (13 daxil deyil) 2 vahid araliqla massiv
print(arng2)

arng3 = np.arange(13, 1, -2) #13-den 1-e dogru (1 daxil deyil) 2 vahid menfi araliqla massiv
print(arng3)

arng4 = np.arange(1, 13, 2, dtype=float) #1-den 13-e qeder (13 daxil deyil) 2 vahid araliqla massiv (elementler float olaraq)
print(arng4)


# --------------------------------------------
# Max, Min
# max - bir massivin en boyuk elementini tapmaq ucundur.
# min - bir massivin en kicik elementini tapmaq ucundur.

marr = np.random.randint(3, 25, 5)
print(marr)
print(np.min(marr))
print(np.max(marr))


# --------------------------------------------
# Rand
# rand - randint kimidir, sadece olaraq float ededler generate edir.
# sadece 0 ve ya 1 arasinda eded generate edir. (moterizede yazilanlar massivin olculeri ucundur)
# rand(d0, d1, ..., dn)
arr_rnd = np.random.rand(3) #1x3 olculu massiv 
print(arr_rnd)

arr_rnd1 = np.random.rand(2, 3) #2x3 olculu massiv
print(arr_rnd1)

arr_rnd2 = np.random.rand(3, 3, 3) #3x3x3 olculu massiv
print(arr_rnd2)


# --------------------------------------------
# Mean
# mean - massivin elementlerinin ededi ortasini tapmaq ucundur. 
# mean(a, axis, dtype)
# a (required) - ededi ortasi tapilacaq element;
# axis (optional) - setir ve sutun uzre hesablanma (0 - sutun / 1 - setir);
# dtype (optional) - data type (default - float64)

m_arr = np.random.randint(3, 23, 5)
print(m_arr)
print(np.mean(m_arr)) #1 olculu massivin elementlerinin ededi ortasi

m_arr2 = np.random.randint(3, 23, (3, 2))
print(m_arr2)
print(np.mean(m_arr2)) #3x2 olculu massivin butun elementlerinin ededi ortasi
print(np.mean(m_arr2, axis=0)) #3x2 olculu massivin sutunlarinin ayri-ayriliqda ededi ortasi
print(np.mean(m_arr2, axis=1)) #3x2 olculu massivin setirlerinin ayri-ayriliqda ededi ortasi
print(np.mean(m_arr2, dtype=int)) #3x2 olculu massivin butun elementlerinin ededi ortasinin int-le tesviri


# --------------------------------------------
# Size
# size - massivin nece elementden ibaret oldugunu qaytarir. 
# size(a, axis)
s_arr = np.random.randint(3, 27, 5)
print(s_arr)
print(np.size(s_arr)) # 1 setirden ibaret massivin element sayi

s_arr2 = np.random.randint(3, 27, (2, 3))
print(s_arr2)
print(np.size(s_arr2, axis = 0)) #2x3 olculu massivin setir sayi
print(np.size(s_arr2, axis = 1)) #2x3 olculu massivin sutun sayi


# --------------------------------------------
# Shape
# shape - array-in olcusunu qaytarir.
# shape(a)
# a (required) olcusu sorusulacaq massiv
sh_arr = np.random.randint(3, 27, 5) #1 setirden ibaret massivlerde sadece element sayini gosterir (element_ sayi,)
print(sh_arr)
print(np.shape(sh_arr))

sh_arr2 = np.random.randint(3, 27, (2, 3)) #2 setir, 3 sutun (2x3)
print(sh_arr2)
print(np.shape(sh_arr2))

sh_arr3 = np.random.randint(3, 27, (1, 5)) #1setir, 5 sutun (1,5)
print(sh_arr3)
print(np.shape(sh_arr3))


# --------------------------------------------
# Reshape
# massivin formasini deyismek ucundur.
# reshape(a, shape)
# a (required) - yeniden formalasdirilacaq massiv
# shape (required) - yeni forma
# QEYD: MASSIVIN MOVCUD FORMASININ HASILI ILE YENI FORMASININ HASILI EYNI OLMALIDIR. (COLxROW)

rs_arr = np.random.randint(3, 27, 5)
print(rs_arr)
print(np.reshape(rs_arr, (5, 1))) #1x5 -- 5x1

rs_arr2 = np.random.randint(3, 25, (2,3))
print(rs_arr2)
print(np.reshape(rs_arr2, (3,2))) #2x3 -- 3x2
print(np.reshape(rs_arr2, (6, 1))) #2x3 -- 6x1


# --------------------------------------------
# Astype
# astype - massivin elementlerinin data type-ini deyismek ucundur.
# astype(x, dtype, copy)
# x (required) - tipi deyisdirilecek obyekt
# dtype (required) - obyektin yeni dtype-i
# copy (optional) default=True 
# True = esas array deyismir.
# False = esas array deyisir.

as_arr = np.random.randint(1, 5, 3)
print(as_arr)
print(as_arr.astype(float)) #int tipindeki bir array-in float-a cevrilmesi
print(as_arr.astype(str)) #int tipindeki bir array-in string-e cevrilmesi

as_arr1 = np.array([5.3, 7.6, 8.2, 4.3])
print(as_arr1)
print(as_arr1.astype(int)) #float tipindeki bir array-in int-e cevrilmesi (kesr hisse silinir, yalniz tam hisse qalir.)


# --------------------------------------------
# Sin, Cos
# sin ve cos muvafiq olaraq verilmis elementleri radian olaraq goturub onlarin sinus ve ya cosinusunu hesablayir.

a = np.random.randint(3, 30, 5)
print(a)
print(np.sin(a)) 
print(np.cos(a))


# --------------------------------------------
# Radians
# radians - dereceden radian-a cevirir. 

degree = np.arange(30, 91, 15)
print(degree)
print(np.radians(degree)) # derecelerin radians-a cevrilmesi


# --------------------------------------------
# Linspace
# linspace - start ve stop deyerleri arasinda belirli araqliqlarla ededler yaradir.
# linspace(start, stop, num, endpoint, retstep, dtype)
# start (required) - baslangic deyeri
# stop (required) - sonuncu deyer
# num (optional) - generate edilecek eded sayi (menfi ola bilmez / default=50)
# endpoint (bool, optional) - True = stop daxildir / False = stop daxil deyil (default = True)
# retstep (bool, optional) - True - addimi gosterir / False = addimi gostermir (default = False)
# dtype (optional) generate olunan ededlerin tipini mueyyen edir.

ls = np.linspace(5, 10, 5) #5 ve 10 arasinda 5 eded
print(ls)
ls1 = np.linspace(5, 10, 5, endpoint=False)  #5 ve 10 arasinda 5 eded (10 daxil deyil)
print(ls1)
ls2 = np.linspace(5, 10, 5, retstep=True) #5 ve 10 arasinda 5 eded (addim-la birlikde)
print(ls2)
ls3 = np.linspace(5, 10) #5 ve 10 arasinda 50 eded (default)
print(ls3)
ls4 = np.linspace(5, 10, 5, dtype=int) #5 ve 10 arasinda 5 eded int tipinde
print(ls4)


# --------------------------------------------
# Dot
# dot - iki massivin skalyar hasilini qaytarir

a = np.random.randint(5, 10, 5)
b = np.random.randint(5, 10, 5)

print(a)
print(b)
print(np.dot(a, b))

c = np.random.randint(5, 10, (2,2))
d = np.random.randint(5, 10, (2,2))
print(c)
print(d)
print(np.dot(c,d))


# --------------------------------------------
# Diff
# diff - array-in elementlerinin ferqini tapir.
# diff(a, n, axis)
# a (required) - ferqi tapilacaq massiv
# n (optional) - necenci terib? 
# axis (optional) - sutun ve ya setir
# axis = 1 - 2-ci sutundan 1-cini cixir, 1 sutun azalir.
# axis = 0 - 2-ci setirden 1-cini cixir, 1 setir azalir.
# n = 2 evvelce sutun elementlerinin ferqini tapir, sonra ferqlerin ferqini tapir.

d_arr = np.random.randint(5, 15, 3)
print(d_arr)
print(np.diff(d_arr)) 
print(np.diff(d_arr, n=2)) #2-ci tertib

d_arr2 = np.random.randint(5, 15, (2,2))
print(d_arr2)
print(np.diff(d_arr2))
print(np.diff(d_arr2, axis=0)) #setirler uzre ferq


# --------------------------------------------
# Zeros, Ones
# zeros - ancaq 0-lardan ibaret array yaradir.
# ones - ancaq 1-lerden ibaret array yaradir.

z_arr = np.zeros(5) #[0. 0. 0. 0. 0.]
o_arr = np.ones(5) #[1. 1. 1. 1. 1.]
print(z_arr)
print(o_arr)

z_arr1 = np.zeros((3, 3)) #3x3 olculu, yalniz 0-lardan ibaret
o_arr1 = np.ones((3, 3)) #3x3 olculu yalniz 1-lerden ibaret
print(z_arr1)
print(o_arr1)


# --------------------------------------------
# Eye
# Eye - diaqonali olan bir matris yaradir, esas diaqonal ancaq 1-lerden ibaret olur, qalan elementler 0.
# eye(N, M, k, dtype)
# N (required) setir sayini ifade edir.
# M (optional) sutun sayini ifade edir. Default olaraq N-le beraber olur.
# k (optional) 1-lerin hansi diaqonalda olacagini gosterir. Musbet ededde saga surusur, menfi ededde sola.
# dtype (optional) elementlerin dtype-ini mueyyen edir. Default float-dir.


print(np.eye(3)) #3x3 olculu massiv
print(np.eye(3, 4)) #3x4 olculu massiv
print(np.eye(4, k=1)) #4x4 olculu massiv, 20ci diaqonal
print(np.eye(4, k=-1)) #4x4 olculu massiv, -1 diaqonal