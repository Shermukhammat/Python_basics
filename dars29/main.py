class Student:
	def __init__(self, ism, familya, tyil):
		self.name = ism
		self.secondname = familya
		self.borin = tyil
		self.lable = 1
	
	def get_name(self):
		""" Talabaning ismni qaytaruvchi metid"""
		return self.name
	
	def get_lastname(self):
		return self.secondname
	
	def get_lable(self):
		return self.lable
	
	def get_age(self):
		""" Talabaning yoshni qaytaruvchi metod. yil -> hozirgi yil"""
		return 2023 - self.borin

	def introduce(self):
		return f"My name is {self.name} and my secondname is {self.secondname}! I was borin in {self.borin}."

	def set_lable(self, new_lable):
		self.lable = new_lable
		return self.lable

	def talaba_update(self):
		self.lable -= 1
		return self.lable


# student1 = Student("SHermuhammad", "Temirov", 2003)
# student1.set_lable(10)
# print(student1.get_lable())

class Science():
	"""
	Colled Science class
	"""

	def __init__(self, science_name):
		self.name = science_name
		self.number_of_students = 0
		self.students = []

	def add_students(self, talaba):
		self.students.append(talaba)
		self.number_of_students += 1
	
	def get_students_info(self):
		"""
		Print student's data
		"""
		return [student.get_name() for student in self.students]


student1 = Student("SHermuhammad", "Temirov", 2003)
student2 = Student("Napi", "Valieva", 2004)
student3 = Student("Vali", "Valiev", 2005)
student4 = Student("Bolta", "Teshaboyev", 2006)

students = [student1, student2, student3, student4]


math = Science("Liner Algebra")
for student in students:
	math.add_students(student)
# for info in math.get_students_info():
# 	print(info)

# for metod in dir(math):
# 	if metod[0] != "_":
# 		print(metod)

print(student1.__dict__)