class Bank:
    def showData(self):
        print("BANK")

class Manager(Bank):
    def showData(self):
        print("Managers")

class Staff(Manager):
    def showData(self):
        print("Staff")

bnk = Bank()
mng = Manager()
stf = Staff()

# bnk.showData()
mng.showData()
# stf.showData()


