# 'FizzBuzz' FizzBuzz მიზანი: შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 100-მდე. თუმცა 3-ის ჯერადებისთვის რიცხვის ნაცვლად დაბეჭდეთ „Fizz“, ხოლო 5-ის ჯერადებისთვის დაბეჭდეთ „Buzz“. 3-ისა და 5-ის ჯერადი რიცხვებისთვის დაბეჭდეთ "FizzBuzz".  მოთხოვნები: გამოიყენეთ მარყუჟი 1-დან 100-მდე რიცხვების გასამეორებლად.გამოიყენეთ პირობითი განცხადებები, რათა შეამოწმოთ რიცხვი იყოფა 3-ზე, 5-ზე ან ორივეზე. დაბეჭდეთ შესაბამისი სიტყვა ("Fizz", "Buzz" ან "FizzBuzz") ან ნომერი. 
for i in range(1 , 100):
   if i % 3 == 0 and i % 5 == 0 :
      print(i,"FizzBazz")    
   elif i % 3 ==0 :
    print(i,"Fizz")
   elif i % 5 ==0:
     print(i,"Buzz")