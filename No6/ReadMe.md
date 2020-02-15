# # Tugas No 6

#### Keterangan:

Aplikasi Web ini menggunakan Framework Django dan Python versi 3

#### Cara Menjalankan Web

1. buatlah terlebih dahulu sebuah environment pada folder "No6" dimana terdapat file ReadMe.md ini dengan cara
   untuk windows dengan CMD:

   ​	```python -m venv ENV``

   untuk Ubuntu dan OS X dengan Terminal:

   ​	```python3 -m venv ENV```

2. Aktivkan Environment dengan:

   untuk windows dengan CMD:

   ​	```ENV\bin\activate```

   untuk Ubuntu dan OS X dengan Terminal:

   ​	``` source ENV/bin/activate```

3. Masuk Kedalam Folder CRUD lalu install requirements library dengan cara:

   ​	```pip install requirements.txt``

4. Buatalah Migrations Model dengan ```python manage.py makemigrations``

5. Jalankan Migrations Model dengann ```python manage.py migrate``

6. buatalah sebuah superUser agar dapat menambahkan Cashier dan Category:

   ​	```python manage.py createsuperuser```

   isilah usernama dan password

7. jalankan server dengan ```python manage.py runserver``
8. bukalah localhost:8000

#### CRUD Cashier dan Category

​	- CRUD pada Cashier dan Category hanya dapat dilakukan oleh admin dengan masuk ke localhost:8000/admin

​	- lalu masukan usernama dan password

#### CRUD Product 

​	CRUD Product dapat dilakukan pada halaman localhost:8000

##### Contoh Data

![1](/home/alen/tes_arkademy/No6/CRUD/readMe.source/1.png)

##### Tambah data

![2](/home/alen/tes_arkademy/No6/CRUD/readMe.source/2.png)

![3](/home/alen/tes_arkademy/No6/CRUD/readMe.source/3.png)



##### Edit data

![4](/home/alen/tes_arkademy/No6/CRUD/readMe.source/4.png)