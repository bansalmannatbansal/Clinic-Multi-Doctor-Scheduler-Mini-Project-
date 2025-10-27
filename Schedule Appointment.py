import random
Username = " "
Password = " "
def userlogin():
    Username = "mannatbansal"
    Password = "man324ban"
    print("-------------LOGIN-------------")
    i= 4
    while i > 0:
        username = input("Enter Username:")
        password = input("Enter Password:")
        if username == Username and password == Password:
            print("\nLogin Successful 🎉")
            break
        elif username == Username and password != Password:
            print("\nIncorrect Password!")
        elif username != Username and password == Password:
            print("\nIncorrect Username!")
        else:
            print("\nIncorrect Username and Password!")
        i -= 1
        if i == 0:
            print("Too Many Attempts.... Try Again Later")
            exit()

def doclogin():
    Username = "doctor"
    Password = "12345"
    print("-------------LOGIN-------------")
    i= 4
    while i > 0:
        username = input("Enter Username:").strip( )
        password = input("Enter Password:").strip( )
        if username == Username and password == Password:
            print("\nLogin Successful 🎉")
            break
        elif username == Username and password != Password:
            print("\nIncorrect Password!")
        elif username != Username and password == Password:
            print("\nIncorrect Username!")
        else:
            print("\nIncorrect Username and Password!")
        i -= 1
        if i == 0:
            print("Too Many Attempts.... Try Again Later")
            exit()


def show_menu_patient():
    print("\n-------------- Clinic Scheduler -------------\n")
    print("1. Book Appointment")
    print("2. Modify Appointment")
    print("3. Cancel Appointment")

def show_menu_doctor():
    print("\n-------------- Doctor Menu -------------\n")
    print("1. View Appointment")
    print("2. Search Appointment")

def slots(start_time = "10:00", slot_duration = 15, break_duration = 5, slot_count = 6):
    slots_available = []
    # spliting hours and minutes
    hours, minutes = start_time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    total_duration = slot_duration + break_duration

    for i in range(slot_count+1):
        slots_available.append(f"{hours:02d}:{minutes:02d}")

        #adding timegap
        minutes += total_duration
        if minutes >= 60:
            hours += 1
            minutes = minutes % 60
    return slots_available

doctors = {
    "Dr. A": {"slots": slots(), "bookings": {}},
    "Dr. B": {"slots": slots(), "bookings": {}},
    "Dr. C": {"slots": slots(), "bookings": {}},
}

def bookingdoc(patientname):
    print("\n--------------BOOK YOUR APPOINTMENT-------------\n")
    print("(Duration of Appointment is 15 Minutes)\n")

    for doc, data in doctors.items():
        print(f"{doc}: {data['slots']}")
    print()
    docprefference = input("Do you have any Doctor prefference(yes/ no): ")
    if docprefference.lower() == "yes":
        docname = input("Enter Doctor name: ").upper()
        doc_key = f"Dr. {docname}"
        if doc_key not in doctors:
            print("Invalid Doctor Name!")
            return
        available_slots = doctors[doc_key]["slots"]
        booking = input("Enter time slot(HH:MM): ")
        if booking in available_slots and booking not in doctors[doc_key]["bookings"]:
            doctors[doc_key]["bookings"][booking] = patientname
            print("\nSlot Confirmed")
            print(f"Assigned Doctor : {doc_key}")
            print(f"Slot : {booking}")
            print(f"Patient Name : {patientname}")
        else:
            print("🙁Slot Not Available")

    if docprefference.lower() == "no":
        choose_doctor_list = ["Dr. A", "Dr. B", "Dr. C"]
        choose_doctor = random.choice(choose_doctor_list)
        print("\n-----VIEW AVAILABLE SLOTS-----\n")
        print("(Duration of Appointment is 15 Minutes)\n")
        doctor_slot = doctors[choose_doctor]["slots"]
        print(f"Available Slots of {choose_doctor} : {doctor_slot}")

        bookings_choose = input("Enter time slot(HH:MM): ")
        if bookings_choose in doctor_slot:
            doctors[choose_doctor]["bookings"][bookings_choose] = patientname
            print("\nSlot Confirmed")
            print(f"Assigned Doctor : {choose_doctor}")
            print(f"Slot : {bookings_choose}")
            print(f"Patient Name : {patientname}")
        else:
            print("Slots not Available 🙁\nTry Again Tomorrow!!")


def view():
    print("\n-------------- Doctor Appointment Viewer --------------")
    print("Here are all booked appointments:\n")

    found_any = False
    for doctor_name, data in doctors.items():
        if data["bookings"]:
            found_any = True
            print(f"\n{doctor_name}'s Appointments:")
            for slotbooked, patient in data["bookings"].items():
                print(f"Slot: {slotbooked}")
                print(f"Patient: {patient}")
    if not found_any:
        print("\nNo Appointment Found!")


def modify():
    print("\n-------------- Modify Appointment --------------")
    nameofpatient = input("Enter your name: ").strip()
    found = False
    for doctorname,data in doctors.items():
        for slot_time, patient in list(data["bookings"].items()):
            if patient.lower() == nameofpatient.lower():
                found = True
                print("Current Appointment: ")
                print(f"Doctor: {doctorname}")
                print(f"Time: {slot_time}")

                modify = input("Do you want to modify your appointment(Yes/No) : ")
                if modify.lower() == "yes":
                    available = [
                    slot for slot in data["slots"]
                    if slot not in data["bookings"]
                    ]
                    print(f"Available Slots for {doctorname}: {available}")
                    if not available:
                        print("No other slots available for this doctor!")
                        return
                    newtime = input("Enter time(HH:MM): ").strip()
                    if newtime in available:
                        del data["bookings"][slot_time]
                        data["bookings"][newtime] = patient
                        print("\n✅ Appointment Modified Successfully!")
                        print(f"Doctor: {doctorname}")
                        print(f"New Slot: {newtime}")
                        return
                    if newtime not in available:
                        print("Slot not available :(")
                else:
                    print("Modification cancelled.")
    if not found:
        print("Patient not found 👀")


def search():
    print("\n-------------- Search Appointments --------------")
    searchtime = input("Enter time(HH:MM): ").strip()
    found_app = False
    for doctor_name, data in doctors.items():
        if searchtime in data["bookings"]:
            found_app = True
            print(f"\nDoctor: {doctor_name}")
            print(f"Slot: {searchtime}")
            print(f"Patient: {data['bookings'][searchtime]}")
    if not found_app:
       print("\nNo Appointment Found!")


def cancel():
    patientname = input("Enter your name:").strip()
    foundname = False
    for docname,data in doctors.items():
        for slot_time,patient in list(data["bookings"].items()):
            if patientname.lower() == patient.lower():
                foundname = True
                print("Current Appointment: ")
                print(f"Doctor: {docname}")
                print(f"Time: {slot_time}")
                cancel = input("Do you want to cancel your appointment(Yes/No) : ")
                if cancel.lower() == "yes":
                    del data["bookings"][slot_time]
                    print("\nAppointment Cancelled Successfully!!")
                elif cancel.lower() == "no":
                    print("\nThe Appointment remains the same.")
                else:
                    print("INVALID")
    if not foundname:
        print(f"\nNo Appointment under {patientname} found!")


if __name__ == "__main__":    
    print("Welcome to Clinic Appointment Scheduler\nMay us know your identity")
    print("\n1. Doctor\n2. Patient")
    
    user = int(input("Enter your Identity[1 or 2]: ").strip())
    if user == 1:
        doclogin()
        show_menu_doctor()
        need = int(input("Enter the number of what you want from menu: "))  # what does patient wants from menu
        if need == 1:
            view()
        if need == 2:
            search()


    if user == 2:
        userlogin()
        patientname = input("Enter your name:").strip()
        show_menu_patient()
        need = int(input("Enter the number of what you want from menu: ")) # what does patient wants from menu
        if need == 1:
            bookingdoc(patientname)
        if need == 2:
            modify()
        if need == 3:
            cancel()




