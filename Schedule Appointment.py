import random
Username = "mannatbansal"
Password = "man324ban"
def login():
    print("-------------LOGIN-------------")
    i= 4
    while i > 0:
        username = input("Enter Username:")
        password = input("Enter Password:")
        if username == Username and Password == password:
            print("\nLogin Successful 🎉")
            break
        elif username == Username and Password != password:
            print("\nIncorrect Password!")
        elif username != Username and Password == password:
            print("\nIncorrect Username!")
        else:
            print("\nIncorrect Username and Password!")
            i -= 1
        if i == 0:
            print("Too Many Attempts.... Try Again Later")
            exit()


def show_menu():
    print("\n--- Clinic Scheduler ---\n")
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Modify Appointment")
    print("4. Search Appointment")
    print("5. Cancel Appointment")

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

def doctors():
    A = slots()
    B = slots()
    C = slots()
    print(f"Dr.A : {A}\nDr.B : {B}\nDr.C : {C}\n")
    return



if __name__ == "__main__":
    print("Name: Mannat Bansal")
    print("Enrollment number: 2502140040")
    login()
    show_menu()
    need = int(input("Enter the number of what you want from menu: "))    #what does patient wants from menu
    if need == 1:
        print("\n-----VIEW AVAILABLE SLOTS-----\n")
        print("(Duration of Appointment is 15 Minutes)\n")
        doctors()
        docprefference = input("Do you have any Doctor prefference(yes/ no): ")
        if docprefference.lower() == "yes":
            docname = input("Dr. ").upper()
            booking = input("Enter time slot(HH:MM): ")
            available_slots = slots()
            if booking in available_slots:
                slot_booking = {
                    "Assigned Doctor" : f"Dr. {docname}",
                    "Slot" : f"{booking}"
                }
                print("\nSlot Confirmed")
                print(f"Assigned Doctor : Dr. {docname}")
                print(f"Slot : {booking}")
            else:
                print("🙁Slot Not Available")
        if docprefference.lower() == "no":
            choose_doctor_list= ["A","B","C"]
            choose_doctor = random.choice(choose_doctor_list)
            #print(f"Assigned Doctors: Dr.{choose_doctor}")
            print("\n-----VIEW AVAILABLE SLOTS-----\n")
            print("(Duration of Appointment is 15 Minutes)\n")
            doctor_slot = slots()
            print(f"Available Slots of Dr.{choose_doctor} : {doctor_slot}")

            bookings_choose = input("Enter time slot(HH:MM): ")
            if bookings_choose in doctor_slot:
                slot_booking = {
                "Assigned Doctor": f"Dr. {choose_doctor}",
                "Slot": f"{bookings_choose}"
            }
            print("\nSlot Confirmed")
            print(f"Assigned Doctor : Dr. {choose_doctor}")
            print(f"Slot : {bookings_choose}")


