from pydantic import BaseModel,field_validator,model_validator,computed_field

def menu():
    print("==AI MANAGER==")

def register_menu():
    print("Registered Agents: ")

def options():
    print("1. Create an Agent\n2. View All Agents\n3. View Agent Details\n4. Update Agent\n5. Delete Agent\n6. Compare Agents\n7. View System Statistics\n8. Exit")

def create_agent():
    print("========== CREATE AGENT ==========")

menu()
options()
choice=int(input("Select an Option: "))
match choice:
    case 1: 
        create_agent()
        name_agent=str(input("Enter name: "))

class Registration(BaseModel):
    choice: int
    name_agent: int

user=Registration(choice=choice,name_agent=name_agent)