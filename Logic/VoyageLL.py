import datetime
import dateutil.parser
from Models.VoyageMODEL import Voyage
from Data.DataLayerAPI import DataLayer
from Logic.DestinationLL import DestinationLL
from Models.EmployeeMODEL import Employee

class VoyageLL:
    def __init__(self):
        STOP_TIME = 60 # The time between landing and takeoff at some location (in mins)
        self.__stop_time = STOP_TIME
        self.__data_layer = DataLayer()
        self.__logic_destination = DestinationLL()

    def create_voyage(self, some_voyage): # Er að vinna í þessu
        all_voyages = self.__data_layer.list_voyages()
        new_voyage_date = dateutil.parser.parse(some_voyage.get_voyage_depart_time())
        new_voyage_destination = some_voyage.get_destination()

        # Find colliding voyage indexes
        colliding_voyages = []
        for num in range(len(all_voyages)):
            voyage_date = dateutil.parser.parse(all_voyages[num].get_voyage_depart_time())
            if new_voyage_date.date() == voyage_date.date():
                if all_voyages[num].get_destination() == new_voyage_destination:
                    colliding_voyages.append(num)

        # Change flight numbers for the colliding voyages
        last_num = 0
        for num in colliding_voyages:
            voyage_date = dateutil.parser.parse(all_voyages[num].get_voyage_depart_time())
            if voyage_date < new_voyage_date:
                last_num += 2
            elif voyage_date > new_voyage_date:
                all_voyages[num].change_flight_numbers()
    
        # Get the destination number and flight time
        destination = self.__logic_destination.find_destination(new_voyage_destination)
        destination_number = destination.get_destiantion_number()
        flight_time = destination.get_fligh_time()

        # Assemble the flight numbers
        flight_num_1 = 'NA' + destination_number + str(last_num)
        flight_num_2 = 'NA' + destination_number + str(last_num + 1)

        # Find the other three dates
        arrival_1 = new_voyage_date + datetime.timedelta(minutes= int(flight_time))
        departure_2 = new_voyage_date + datetime.timedelta(minutes= (int(flight_time) + self.__stop_time))
        arrival_2 = new_voyage_date + datetime.timedelta(minutes= (int(flight_time)*2 + self.__stop_time))
        arrival_1 = arrival_1.isoformat()
        departure_2 = departure_2.isoformat()
        arrival_2 = arrival_2.isoformat()

        # Add flight numbers and dates to the new voyage
        some_voyage.add_flight_numbers_to_voyage(flight_num_1, flight_num_2)
        some_voyage.add_dates_to_voyage(arrival_1, departure_2, arrival_2)

        all_voyages.append(some_voyage)
        self.__data_layer.overwrite_voyages(all_voyages)

    def voyage_time_check(self, some_voyage):
        '''Takes a Voyage and checks to see if the departure time collides with any pre-existing voyage'''
        all_voyages = self.__data_layer.list_voyages()
        for voyage in all_voyages:
            if voyage.get_voyage_depart_time() == some_voyage.get_voyage_depart_time():
                return False
        return True

    def find_voyage(self, flight_num, date):
        all_voyages = self.__data_layer.list_voyages()
        found_voyages = []
        for voyage in all_voyages:
            if (date == voyage.get_voyage_depart_time()) and (flight_num in voyage.get_voyage_flight_numbers()):
                found_voyages.append(voyage)
        return found_voyages

    def get_all_voyages_by_date(self, from_date, to_date):
        from_date = dateutil.parser.parse(from_date).date()
        to_date = dateutil.parser.parse(to_date).date()
        all_voyages = self.__data_layer.list_voyages()
        matching_voyages = []
        for voyage in all_voyages:
            voyage_date = dateutil.parser.parse(voyage.get_voyage_depart_time())
            if from_date <= voyage_date.date() <= to_date:
                matching_voyages.append(voyage)
        return matching_voyages

    def get_all_voyages(self):
        return self.__data_layer.list_voyages()

    def add_employee_to_voyage(self, some_voyage, role, ssn):
        all_voyage = self.__data_layer.list_voyages()
        all_employees = self.__data_layer.list_employee()
        all_planes = self.__data_layer.list_airplanes()
        some_voyage = some_voyage[0]
        for num in range(len(all_voyage)):
            if (all_voyage[num].get_voyage_depart_time() == some_voyage.get_voyage_depart_time()) and (all_voyage[num].get_voyage_flight_numbers() == some_voyage.get_voyage_flight_numbers()):
                if role == "Captain":
                    voyage_airplane = some_voyage.get_airplane()
                    for plane in all_planes:
                        if plane == voyage_airplane:
                            voyage_license = plane
                    for employee in all_employees:
                        if employee == ssn:
                            if employee.get_license() == voyage_license:
                                if not employee.busy(some_voyage.get_voyage_depart_time(), some_voyage.get_arrival(), self.get_all_voyages()):  
                                    all_voyage[num].captain = ssn
                                else:
                                    return "Employee is already working on that day"
                            else:
                                return "Captains license does not match airplane on voyage!"
                elif role == "Copilot":
                    voyage_airplane = some_voyage.get_airplane()
                    for plane in all_planes:
                        if plane == voyage_airplane:
                            voyage_license = plane
                    for employee in all_employees:
                        if employee == ssn:
                            if employee.get_license() == voyage_license:
                                all_voyage[num].copilot = ssn
                            else:
                                return "Copilots license does not match airplane on voyage!"
                elif role == "Flight Service Manager":
                    all_voyage[num].fsm = ssn
                elif role == "Flight Attendant":
                    if all_voyage[num].fa1 == '':
                        all_voyage[num].fa1 = ssn
                    else:
                        all_voyage[num].fa2 = ssn
        self.__data_layer.overwrite_voyages(all_voyage)
        return "{} added to voyage".format(role)


    def get_voyage_status(self, some_voyage):
        departure_1, arrival_1, departure_2, arrival_2 = some_voyage.get_takeoff_dates()
        departure_1 = dateutil.parser.parse(departure_1)
        arrival_1 = dateutil.parser.parse(arrival_1)
        departure_2 = dateutil.parser.parse(departure_2)
        arrival_2 = dateutil.parser.parse(arrival_2)
        right_now = datetime.datetime.now()

        if right_now < departure_1:
            return 'Upcoming'
        elif departure_1 <= right_now <= arrival_1:
            des = some_voyage.get_destination()
            return 'In flight to ' + des
        elif arrival_1 < right_now < departure_2:
            des = some_voyage.get_destination()
            return 'Standby at ' + des
        elif departure_2 <= right_now <= arrival_2:
            des = some_voyage.get_home_airport()
            return 'In flight to ' + des
        elif arrival_2 < right_now:
            return 'Finished'