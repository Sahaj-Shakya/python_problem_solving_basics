math = float(input("Enter percentage obtained in maths: "))
science = float(input("Enter percentage obtained in science: "))
english = float(input("Enter percentage obtained in english: "))
social = float(input("Enter percentage obtained in social: "))

total = ((math + science + english + social)/400)*100

if total >= 80:
    print(f"Congratulations you have obtained A+ by scoring a total of {total}%.")
elif total >=70 and total < 80:
    print(f"Congratulations you have obtained A by scoring a total of {total}%.")
elif total >= 60 and total < 70:
    print(f"Congratulations you have obtained A- by scoring a total of {total}%.")
elif total >= 50 and total < 59:
    print(f"Congratulations you have obtained B by scoring a total of {total}%.")
elif total >= 40 and total < 49:
    print(f"Congratulations you have obtained B by scoring a total of {total}%.")
else:
    print(f"You have failed the exams! You only obtained {total}%.")
    
    