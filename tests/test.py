import unittest

from wcc_timetable_generator.algo import generate_timetable
from wcc_timetable_generator.subject_model import Subject

class TestAlgo(unittest.TestCase):
    subjects = [
        Subject('SGBD', 2),
        Subject('SysAdmin', 6),
        Subject('Dev WEB', 4),
        Subject('Algo', 4),
        Subject('Comm', 2),
        Subject('Anglais', 2),
    ]

    def test_algo(self):
        timetable = generate_timetable(TestAlgo.subjects)
        self.assertTrue(timetable)

    def test_all_subjects_are_distributed(self):
        """
        Test if all subjects hours are totally distributed
        """
        timetable = generate_timetable(TestAlgo.subjects)
        for subject in TestAlgo.subjects:
            total_distributed_hour = len([slot for day in timetable for slot in day if slot == subject.label])
            self.assertEqual(total_distributed_hour, subject.duration)
    
    def test_no_adjacent_day_with_same_subject(self):
        """
        Test if no subject is present in two consecutive days
        for 10 random timetables
        """
        subjects = [
            Subject('SGBD', 2),
            Subject('SysAdmin', 6),
            Subject('Dev WEB', 4),
            Subject('Algo', 4),
            Subject('Comm', 2),
            Subject('Anglais', 2),
        ]
        for _ in range(10):
            timetable = generate_timetable(subjects)
            local_subjects = subjects.copy()
            for subject in local_subjects:
                for day in range(len(timetable)):
                    if subject.label in timetable[day]:
                        previous_day = day - 1
                        next_day = day + 1
                        if previous_day >= 0 and previous_day < len(timetable):
                            self.assertNotIn(subject.label, timetable[previous_day])
                        if next_day >= 0 and next_day < len(timetable):
                            self.assertNotIn(subject.label, timetable[next_day])

if __name__ == "__main__":
    unittest.main()