# Write a Python program to create a histogram from a given list
# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# f={}
# for i in data:
#    f[i] = f.get(i,0)+1
# for i,c in f.items():
#    print(f'{i:10}:{"*" * c}')


# input = 3 , output = ABC
# num = 3
# for i in range(0,num):
#    print(chr(65+i))
# login system 
# d={"metab":123,"afsar":333,"Ali":777}
# username = input("Enter the username:-")
# password = int(input("Enter the password:-"))
# if username in d and d[username] == password:
#     print("login valid")
# else:
#     print("login invalid")
# palindrom
# string="mom"
# if string == string[::-1]:
#    print("palindrom")
# else:
#    print("not palindrom")
# Print all prime numbers within a range
start = 20
end = 30
num=0
for i in range(start,end+1):
   if num<i:
      for i in range(2,num):
         if i%2 != 0:
            print(i) 