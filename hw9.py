class Patient:
    next_id = 1

    def __init__(self, last_name, first_name, age, address):
        self.id = Patient.next_id
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.address = address
        Patient.next_id += 1


class PatientsDb:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients.update({patient.id: patient})

    def get_patients(self):
        return list(self.patients.values())

    def get_patient_by_id(self, patient_id):
        return self.patients.get(patient_id)


def main():
    db = PatientsDb()

    while True:
        command = input("Enter command: ")
        if command == "stop":
            break

        if command == "add":
            """
            Спрашивать по отдельности фамилию, имя, возраст, адрес
            Печатать сообщение об успешности добавления пациента в БД
            """
            last_name = input("Enter patient's last name: ")
            last_name = last_name[0].upper() + last_name[1:]    # Capitalizing the 1st letter
            first_name = input("Enter patient's first name: ")
            first_name = first_name[0].upper() + first_name[1:]
            age = int(input("Enter patient's age: "))
            address = input("Enter patient's city: ")
            address = address[0].upper() + address[1:]
            patient = Patient(last_name, first_name, age, address)
            db.add_patient(patient)

        if command == "list":
            print("List of patients:")
            for patient in db.get_patients():
                print(patient.id, patient.last_name, patient.first_name, patient.age, patient.address)

        if command == "get_by_id":
            patient_id = int(input("Enter patient's id: "))
            patient = db.get_patient_by_id(patient_id)
            if not patient:
                print(f"Patient with id {patient_id} not found")
            else:
                print(patient.id, patient.last_name, patient.first_name, patient.age, patient.address)



if __name__ == '__main__':
   main()


