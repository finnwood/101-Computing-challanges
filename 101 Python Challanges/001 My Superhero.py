# My superhero - www.101computing.net/my-superhero/

#Store the properties of your superhero
name = "BatJim"
location = "Gothman"
gender = "Male"
enemy = "Mr Funny"
powers = "Intellengence, Technology, Money"
strength = 9
speed = 8
age = 35
height = 2


#Display a description of your superhero
print("###############################")
print("#                             #")
print("#       MY SUPERHERO          #")
print("#                             #")
print("###############################")
print("")
print("I am  "+ name + " and I live in "+ location +".")
#Cant concantate an integer so str() convers intiger to string
print("I am  "+ gender + " and am "+ str(age) +" years old.") 
print("My Powers are " + powers + " and my arch nemesis is " + enemy + ".")
print("My strength score is " + str(strength) + "/10.")