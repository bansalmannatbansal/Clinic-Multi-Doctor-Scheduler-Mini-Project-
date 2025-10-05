from datetime import datetime
def show_menu():
    print("\n--- Clinic Scheduler ---\n")
    print("1. Book Appointment")
    print("2. Cancel Appointment")


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
    return f"Dr.A : {A}\nDr.B : {B}\nDr.C : {C}\n"



if __name__ == "__main__":
    show_menu()
    need = int(input("Enter the number of what you want from menu:"))
    if need == 1:
        print("\n-----VIEW AVAILABLE SLOTS-----\n")
        print("(Duration of Appointment is 15 Minutes)\n")
        print(doctors())