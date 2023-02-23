
# Imports
import sys
import time
import threading
from queue import Queue

# Pet Age Related Variables
PetAge_lock = threading.Lock()
PetAge = 1
Pet_Age_Check_A = 1
Pet_Age_Increase_Age_Time_Value = 10
Maximum_Pet_Age_Value = 10

# Hunger Time Start Variable - supposed to be 0
start_time_hunger = time.time()

# Age Time Start Variable - supposed to be 0
start_time_age = time.time()

# Pet Feeding Function Variable for queue
FeedingInputValue = ""
Feeding_Hunger_Start_Value = 10 - PetAge
Feeding_Hunger_Value_Multiplier = 0.3
Feeding_Hunger_Value = int(Feeding_Hunger_Start_Value * Feeding_Hunger_Value_Multiplier)

# Hunger Related Variables
Hunger_lock = threading.Lock()
Hunger = 10
Hunger_Check_A = 10
Hunger_Decrease_Hunger_Time_Value = 5
Maximum_Hunger_Value = 10
Hunger_Decrease_Value_Base = 3
Hunger_Decrease_Multiplier = 0.2
Hunger_Decrease_Value = (PetAge * Hunger_Decrease_Value_Base * Hunger_Decrease_Multiplier)

# Death Flag Variables
Death_Flag = False


#---------------------------------------------------------------------------------------------------------------
# PET AGE LOOP FUNCTION
def Pet_Age_Loop():

    # Pet Age Variables
    global PetAge
    global Pet_Age_Check_A
    global Pet_Age_Increase_Age_Time_Value
    global Death_Flag

    # Time Check for Pet Age
    start_time_age = time.time()
    while PetAge < Maximum_Pet_Age_Value and Death_Flag is False:

        # Pet Age time tracker and reset
        current_time_age = time.time()

        # Pet Age tick up condition, checking time passed and first age checkpoint
        if current_time_age - start_time_age > Pet_Age_Increase_Age_Time_Value:
            Pet_Age_Check_A = PetAge
            PetAge += 1
            start_time_age = current_time_age

    time.sleep(0.5)

#----------------------------------------------------------------------------------------------------------------
# PET HUNGER LOOP FUNCTION
def Pet_Hunger_Loop():

    # Pet Hunger Variables
    global Hunger
    global Hunger_Check_A
    global Hunger_Decrease_Hunger_Time_Value
    global Death_Flag
    global Hunger_Decrease_Value
    global PetAge

    # Time Check for Pet Hunger
    start_time_hunger = time.time()
    while Hunger > int(0) and Death_Flag is False:
        Hunger_lock.acquire()

        # Pet Hunger time tracker and reset
        current_time_hunger = time.time()

        # Pet Hunger tick down condition, checking time passed and first hunger checkpoint
        if current_time_hunger - start_time_hunger > Hunger_Decrease_Hunger_Time_Value:
            Hunger_Decrease_Value = (PetAge * Hunger_Decrease_Value_Base * Hunger_Decrease_Multiplier)
            Hunger_Check_A = Hunger
            Hunger = Hunger - int(Hunger_Decrease_Value)
            start_time_hunger = current_time_hunger
        Hunger_lock.release()

    # Prevents program getting out of control
    time.sleep(0.5)

#---------------------------------------------------------------------------------------------------------------
# FEED PET FUNCTION
def Feeding_Pet_Function():
    global Hunger
    global FeedingInputValue
    global Death_Flag

    while Death_Flag is False:

        # Feed Pet Queue function
        Feeding_Queue = Queue()

        # Input check for feeding pet and Pet Feed Value
        print()
        FeedingInputValue = input("Press f to feed your pet.")
        if FeedingInputValue == "f":
            Feeding_Queue.put(Feeding_Hunger_Value)

        # Checks if feeding queue is not empty. If not, adds the Feeding Value to the queue and increases hunger
        if not Feeding_Queue.empty():
            Hunger_lock.acquire()
            Feeding_Value_Increase = Feeding_Queue.get()
            Hunger += Feeding_Value_Increase

            # Maximum Hunger Value
            if Hunger > Maximum_Hunger_Value:
                Hunger = Maximum_Hunger_Value

            # Releasing Hunger Lock and Print
            Hunger_lock.release()
            print()
            print("You fed your pet. Your pet is at", Hunger, "/", Maximum_Hunger_Value, "food.", end="\n")

    # Prevents program getting out of control
    time.sleep(0.5)

#---------------------------------------------------------------------------------------------------------------
# PET VARIABLE CHECK FUNCTION
def Check_Pet_Values_Loop():
    global Hunger
    global PetAge
    global Hunger_Check_A
    global Pet_Age_Check_A
    global Death_Flag

    while Death_Flag is False:
        # Checks current pet variables and prints current stats.

        # Hunger Check and Pet Age Chek
        if Hunger > int(0) and PetAge < Maximum_Pet_Age_Value:
            if Hunger_Check_A != Hunger:
                Hunger_Check_A = Hunger
                print()
                print("Your pet is at", Hunger, " /", Maximum_Hunger_Value, "food.", end="\n")

            # Pet Age Print Check
            if Pet_Age_Check_A != PetAge:
                Pet_Age_Check_A = PetAge
                print()
                print("Your pet is", PetAge, " years old.", end="\n")

        # Checks if pet has died of hunger > 0. Code ends at break
        elif Hunger < int(1):
            print()
            print("Your pet died of starvation. Great work.", end="\n")
            Death_Flag = True
        # Checks if pet has died of age > Max Age Value
        elif PetAge > (Maximum_Pet_Age_Value - 1):
            print()
            print("Your pet died of old age. Great work.", end="\n")
            Death_Flag = True

    # Prevents program getting out of control
    time.sleep(0.5)

#---------------------------------------------------------------------------------------------------------------
# LOOP THREADS
Age_Thread = threading.Thread(target=Pet_Age_Loop)
Hunger_Thread = threading.Thread(target=Pet_Hunger_Loop)
Feeding_Thread = threading.Thread(target=Feeding_Pet_Function)
Check_Thread = threading.Thread(target=Check_Pet_Values_Loop)

# START THREADS
Hunger_Thread.start()
Age_Thread.start()
Feeding_Thread.start()
Check_Thread.start()
#-----------------------------------------------------------------------------------------------------------------