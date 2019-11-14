

class Worker:
    company = "Love Python"

    def __init__(self, position, salary, name, surname, experience, seniority, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.experience = experience
        self.seniority = seniority
        self.is_student = is_student

    def salary_raise(self):
        print("After " + str(self.experience) + " years of work, " + self.name + " gets a rise of: " + str((self.experience*(self.salary * 0.01) )) + " dollars!")
        return (self.experience*(self.salary * 0.01) )

    def taxes(self):
        return self.salary * 0.02

    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
        return self.salary * proc

    def email(self):
        vowels = [a, e, i, o, u, y]
        primary = self.name + "." + self.surname
        secondary = self.company.strip().lower() + ".com"
        email = primary + "@ " + secondary
        return email


work_1 = Worker("CEO", 3500, "Karen", "Smith", 7, False, False)
work_2 = Worker("HR", 2800, "John", "Munk", 3, True, False)
work_3 = Worker("PR", 3200, "Jack", "Wazowski", 4, False, True)

work_1.salary_raise()