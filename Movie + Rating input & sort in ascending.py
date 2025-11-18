movies = []

name1 = input("Enter movie name: ")
rating1 = float(input("Enter movie rating: "))
movies.append([name1, rating1])

name2 = input("Enter movie name: ")
rating2 = float(input("Enter movie rating: "))
movies.append([name2, rating2])

name3 = input("Enter movie name: ")
rating3 = float(input("Enter movie rating: "))
movies.append([name3, rating3])

movies.sort(key=lambda x: x[1])
print(movies)
