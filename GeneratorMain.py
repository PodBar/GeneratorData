from collections import Counter
from random_pesel import RandomPESEL
import random as rdm
from faker import Faker
import datetime
fake_data = Faker()
pesel = RandomPESEL()
x = 10
# miejsce pozwalające nam określić ile danych chcemy wygenerować, dane te następnie możemy
# użyć do wczytania do bazy danych za pomocą bulk.
# Client table


def check_level(clientSkillLevel):
    if clientSkillLevel == "junior":
        years = 1
    elif clientSkillLevel == "mid":
        years = 2
    else:
        years = 3
    return years


def add_years(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d + (datetime.date(d.year + years, 3, 1) - datetime.date(d.year, 3, 1))


def give_client_age_category(clientAge):
    if clientAge < 16:
        CAC = "less than 16"
    elif clientAge >= 16 and clientAge < 20:
        CAC = "between 16 and 20"
    elif clientAge >= 20 and clientAge < 27:
        CAC = "between 21 and 27"
    elif clientAge >= 27 and clientAge < 35:
        CAC = "between 28 and 35"
    elif clientAge >= 35 and clientAge < 49:
        CAC = "between 36 and 49"
    elif clientAge >= 49 and clientAge < 65:
        CAC = "between 50 and 65"
    elif clientAge >= 65 and clientAge < 75:
        CAC = "between 66 and 75"
    else:
        CAC = "more than 75"
    return CAC


CLIENT = []
CSL = ["junior", "mid", "expert"]
CS = ["female", "male"]
CG = ["very bad", "bad", "neutral", "good", "very good"]


with open("Client.txt", "w+", encoding="UTF-8") as file:
    for _ in range(1, x):
        clientPesel = pesel.generate()
        clientSex = rdm.choice(CS)
        if clientSex == "female":
            clientNameSurname = fake_data.name_female()
        else:
            clientNameSurname = fake_data.name_male()
        clientNationality = fake_data.country()
        clientSkillLevel = rdm.choice(CSL)
        clientAge = rdm.choice(range(5, 85))
        clientAgeCategory = give_client_age_category(clientAge)
        clientGrade = rdm.choice(CG)
        clientInsertDate = fake_data.date_between_dates(
            date_start=datetime.date(2019, 11, 15), date_end=datetime.date(2020, 4, 10))
        clientCheckDate = add_years(
            clientInsertDate, check_level(clientSkillLevel))
        clientRow = ("," + str(clientPesel) + "," + str(clientSex) + "," +
                     str(clientNameSurname) + "," + str(clientNationality) + "," + str(clientSkillLevel) + "," + str(clientAge) + "," +
                     str(clientAgeCategory) + "," + str(clientGrade) + "," + str(clientInsertDate) + "," + str(clientCheckDate))
        CLIENT.append(clientRow)
        C = ('\n'.join(CLIENT))
    file.write(C)

# Skipass table


def give_skipass_category_depends_on_hours(skipassTypeHour):
    if skipassTypeHour in [1, 2]:
        skipassPriceCategory = "cheap"
    elif skipassTypeHour in [3, 4, 5]:
        skipassPriceCategory = "medium"
    elif skipassTypeHour in [6, 7]:
        skipassPriceCategory = "expensive"
    return skipassPriceCategory


SKIPASS = []
SR = ["orange", "blue", "red"]

with open("Skipass.txt", "w+", encoding="UTF-8") as file:
    for skipass in range(1, x):
        skipassBelongsToClient = skipass
        skipassRange = rdm.choice(SR)
        skipassBk = pesel.generate()
        skipassTypeHour = rdm.choice(range(1, 8))
        skipassRow = ("," + str(skipassBelongsToClient) + "," + str(skipassRange) + "," + str(skipassBk) + "," + str(skipassTypeHour) +
                      "," + str(give_skipass_category_depends_on_hours(skipassTypeHour)))
        SKIPASS.append(skipassRow)
        S = ('\n'.join(SKIPASS))
    file.write(S)
# SKIPASS_TYPE table
with open("SKIPASS_TYPE.txt", "w+", encoding="UTF-8") as file:
    LSKI = [",2", ",4", ",12", ",24", ",48", ",72", ",168"]
    t = ('\n'.join(LSKI))
    file.write(t)
# PRICE_LIST table
with open("PRICE_LIST.txt", "w+", encoding="UTF-8") as file:
    price1 = [40, 1]
    price2 = [60, 2]
    price3 = [70, 3]
    price4 = [100, 4]
    price5 = [190, 5]
    price6 = [240, 6]
    price7 = [560, 7]
    PriceList = [price1, price2, price3, price4, price5, price6, price7]
    for line in PriceList:
        file.write("," + str(line)[1:-1] + "\n")
# GATEPASSING


def time_of_day_given_by_interval(hours):
    if hours < 9:
        interval_time = "between 0 and 8"
    elif hours < 13 and hours >= 9:
        interval_time = "between 9 and 12"
    elif hours < 16 and hours >= 13:
        interval_time = "between 13 and 15"
    elif hours < 20 and hours >= 16:
        interval_time = "between 16 and 20"
    else:
        interval_time = "between 21 and 23"
    return interval_time


amountOfScans = []
GPL = [1, 2, 3, 4, 5]
GATE = []
weekDays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
monthName = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']

with open("GATEPASSING.txt", "w+", encoding="UTF-8") as file:
    for _ in range(3 * x):
        gatePassingDate = fake_data.date_between_dates(
            date_start=datetime.date(2019, 11, 15), date_end=datetime.date(2020, 4, 10))
        gatePassingTime = fake_data.time(pattern='%H:%M:%S')
        t = list(map(int, str(gatePassingTime).split(':')))
        hours = datetime.time(t[0], t[1], t[2]).hour
        IntervalTimeOfDay = time_of_day_given_by_interval(hours)
        minutes = datetime.time(t[0], t[1], t[2]).minute
        seconds = datetime.time(t[0], t[1], t[2]).second
        gatePassingBySkipass = rdm.choice(range(1, x))
        amountOfScans.append(gatePassingBySkipass)
        gatePassingLift = rdm.choice(GPL)
        d = list(map(int, str(gatePassingDate).split('-')))
        day = datetime.date(d[0], d[1], d[2]).weekday()
        gatePassingDayOfWeek = weekDays[day]
        month = datetime.date(d[0], d[1], d[2]).month
        gatePassingNameOfMonth = monthName[month - 1]
        gatePassingYear = datetime.date(d[0], d[1], d[2]).year
        weekNumber = gatePassingDate.isocalendar()[1]
        gateRow = ("," + str(gatePassingDate) + "," +
                   str(gatePassingTime) + "," + str(gatePassingBySkipass) + "," + str(gatePassingLift) + "," +
                   str(gatePassingDayOfWeek) + "," + str(gatePassingNameOfMonth) + "," + str(gatePassingYear) + "," +
                   str(hours) + "," + str(minutes) + "," + str(seconds) + "," + str(IntervalTimeOfDay) + "," + str(weekNumber))
        GATE.append(gateRow)
        G = ('\n'.join(GATE))
    file.write(G)

with open("counter.txt", "w+", encoding="UTF-8") as file:
    amountOfScansPerSkier = dict(Counter(amountOfScans))
    for elements in amountOfScansPerSkier.items():
        file.write(str(elements).replace(
            "(", "").replace(" ", "").replace(")", "") + '\n')

# LIFT_TYPE
with open("LIFT_TYPE.txt", "w+", encoding="UTF-8") as file:
    LIFT_TYPE = [",drag ski lift", ",ski couch"]
    F = ('\n'.join(LIFT_TYPE))
    file.write(F)

# Lift Table

with open("LIFT.txt", "w+", encoding="UTF-8") as file:
    lift1 = ["Pasieka", 290, "between 0 and 300",
             "between 1 and 2 min", 1, "single", "between 30 and 40"]
    lift2 = ["Banach", 400, "between 300 and 500",
             "between 1 and 2 min", 1, "single", "more than 60"]
    lift3 = ["Poniat", 800, "between 500 and 1000",
             "between 2 and 3 min", 1, "double", "between 50 and 60"]
    lift4 = ["Batory", 1200, "between 500 and 1000",
             "between 3 and 4 min", 2, "quadruple", "between 40 and 50"]
    lift5 = ["Boltzman", 1600, "more than 1000",
             "more than 4 min", 2, "six-seater", "between 40 and 50"]
    row_lift = [lift1, lift2, lift3, lift4, lift5]
    for lift in row_lift:
        routeLength = 1.5 * lift[1]
        lift.append(round(routeLength))
    for line in row_lift:
        file.write("," + ', '.join(map(str, line)) + "\n")
