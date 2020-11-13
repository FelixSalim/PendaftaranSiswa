from json import load, dump
def load_student_data():
	with open(student_table_path, "r") as studentFile:
		data = load(studentFile)
	return data
def load_user_data():	
	with open(user_table_path, "r") as userFile:
		data = load(userFile)
	return data

error = False
student_table_path = "data/student_table.json"
user_table_path = "data/user_table.json"

students = {}
users = {}

main_menu = """
Aplikasi Daftar Siswa
--------MENU AWAL-------
[ A ] = Tampilkan Daftar
[ B ] = Tambahkan Data Siswa
[ C ] = Cari Data Siswa
[ D ] = Cari Data Siswa Berdasarkan Nama
[ E ] = Hapus Data Siswa
[ F ] = Hapus Data Siswa Berdasarkan Nama
[ G ] = Perbarui Data Siswa
[ H ] = Cetak PDF Data Siswa
[ I ] = Cetak QR Siswa
[ O ] = Keluar
-------------------------
	"""