class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @property #jakby była tylko atrybutem - nie trzeba ()
    def email(self):
        return '{}.{}@university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod #whole class
    def set_min_avg(cls, new_avg):
        cls.min_avg = new_avg

    @staticmethod
    def academic_football_team_cheer():
        return "Go go New York Academy!"


obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)

print(obj_anna.email)
