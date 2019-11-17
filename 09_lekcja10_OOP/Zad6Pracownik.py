
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
        print("After " + str(self.experience) + " years of work, " + self.name + " gets a rise of: " + str((self.experience*(self.salary * 0.01) )) + " PLN!")
        return (self.experience*(self.salary * 0.01))

    def basic_taxes(self):
        tax = self.salary * 0.02
        print("\t" + self.name + "'s taxes:\n\t\t" + str(tax))
        return tax

    def health_care(self):
        if self.is_student:
            proc = 0
            print("\t\tA student doesn't have to pay for health care!")
        else:
            proc = 0.016
            print("\t\t"+str(self.salary * proc))
        return self.salary * proc

    def email(self):
        vowels = "aeiouy"
        persona = [self.name, self.surname]
        updated_pers = []
        for i in persona:
            word = i
            for j in word:
                if j in vowels:
                    word = word.replace(j,"")
            updated_pers.append(word)
        primary = "".join(updated_pers)
        primary = primary.lower()
        company = self.company
        company = company.lower()
        company = company.replace(" ","")
        secondary = company + ".com"
        email = primary + "@" + secondary
        return email


def worker_checker(num):
    workers = ["1","2","3","4","5","6"]
    worker = f"work_{num}"
    if num not in workers:
        status = False
        worker = None
        return status, worker
    else:
        status = True
        return status, worker


def showing_files(worker):
    print("\nExtra data of", worker.name, worker.surname + ":\n")
    worker.salary_raise()
    print("\nDeducting from salary: ")
    print("\tHealth care:")
    h_care =  worker.health_care()
    b_tax = worker.basic_taxes()
    money_left = worker.salary - h_care - b_tax
    print(worker.name, worker.surname, "Has a salary of", worker.salary, "but after deduction only",money_left, "PLN are left")
    print("\nIf you think that", worker.name, "earns too much, write an email:")
    print("\t\t",worker.email())


worker_dict = {}

worker_dict["work_1"] = Worker("CEO", 13500, "Karen", "Smith", 7, False, False)
worker_dict["work_2"] = Worker("HR", 2800, "John", "Munk", 3, True, False)
worker_dict["work_3"] = Worker("PR", 3200, "Jack", "Wazowski", 4, False, True)
worker_dict["work_4"] = Worker("cleaning lady", 1600, "Jessica", "Johnson", 2, False, False)
worker_dict["work_5"] = Worker("HR Junior", 2100, "Betty", "Odden", 1, False, True)
worker_dict["work_6"] = Worker("Security guard", 2500, "Tom", "Phillips", 16, True, False)


state = False
while state == False:
    chosen_worker = input("\nHello, whose files do you need to see?\n\t1 - Karen Smith\n\t2 - John Munk\n\t"
                          "3 - Jack Wazowski\n\t4 - Jessica Johnson\n\t5 - Betty Odden\n\t6 - Tom Phillips\n\t\t")
    state, worker = worker_checker(chosen_worker)

showing_files(worker_dict[worker])