#Medical Records will include name, age, sex, bmi, number of children and smoking status:
class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  
#Creating a new method that returns the patient's expected yearly medical fees (fictional values):
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(self.name + "'s estimated insurance costs is "+ str(estimated_cost) + " dollars.")

#Creating a new method that allows us to update those parameters and recalculate the estimated fees:
  def update_age(self, new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.")
    self.estimated_insurance_cost()

#Creating a new method to update the number of children and checking the new costs:
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    else:
      print(self.name + " has " + str(self.num_of_children) + " children.")
    self.estimated_insurance_cost()

#Creating a new method that uses a dict to store a patient's information in one convenient variable:
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information

#Creating an instance variable called patient1:
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
print(patient1.patient_profile())