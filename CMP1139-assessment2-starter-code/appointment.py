""" appointment.py
"""
from abc import ABC, abstractmethod

class Decorator(ABC):
    """ Component """
    @abstractmethod
    def get_pet(self):
        pass

    @abstractmethod
    def get_notes(self):
        pass

class BaseAppointment(Decorator):
    """ Concrete Component """
    def get_pet(self):
        return ""

    def get_notes(self):
        return ""

class AppointmentDecorator(Decorator):
    """ Decorator """
    def __init__(self, decorated_appointment):
        self.decorated_appointment = decorated_appointment

    def get_pet(self):
        return self.decorated_appointment.get_pet()

    def get_notes(self):
        return self.decorated_appointment.get_notes()

# Concrete Decorators:

class VaccineDecorator(AppointmentDecorator):
    """ Concrete Decorator A """
    def get_pet(self):
        return self.decorated_appointment.get_pet()

    def get_notes(self):
        print("Please state a vaccine that was given, if none leave blank: ")
        note = input()
        if (note != ""):
            return self.decorated_appointment.get_notes() + (f", vaccination = {note}")
        else:
            return self.decorated_appointment.get_notes()

class SurgeryDecorator(AppointmentDecorator):
    """ Concrete Decorator B """
    def get_pet(self):
        return self.decorated_appointment.get_pet()

    def get_notes(self):
        print("Please state the surgery that was performed, if none leave blank: ")
        note = input()
        if (note != ""):
            return self.decorated_appointment.get_notes() + (f", surgery = {note}")
        else:
            return self.decorated_appointment.get_notes()

class Appointment:

    """
    Stores the appointment details.
    Allows notes to be entered when the appointment is attended.
    """

    def __init__(self, pet, time):
        """
        Appointment constructor

        :param pet (Pet): the pet the appointment is for
        :param time (str): A string containing the date/time of the appointment
        """
        self.pet = pet
        pet.add_appointment(self)
        self.time = time

        # notes will be added when the appointment is attended
        self.notes = []

    def attend_appointment(self):
        """
        Asks the user to enter the pet's weight and health notes.
        :param self
        """

        print("Enter pet weight: ")
        note = input()
        self.notes.append(f"weight= {note}")

        print("Enter health notes: ")
        note = input()
        self.notes.append(note)
        additions = SurgeryDecorator(VaccineDecorator(VaccineDecorator(BaseAppointment())))
        self.notes.append(additions.get_notes())

    # ---
    # getters

    def get_pet(self):
        return self.pet

    def get_notes(self):
        return self.notes
    



# EOF
# ----
