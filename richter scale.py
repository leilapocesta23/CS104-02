first_name=input("enter your first name:")
last_name=input("enter your last name:")
ID=int(input("Enter your ID:"))

richter=float(input("Enter a Richter scale value:"))
Stop=False
while Stop==False:
if richter>=8:
    print("Most structures fall")
    Stop=True
elif richter<8 and richter>=7:
    print("Many buildings destroyed")
elif richter<7 and richter>=6:
    print("Many buildings considerably damaged, some collapse")
elif richter<6 and richter>=4.5:
    print("Damage to poorly constructured buildings")
elif richter==0:
    print("No earthquakes")

