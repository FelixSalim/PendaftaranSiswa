from time import sleep
from os import system
from getpass import getpass
from datetime import datetime
from json import load, dump

file_path = "storage/siswa.json"
modeRead = "r"
modeWrite = "w"
daftar_siswa = {}

def load_data_apps():
	with open(file_path, modeRead) as data:
		daftar_siswa = load(data)
	return daftar_siswa

def save_data_apps():
	with open(file_path, modeWrite) as data:
		dump(daftar_siswa, data)

def buat_id():
	today = datetime.now()
	tahun = today.year
	bulan = today.month
	hari = today.day
	counter = len(daftar_siswa) + 1
	id_siswa = str("%4d%02d%02d-O%01d" % (tahun, bulan, hari, counter))
	return id_siswa

def masukkan_password():
	password = "123456789"
	pw = getpass("Masukkan Password: ")
	while pw != password:
		print("Coba Lagi")
		pw = input("Masukkan Password :")
	else:
		print("Welcome...")

def verify(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def menu():
	system("cls")
	print("--------MENU AWAL-------")
	print("[ A ] = Tampilkan Daftar")
	print("[ B ] = Tambahkan Data Siswa")
	print("[ C ] = Cari Data Siswa")
	print("[ D ] = Cari Data Siswa Berdasarkan Nama")
	print("[ E ] = Hapus Data Siswa")
	print("[ F ] = Hapus Data Siswa Berdasarkan Nama")
	print("[ G ] = Perbarui Data Siswa")
	print("[ O ] = Keluar")
	print("-------------------------")

def tampilkan_daftar():
	system("cls")
	print("---Daftar Siswa---")
	if len(daftar_siswa) == 0:
		print("Daftar Masih Kosong, Tolong Masukkan Data Terlebih Dahulu")
	else:
		for id_siswa in daftar_siswa:
			print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
			print("ID:%s\tNama:%s\tNoTelp:%s\tHobi:%s\tEmail:%s\tAlamat:%s\tJurusan: %s\tTanggalLahir:%s\tAsalSekolah:%s\tNilaiUjian:%s\t" % (id_siswa, daftar_siswa[id_siswa]["Nama"][0:5], daftar_siswa[id_siswa]["No_Telp"][2:12], daftar_siswa[id_siswa]["Hobi"][0:7], daftar_siswa[id_siswa]["Email"][0:7], daftar_siswa[id_siswa]["Alamat"][0:7], daftar_siswa[id_siswa]["Jurusan"], daftar_siswa[id_siswa]["Tanggal_Lahir"], daftar_siswa[id_siswa]["Asal_Sekolah"][0:5], daftar_siswa[id_siswa]["Nilai_Ujian"][0:1]))
			print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	input("Tekan ENTER untuk kembali ke menu")

def ambilIDdariNama(siswa):
	for id_siswa in daftar_siswa:
		if daftar_siswa[id_siswa]["Nama"] == siswa:
			return id_siswa

def tambahkan_data():
	system("cls")
	print("---Tambahkan Data---")
	id_siswa = buat_id()
	nama = input("Nama: ")
	nama = nama.title()
	no_telp = input("No Telp: ")
	hobi = input("Hobi: ")
	email = input("Email: ")
	alamat = input("Alamat: ")
	jurusan = input("Jurusan(IPA/IPS): ")
	run = True
	while run:
		try:
			tgl_lahir = int(input("Tanggal Lahir: "))
			run = False
		except ValueError:
			print("Masukkan Angka!!")
	bln_lahir = input("Bulan Lahir: ")
	run = True
	while run:
		try:
			thn_lahir = int(input("Tahun Lahir: "))
			run = False
		except ValueError:
			print("Masukkan Angka!!!")
	asal_sekolah = input("Asal Sekolah: ")
	run = True
	while run:
		try:
			nilai_ujian = int(input("Nilai Ujian Terakhir: "))
			run = False
		except ValueError:
			print("Masukkan Angka!!!")
	yakin = input("Tekan Y Untuk Menambahkan Data\t")
	if verify(yakin):
		print("Menambahkan Data, Mohon Tunggu Sebentar...")
		sleep(1)
		daftar_siswa[id_siswa] = {
			"Nama" : nama,
			"No_Telp" : no_telp,
			"Hobi" : hobi,
			"Email" : email,
			"Alamat" : alamat,
			"Jurusan" : jurusan,
			"Tanggal_Lahir" : tgl_lahir[0:2] + " " + bln_lahir[0:3] + " " +thn_lahir,
			"Asal_Sekolah" : asal_sekolah,
			"Nilai_Ujian" : nilai_ujian
		}
		save_data_apps()
		print("Data Telah Ditambahkan")
	else:
		print("Data Batal Ditambahkan")
	input("Tekan ENTER untuk kembali ke menu")

def cariNama(siswa):
	for id_siswa in daftar_siswa:
		if daftar_siswa[id_siswa]["Nama"] == siswa:
			print(f"""
	~~~~~~~~~~~~DATA DITEMUKAN~~~~~~~~~~~~
	ID\t\t\t:{id_siswa}
	Nama\t\t\t:{daftar_siswa[id_siswa]["Nama"]}
	No Telp\t\t\t:{daftar_siswa[id_siswa]["No_Telp"]}
	Hobi\t\t\t:{daftar_siswa[id_siswa]["Hobi"]}
	Email\t\t\t:{daftar_siswa[id_siswa]["Email"]}
	Alamat\t\t\t:{daftar_siswa[id_siswa]["Alamat"]}
	Jurusan\t\t\t:{daftar_siswa[id_siswa]["Jurusan"]}
	Tanggal Lahir\t\t:{daftar_siswa[id_siswa]["Tanggal_Lahir"]}
	Asal Sekolah\t\t:{daftar_siswa[id_siswa]["Asal_Sekolah"]}
	Nilai Ujian Terakhir\t:{daftar_siswa[id_siswa]["Nilai_Ujian"]}
			""")
		return True
	else:
		print("~~~~~DATA TIDAK DITEMUKAN~~~~~")
		return False

def carikan(id_siswa):
	if id_siswa in daftar_siswa:
		print(f"""
	~~~~~~~~~~~~DATA DITEMUKAN~~~~~~~~~~~~
	ID\t\t\t:{id_siswa}
	Nama\t\t\t:{daftar_siswa[id_siswa]["Nama"]}
	No Telp\t\t\t:{daftar_siswa[id_siswa]["No_Telp"]}
	Hobi\t\t\t:{daftar_siswa[id_siswa]["Hobi"]}
	Email\t\t\t:{daftar_siswa[id_siswa]["Email"]}
	Alamat\t\t\t:{daftar_siswa[id_siswa]["Alamat"]}
	Jurusan\t\t\t:{daftar_siswa[id_siswa]["Jurusan"]}
	Tanggal Lahir\t\t:{daftar_siswa[id_siswa]["Tanggal_Lahir"]}
	Asal Sekolah\t\t:{daftar_siswa[id_siswa]["Asal_Sekolah"]}
	Nilai Ujian Terakhir\t:{daftar_siswa[id_siswa]["Nilai_Ujian"]}
			""")
		return True
	else:
		print("~~~~~DATA TIDAK DITEMUKAN~~~~~")
		return False

def cari_data():
	system("cls")
	print("---Cari Data Siswa---")
	cari = input("Masukkan ID Siswa yang ingin dicari: ")
	cari = cari.title()
	yakin = input("Tekan Y Untuk Mencari Data\t")
	if verify(yakin):
		print("Sedang Mencari Data, Mohon Tunggu Sebentar...")
		sleep(1)
		carikan(cari)
	else:
		print("Pencarian Dibatalkan")
	input("Tekan ENTER untuk kembali ke menu awal")

def cari_dataNama():
	system("cls")
	print("---Cari Data Siswa---")
	cari = input("Masukkan nama Siswa yang ingin dicari: ")
	cari = cari.title()
	yakin = input("Tekan Y Untuk Mencari Data\t")
	if verify(yakin):
		print("Sedang Mencari Data, Mohon Tunggu Sebentar...")
		sleep(1)
		cariNama(cari)
	else:
		print("Pencarian Dibatalkan")
	input("Tekan ENTER untuk kembali ke menu awal")

def hapus_data():
	system("cls")
	print("---Hapus Data Siswa---")
	hapus = input("Masukkan ID Siswa yang ingin dihapus: ")
	hasil = carikan(hapus)
	if hasil:
		yakin = input("Tekan Y Untuk Menghapus Data\t")
		if verify(yakin):
			print("Sedang Menghapus Data, Mohon Tunggu Sebentar...")
			sleep(1)
			daftar_siswa.pop(hapus)
			save_data_apps()
			print(f"Data {hapus} telah di hapus")
		else:
			print("Penghapusan Dibatalkan")
	else:
		print("---------------------------------------")
		print("Kontak tidak ada, tidak dapat menghapus")
		print("---------------------------------------")
	input("Tekan ENTER untuk kembali ke menu")

def hapus_nama():
	system("cls")
	print("---Hapus Data Siswa---")
	nama = input("Masukkan Nama Siswa yang ingin dihapus: ")
	nama = nama.title()
	hasil = ambilIDdariNama(nama)
	if hasil:
		yakin = input("Tekan Y Untuk Menghapus Data\t")
		if verify(yakin):
			print("Sedang Menghapus Data, Mohon Tunggu Sebentar...")
			sleep(1)
			daftar_siswa.pop(hasil)
			save_data_apps()
			print(f"Data {nama} telah di hapus")
		else:
			print("Penghapusan Dibatalkan")
	else:
		print("---------------------------------------")
		print("Kontak tidak ada, tidak dapat menghapus")
		print("---------------------------------------")
	input("Tekan ENTER untuk kembali ke menu")

def updateNama(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	new_nama = input("Nama Baru\t: ")
	new_nama = new_nama.title()
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Nama"] = new_nama
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateTelp(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Telp Lama\t: {daftar_siswa[student]['No_Telp']}")
	new_telp = input("Telp Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["No_Telp"] = new_telp
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateHobi(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Hobi Lama\t: {daftar_siswa[student]['Hobi']}")
	new_hobi = input("Hobi Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Hobi"] = new_hobi
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateEmail(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Email Lama\t: {daftar_siswa[student]['Email']}")
	new_email = input("Email Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Email"] = new_email
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateAlamat(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Alamat Lama\t: {daftar_siswa[student]['Alamat']}")
	new_alamat = input("Alamat Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Alamat"] = new_alamat
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateJurusan(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Jurusan Lama\t: {daftar_siswa[student]['Jurusan']}")
	new_jurusan = input("Jurusan Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Jurusan"] = new_jurusan
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateTglLahir(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Tanggal Lahir Lama\t: {daftar_siswa[student]['Tanggal_Lahir']}")
	new_tglLahir = input("Tanggal Lahir Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Tanggal_Lahir"] = new_tglLahir
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateAsalSekolah(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Asal Sekolah Lama\t: {daftar_siswa[student]['Asal_Sekolah']}")
	new_asalSekolah = input("Asal Sekolah Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Asal_Sekolah"] = new_asalSekolah
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def updateNilaiUjian(student):
	ID = ambilIDdariNama(student)
	print(f"Nama\t: {student}")
	print(f"Nilai Ujian Terakhir Lama\t: {daftar_siswa[student]['Nilai_Ujian']}")
	new_nilaiUjian = input("Nilai Ujian Terakhir Baru\t: ")
	respon = input("Tekan Y untuk memperbarui\t")
	if verify(respon):
		print("Memperbarui Data....")
		sleep(1)
		daftar_siswa[ID]["Nilai_Ujian"] = new_nilaiUjian
		save_data_apps()
		print("Data telah diperbarui")
	else:
		print("Data batal diperbarui")
	input("TEKAN ENTER untuk kembali")

def perbarui_data():
	system("cls")
	print("---Perbarui Data---")
	nama = input("Masukkan nama siswa yang datanya ingin diperbarui: ")
	result = cariNama(nama)
	if result:
		print("Data yang ingin diperbarui")
		print("[ 1 ] - Nama\n[ 2 ] - No Telp\n[ 3 ] - Hobi\n[ 4 ] - Email\n[ 5 ] - Alamat\n[ 6 ] - Jurusan\n[ 7 ] - Tanggal Lahir\n[ 8 ] - Asal Sekolah\n[ 9 ] - Nilai Ujian Terakhir")
		respon = input("Pilihan: ")
		if respon == "1":
			updateNama(nama)
		elif respon == "2":
			updateTelp(nama)
		elif respon == "3":
			updateHobi(nama)
		elif respon == "4":
			updateEmail(nama)
		elif respon == "5":
			updateAlamat(nama)
		elif respon == "6":
			updateJurusan(nama)
		elif respon == "7":
			updateTglLahir(nama)
		elif respon == "8":
			updateAsalSekolah(nama)
		elif respon == "9":
			updateNilaiUjian(nama)
		else:
			print("Tolong Pilih Pilihan Yang Tersedia")
			input("Tekan ENTER untuk kembali ke menu")
	else:
		input("Tekan ENTER untuk kembali ke menu")

def userInput(Input):
	Input = Input.upper()
	if Input == "O":
		print("Sampai Jumpa...")
		return True
	elif Input == "A":
		tampilkan_daftar()
	elif Input == "B":
		tambahkan_data()
	elif Input == "C":
		cari_data()
	elif Input == "D":
		cari_dataNama()
	elif Input == "E":
		hapus_data()
	elif Input == "F":
		hapus_nama()
	elif Input == "G":
		perbarui_data()

daftar_siswa = load_data_apps()
def run():
	masukkan_password()
	Hentikan_program = False
	while not Hentikan_program:
		menu()
		user_input = input("Pilih Fungsi Yang Ingin Dijalankan: ")
		Hentikan_program = userInput(user_input)


run()


#Asal sekolah
#Nilai ujian terakhir
#Tampilan lihat semua siswa dirapiin(hanya 5 karakter string yg tampil di lihat semua data siswa)
#dicek panjang string kalau lebih dari 5 hanya tampilin [0:6]

