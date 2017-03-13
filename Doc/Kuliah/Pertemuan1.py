import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa krama")
l = raw_input("Masukan Nilai 1: ")
u = raw_input("Masukan Nilai 2: ")
t = raw_input("Masukan Nilai 3: ")
f = raw_input("Masukan Nilai 4: ")
i = raw_input("Masukan Nilai 5: ")

if l == 'setunggal':
	l=1

if l == 'kalih':
	l=2

if l == 'tigo':
	l=3

if l == 'sekawan':
	l=4

if l == 'gangsal':
	l=5

if l == 'enem':
	l=6

if l == 'pitu':
	l=7

if l == 'wolu':
	l=8

if l == 'sanga':
	l=9

if l == 'sedasa':
	l=0


if u == 'setunggal':
	u=1

if u == 'kalih':
	u=2

if u == 'tigo':
	u=3

if u == 'sekawan':
	u=4

if u == 'gangsal':
	u=5

if u == 'enem':
	u=6

if u == 'pitu':
	u=7

if u == 'wolu':
	u=8

if u == 'sanga':
	u=9

if u == 'sedasa':
	u=0
	

if t == 'setunggal':
	t=1

if t == 'kalih':
	t=2

if t == 'tigo':
	t=3

if t == 'sekawan':
	t=4

if t == 'gangsal':
	t=5

if t == 'enem':
	t=6

if t == 'pitu':
	t=7

if t == 'wolu':
	t=8

if t == 'sanga':
	t=9

if t == 'sedasa':
	t=0


if f == 'setunggal':
	f=1

if f == 'kalih':
	f=2

if f == 'tigo':
	f=3

if f == 'sekawan':
	f=4

if f == 'gangsal':
	f=5

if f == 'enem':
	f=6

if f == 'pitu':
	f=7

if f == 'wolu':
	f=8

if f == 'sanga':
	f=9

if f == 'sedasa':
	f=0


if i == 'setunggal':
	i=1

if i == 'kalih':
	i=2

if i == 'tigo':
	i=3

if i == 'sekawan':
	i=4

if i == 'gangsal':
	i=5

if i == 'enem':
	i=6

if i == 'pitu':
	i=7

if i == 'wolu':
	i=8

if i == 'sanga':
	i=9

if i == 'sedasa':
	i=0


jumlah =(l*u)+(t/f-i)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))
