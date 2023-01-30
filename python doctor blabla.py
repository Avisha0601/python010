class Doctor:
    
    def __init__(self):
        print("This is class Doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is "+str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great your heart rate is normal")
        else:
            print("Your heart rate does not seem normal, please visit the clinic")
            
class Patient(Doctor):
    
    def __init__(self, name, weight, height, heart_rates):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rates = heart_rates

    def healthCheck(self):
        print("\n Patient Name: "+ self.patient_name)
        Doctor.BMI(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
        
patient1 = Patient("Michael", 30, 0.9144, 80)
patient1.healthCheck()

patient2 = Patient("Jessica", 40, 1, 120)
patient2.healthCheck()

patient3 = Patient("Emma", 22, 1.75, 210)
patient3.healthCheck()

patient4 = Patient("Emily", 33, 0.999993, 98)
patient4.healthCheck()

patient5 = Patient("Jack", 29, 3, 149)
patient5.healthCheck()