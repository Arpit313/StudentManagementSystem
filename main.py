import os
import platform

global listStd 
listStd = ["Arpit", "Mayank", "Chris"] 

def manageStudent(): 

	global bye 
	bye = "\n Thank you "

	print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		
		""")

	try: 
		userInput = int(input("Please Select from above Options: ")) 
	except ValueError:
		exit("\nHy! That's Not A Number") 
	else:
		print("\n") 

	#Checking the options	
	if(userInput == 1): 
		print("List Students\n")  
		for students in listStd:
			print("=> {}".format(students))

	elif(userInput == 2): 
		newStd = input("Enter New Student details: ")
		#First checking, if student is already registered or not
		if(newStd in listStd): 
			print("\n This Student {} Already In The Database".format(newStd))  
		else:	
			listStd.append(newStd)
			print("\n=> New Student {} Successfully Add \n".format(newStd))
			for students in listStd:
				print("=> {}".format(students))	

	elif(userInput == 3): 
		srcStd = input("Enter Student Name To Search: ")
		if(srcStd in listStd): 
			print("\n=> Record Found Of Student {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Student {}".format(srcStd)) 

	elif(userInput == 4): 
		rmStd = input("Enter Student Name To Remove: ")
		
		if(rmStd in listStd):  
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
		
			for students in listStd:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) 

	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")			

manageStudent()

def runAgain(): 
	runAgn = input("\nDo you want To Run Again (Y/N): ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		
		manageStudent()
		runAgain()
	else:
		quit(bye) 

runAgain()		
