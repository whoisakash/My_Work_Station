class Bank:
    def bankName(self):
        print("BANK")

class Manager(Bank):
    def managerData(self):
        print("Managers")

class Staff(Manager):
    def staffData(self):
        print("Staff")

stf = Staff()
stf.bankName()
# stf.managerData()
# stf.staffData()

