#list -> data structure which can hold multiple values of multiple type
#array -> data structure which can hold multiple values of same type
list_of_cloud = ["aws","azure","gcp","digital ocean","utho"]
cloud = "gcp" #variable

print(list_of_cloud)

#add a new cloud Salesforce
list_of_cloud.append("Salesforce")

#add a new cloud IBM
list_of_cloud.append("IBM") #adds to the end of list

print(list_of_cloud)

#number position changes
list_of_cloud.insert(2,"utho") 

print(list_of_cloud)

#element count its alwase 01
print(len(list_of_cloud))

# insert "HELLO CLOUD" to the index of list

list_of_cloud.insert(0,"HELLO CLOUD")

print(list_of_cloud)

#Iteration of a list
for cloud in list_of_cloud:
    print(" ")
    print(cloud)

for i in range(1,11):
    print("hello bro")