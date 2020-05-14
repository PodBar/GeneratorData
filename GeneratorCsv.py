from faker import Faker
import random as rdm
import datetime
import numpy as np
import pandas as pd
x = 300000
fake_data = Faker()


def amount_of_couches(id):
    if id == 1:
        NOC = rdm.choice(range(30, 40))
    elif id == 2:
        NOC = rdm.choice(range(61, 70))
    elif id == 3:
        NOC = rdm.choice(range(50, 61))
    elif id == 4:
        NOC = rdm.choice(range(40, 50))
    else:
        NOC = rdm.choice(range(40, 50))
    return NOC


idChange = []
idLift = [1, 2, 3, 4, 5]
idLiftChange = []
numberOfCouch = []
dateChange = []
timeChange = []
decision = ["active", "inactive"]
probabilityDecision = [0.9, 0.1]
statusLift = []
applicationStatus = []
applicationprobability = [0.95, 0.05]

for change in range(1, x):
    idChange.append(change)
    idliftToChange = rdm.choice(idLift)
    idLiftChange.append(idliftToChange)
    AmountOfCouchPerLift = amount_of_couches(idliftToChange)
    numberOfCouch.append(AmountOfCouchPerLift)
    date = fake_data.date_between_dates(date_start=datetime.date(
        2019, 11, 15), date_end=datetime.date(2020, 4, 10))
    dateChange.append(date)
    time = fake_data.time(pattern='%H:%M:%S')
    timeChange.append(time)
    status = np.random.choice(decision, p=probabilityDecision)
    statusLift.append(status)
    application = np.random.choice(decision, p=applicationprobability)
    applicationStatus.append(application)

statusChange = {"idChange": idChange, "idLiftChange": idLiftChange, "numberOfCouch": numberOfCouch,
                "dateChange": dateChange, "timeChange": timeChange, "statusLift": statusLift,
                "applicationStatus": applicationStatus}
DFSC = pd.DataFrame(statusChange)
DFSC.set_index("idChange", inplace=True)
DFSC.to_csv("DFSC.csv", index=True)
