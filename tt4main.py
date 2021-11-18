import functions

print("MENU \n 1.Rectangle \n 2.Triangle\n 3.Square \n 4. Circle\n ")
n=int(input(" Select an option : "))
if n==1 :
	functions.rect()
elif n==2 :
	functions.tri()
elif n==3 :
	functions.squ()
elif n==4 :
	functions.cir() 
else :
	print("invalid")