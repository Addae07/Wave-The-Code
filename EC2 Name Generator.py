#!/user/bin/env python3.7

# Project: EC2 Random Name Generator

# Directive: 
#Several departments share an AWS environment. You need to ensure that the EC2s are properly 
#named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to 
#create your unique EC2 names that the users can then attach to the instances. 

#The Python Script should:

#1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
#2. Allow the user to input the name of their department that is used in the unique name.
#3. Generate random characters and numbers that will be included in the unique name.


import random
import string

def string_generator(size=10, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
 #2   
number = int(input("Enter number of EC2 instances with a unique name:"))

Department = input("Choose name of desired department: Security_Ops, Business_Ops, or Network_Ops: ")

for _ in Department:
    
    if Department == "Security_Ops" :
        print("Security_Ops")
        break
    
    elif Department == "Business_Ops" :
        print("Business_Ops")
        break
    
    elif Department == "Network_Ops" :
        print("Network_Ops")
        break
    
    else:
        print("This Depaartment is not available. Please try again")
        exit()
        
        
 for _ in range(1, number + 1):
     ec2_name = department
     unique_name = ec2_name + "_" + string_generator()
    print("Your EC2's unique name is : ", unique_name)
    