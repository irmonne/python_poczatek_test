class BigBoss:
    pass

    def greeting(self):
        print("Greetings, all employees!")


class DivisionOneBoss(BigBoss):
    pass

    def greeting(self):
        print("Greetings, DivisionOne employees!")


class DivisionTwoBoss(BigBoss):
    pass

    def greeting(self):
        print("Greetings, DivisionTwo employees!")


class SubdivisionTwoBoss(DivisionTwoBoss):
    pass

    def greeting(self):
        print("Greetings, SubdisivionTwo employees!")


class Employee(DivisionTwoBoss, SubdivisionTwoBoss):
    pass

    def greeting(self):
        print("Greetings, all Bosses!")


employee = Employee()
employee.greeting()
print(Employee.mro())
