#ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე.პროგრამის დანიშნულება არის ის, რომგამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს. 
num=int(input("Please enter your number 1 throught 100:"))
my_guess=0

while my_guess != num :
    my_guess= int(input("My Guess is:"))

print("I have guessed your number")