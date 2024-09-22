##                                          ## project ##                                    #####3
class BnkManagementSys:
    def _init_(self) -> None:
        self.bank = {}  #creating dict to store details

## adding bank ##
    def add_bnk(self,bnk_id,name,position,salary):
        if bnk_id in self.bank:
            print("Bank ID already exists")
        else:
            self.bank[bnk_id]={"name":name,"position":position,"salary":salary}
            print("bank added successfully")
##  To update details of bank ##
    def update_bnk(self,bnk_id, name=None,position=None,salary=None):
        if bnk_id in self.bank:
            if name:
                self.bank[bnk_id]["name"]=name
            if position:
                self.bank[bnk_id]["position"]=position
            if salary:
                self.bank[bnk_id]["salary"]=salary
            print("bank details update successfully")
        else:
            print("Bank ID not found")
## To delete bank details ##
    def del_bnk(self,bnk_id):
        if bnk_id in self.bank:
            del self.bank[bnk_id]
            print(f"{bnk_id} has been deleted successfully")
        else:
            print(f"Bank ID {bnk_id} not found")
## To view particular bank details ##
    def view_bnk(self,bnk_id):
        if bnk_id in self.bank:
            print("Bank ID: "+ str(bnk_id))
            print("Name:" + self.bank[bnk_id]["name"])
            print("Position:" + self.bank[bnk_id]["position"])
            print("Salary:" + str(self.bank[bnk_id]["salary"]))
        else:
            print("Bank ID not found")
## To view all details ##
    def view_all_bnk(self):
        if self.bank:
            for bnk_id, details in self.bank.items():
                print("Bank ID: " +str(bnk_id))
                print("Name: " + details["name"])
                print("Position: " + details["position"])
                print("Salary: " + str(details["salary"]))
                print("--*20")
            else:
                print("No bank found")
## Create obj ##
def main():
        mng_sys=BnkManagementSys()

        # for infinite loop
        while True:
            print("1. Add bank ")
            print("2. Update bank ")
            print("3. Delete bank ")
            print("4. View particular bank ")
            print("5. View all bank ")
            print("6. Exit ")

            Choice =input("enter your choice: ")

            if Choice == '1':
                bnk_id=input("enter bank ID: ")
                name =input("enter name: ")
                position=input("enter position: ")
                salary =input("enter salary: ")
                mng_sys.add_bnk(bnk_id,name,position,salary)

            elif Choice == '2':
                bnk_id = input("enter bank ID:")
                name = input("enter name(if no change, leave blank): ")
                position = input("enter position(if no change, leave blank): ")
                salary = input("enter salary(if no change, leave blank): ")
                mng_sys.update_bnk(bnk_id,name or None,position or None,salary or None)

            elif Choice =='3':
                bnk_id = input("enter bank ID:")
                mng_sys.del_bnk(bnk_id)

            elif Choice =='4':
                bnk_id = input("enter bank ID:")
                mng_sys.view_bnk(bnk_id)

            elif Choice =='5':
                mng_sys.view_all_bnk()

            elif Choice =='6':
                break
            else:
                print("invalied number")
main()