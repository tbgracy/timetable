from typing import List
from subject_model import Subject
from random import shuffle
from pprint import pprint as print


def generate_timetable(subjects: List[Subject]):
    timetable = [["vide"] * 4 for _ in range(5)]
    timetable.append(["vide", "vide"])

    for subject in subjects:
        distribute_hours(timetable, subject)

    return timetable


def distribute_hours(timetable, subject):
    if subject.duration == 0:
        return

    slots = []
    for day in range(len(timetable)):
        slots = slots + [(day, slot) for slot in range(len(timetable[day]))]

    shuffle(slots)

    for (day, slot) in slots:
        if is_slot_available(timetable, day, slot) and is_not_present_in_consecutive_days(timetable, day, subject):
            timetable[day][slot] = subject.label
            subject.duration -= 2

            if subject.duration == 0:
                break


def is_not_present_in_consecutive_days(timetable, day, subject):
    previous_day = day - 1
    next_day = day + 1
    if previous_day >= 0 and previous_day < len(timetable):
        for slot in timetable[previous_day]:
            if slot == subject.label:
                return False
    if next_day >= 0 and next_day < len(timetable):
        for slot in timetable[next_day]:
            if slot == subject.label:
                return False
    return True


def is_slot_available(timetable, day, slot):
    return timetable[day][slot] == "vide"


if __name__ == '__main__':

    subjects = [
        Subject('SGBD', 2),
        Subject('SysAdmin', 6),
        Subject('Dev WEB', 4),
        Subject('Algo', 4),
        Subject('Comm', 2),
        Subject('Anglais', 2),
    ]

    print(generate_timetable(subjects))
