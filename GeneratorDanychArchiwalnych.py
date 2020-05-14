import random as rdm
from faker import Faker
import datetime
import pandas as pd
fake_data = Faker()
x = 300000
# Skipass sheet
CSL = ["junior", "mid", "expert"]
skipassId = []
CG = ["very bad", "bad", "neutral", "good", "very good"]
SR = ["orange", "blue", "red"]
CLS = [2, 4, 12, 24, 48, 72, 168]
skipassRangeSum = []
clientSkillLevelSum = []
clientAgeSum = []
clientGradeSum = []
clientDateSkipassSum = []
clientLengthSkipassSum = []

for skipass in range(1, 3 * x):
    skipassId.append(skipass)
    skipassRange = rdm.choice(SR)
    skipassRangeSum.append(skipassRange)
    clientSkillLevel = rdm.choice(CSL)
    clientSkillLevelSum.append(clientSkillLevel)
    clientAge = rdm.choice(range(5, 85))
    clientAgeSum.append(clientAge)
    clientGrade = rdm.choice(CG)
    clientGradeSum.append(clientGrade)
    clientDateSkipass = fake_data.date_between_dates(
        date_start=datetime.date(2018, 11, 15), date_end=datetime.date(2019, 4, 10))
    clientDateSkipassSum.append(clientDateSkipass)
    clientLengthSkipass = rdm.choice(CLS)
    clientLengthSkipassSum.append(clientLengthSkipass)

skipassAllSeason2018_2019 = {"skipass": skipassId, "skipassRange": skipassRangeSum, "clientSkillLevel": clientSkillLevelSum,
                             "clientAge": clientAgeSum, "clientGrade": clientGradeSum, "clientDateSkipass": clientDateSkipassSum,
                             "clientLengthSkipass": clientLengthSkipassSum}

DFSAS = pd.DataFrame(skipassAllSeason2018_2019)
DFSAS.set_index("skipass", inplace=True)
DFSAS.to_csv("DFSAS.csv", index=True)

# All sheet
amountJuniors = []
amountMids = []
amountExperts = []
howManyLiftsActives = []
SUMs = []
dateCalender = pd.date_range(start="2018-11-15", end="2019-04-10")
for date in dateCalender:
    amountJunior = rdm.choice(range(1, x))
    amountJuniors.append(amountJunior)
    amountMid = rdm.choice(range(1, x))
    amountMids.append(amountMid)
    amountExpert = rdm.choice(range(1, x))
    amountExperts.append(amountExpert)
    SUM = amountJunior + amountMid + amountExpert
    SUMs.append(SUM)
    howManyLiftsActive = rdm.choice(range(2, 6))
    howManyLiftsActives.append(howManyLiftsActive)

AllDays = {"date": dateCalender, "amountJunior": amountJuniors, "amountMid": amountMids, "amountExpert": amountExperts,
           "AllSkiers": SUMs, "howManyLiftsActive": howManyLiftsActives}

AD = pd.DataFrame(AllDays)
AD.set_index("date", inplace=True)
AD.to_csv("AD.csv", index=True)
