from datetime import datetime
import pandas as pd


class LabMember:
    def __init__(self, name, group, last_talk, last_jc):
        self.name = name
        self.group = group
        self.last_talk = datetime.strptime(last_talk, "%Y-%m-%d")
        self.last_jc = datetime.strptime(last_jc, "%Y-%m-%d")

    def __repr__(self):
        return '{}'.format(self.name)


def select_group_member(lab_members, group):
    group_members = []
    for lab_member in lab_members:
        if lab_member.group == group:
            group_members.append(lab_member)
    return group_members


def select_lab_talk_person(pool):
    pool.sort(key=lambda x: x.last_talk, reverse=True)
    return pool[-1]


def select_jc_person(pool):
    pool.sort(key=lambda x: x.last_jc, reverse=True)
    return pool[-1]


# initiate group order of lab talk (copied from previous schedule)
# lab_talk_order = ['green', 'green', 'blue', 'blue', 'pink', 'pink', 'green', 'green', 'blue', 'blue', 'pink',
#                   'pink', 'green', 'green', 'blue']
lab_talk_order = ['green', 'pink', 'blue', 'green', 'pink', 'blue', 'pink', 'blue', 'green', 'pink', 'blue']
# initiate group order of journal club (copied from previous schedule)
# jc_order = ['blue', 'pink', 'pink', 'green', 'green', 'blue', 'blue', 'pink', 'pink', 'green', 'green', 'blue',
#             'blue', 'pink', 'pink']
jc_order = ['green', 'pink', 'blue', 'green', 'pink', 'blue', 'pink', 'blue', 'green', 'pink', 'blue']
# initiate dates of lab meetings
# dates = ['2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08', '2021-02-15', '2021-02-22',
#          '2021-03-01', '2021-03-08', '2021-03-15', '2021-03-22', '2021-03-29', '2021-04-05', '2021-04-12', '2021-04-19']
dates = ['2021-04-12', '2021-04-19', '2021-04-26', '2021-05-03', '2021-05-10', '2021-05-17', '2021-05-31', '2021-06-07', '2021-06-14', '2021-06-21', '2021-06-28']

for i in range(len(dates)):
    dates[i] = datetime.strptime(dates[i], "%Y-%m-%d")
# initiate lab members (update information here)
lab_members = []
ALM = LabMember('Adele', 'blue', '2021-03-15', '2021-01-11')
lab_members.append(ALM)
CH = LabMember('Chuanli', 'pink', '2021-02-08', '2021-01-25')
lab_members.append(CH)
LM = LabMember('Lucia', 'blue', '2021-03-08', '2020-12-07')
lab_members.append(LM)
ANU = LabMember('Anu', 'blue', '2021-02-01', '2021-02-15')
lab_members.append(ANU)
BM = LabMember('Bettina', 'pink', '2021-3-22', '2021-03-08')
lab_members.append(BM)
LW = LabMember('Lily', 'green', '2021-01-11', '2021-03-22')
lab_members.append(LW)
WB = LabMember('Wera', 'green', '2021-01-18', '2021-03-15')
lab_members.append(WB)
BS = LabMember('Bessie', 'blue', '2020-11-02', '2021-03-29')
lab_members.append(BS)
LK = LabMember('Lori', 'pink', '2021-03-29', '2021-03-01')
lab_members.append(LK)
ML = LabMember('Melanie', 'green', '2021-02-22', '2020-11-30')
lab_members.append(ML)
DK = LabMember('Dilara', 'blue', '2021-01-25', '2021-02-22')
lab_members.append(DK)
MPJ = LabMember('Meg', 'pink', '2021-02-15', '2020-12-14')
lab_members.append(MPJ)
OP = LabMember('Ola', 'pink', '2020-11-30', '2021-01-18')
lab_members.append(OP)
GP = LabMember('Gerard', 'green', '2021-03-01', '2021-02-08')
lab_members.append(GP)
AV = LabMember('Aparna', 'green', '2020-12-14', '2021-02-01')
lab_members.append(AV)

lab_talk_ls = []
jc_ls = []
# loop through dates
for i in range(len(dates)):
    # get the group for lab talk
    lab_talk_group = lab_talk_order[i]
    # get the group for journal club
    jc_group = jc_order[i]
    # get members in the selected lab talk group
    lab_talk_pool = select_group_member(lab_members, lab_talk_group)
    # get members in the selected journal club group
    jc_pool = select_group_member(lab_members, jc_group)
    # select the person gave lab talk the least recently in the group
    talk_person = select_lab_talk_person(lab_talk_pool)
    # put the name on list
    lab_talk_ls.append(talk_person)
    # update last talk date of that person
    talk_person.last_talk = dates[i]
    # select the person gave journal club the least recently in the group
    jc_person = select_jc_person(jc_pool)
    # put the name on list
    jc_ls.append(jc_person)
    # update last journal club date of that person
    jc_person.last_jc = dates[i]

df = pd.DataFrame({'date': dates, 'progress report': lab_talk_ls, 'journal club': jc_ls})
file_name = '/Users/kikawaryoku/Desktop/Marston_lab_meeting_draft.csv'
df.to_csv(file_name, index=False)
