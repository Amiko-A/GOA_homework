num1=int(input("შეიყვანე პირველი ციფრი"))
num2=int(input("შეიყვანე მეორე ციფრი"))
operations=input("აირჩიე ოპერაცია:მიმატება / გამოკლება / გამრავლება / გაყოფა:")

def simple_calculator(num1 , num2 , operations):
    if operations == "მიმატება":
        return num1+num2
    elif operations ==  "გამოკლება":
        return num1 - num2
    elif operations == "გამრავლება":
        return num1 * num2 
    if  operations == "გაყოფა" and num2==0:
        return"შეცდომა : ნულზე გაყოფა შეუძლებელია"
    else :
        return num1 // num2
    
simple_calculator(num1,num2,operations)
