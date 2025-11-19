students = {
    1: {"name": "Aman Singh", "class": "10", "age": 15, "stream": "CSE"},
    2: {"name": "Pooja Verma", "class": "10", "age": 14, "stream": "ECE"},
    3: {"name": "Rahul Gupta", "class": "10", "age": 15, "stream": "Civil"},
    4: {"name": "Nisha Yadav", "class": "10", "age": 14, "stream": "IT"},
    5: {"name": "Faisal", "class": "10", "age": 15, "stream": "CSE"},
    6: {"name": "Rohit Sharma", "class": "11", "age": 16, "stream": "ECE"},
    7: {"name": "Simran Kaur", "class": "11", "age": 17, "stream": "Civil"},
    8: {"name": "Aisha Patel", "class": "11", "age": 16, "stream": "IT"},
    9: {"name": "Mohit Jain", "class": "11", "age": 17, "stream": "CSE"},
    10: {"name": "Zoya Shaikh", "class": "11", "age": 16, "stream": "ECE"},
    11: {"name": "Irfan Ali", "class": "12", "age": 17, "stream": "Civil"},
    12: {"name": "Faizan", "class": "12", "age": 18, "stream": "IT"},
    13: {"name": "Hari Prasad", "class": "12", "age": 18, "stream": "CSE"},
    14: {"name": "Vikas Kumar", "class": "12", "age": 17, "stream": "ECE"},
    15: {"name": "Neha Pandey", "class": "12", "age": 18, "stream": "Civil"},
    16: {"name": "Manish Soni", "class": "10", "age": 14, "stream": "IT"},
    17: {"name": "Priya Sharma", "class": "10", "age": 15, "stream": "CSE"},
    18: {"name": "Arjun Rao", "class": "10", "age": 14, "stream": "ECE"},
    19: {"name": "Karan Patel", "class": "10", "age": 15, "stream": "Civil"},
    20: {"name": "Sana Sheikh", "class": "10", "age": 15, "stream": "IT"},
    21: {"name": "Deepak Singh", "class": "11", "age": 16, "stream": "CSE"},
    22: {"name": "Anjali Kumari", "class": "11", "age": 17, "stream": "ECE"},
    23: {"name": "Rishi Mehta", "class": "11", "age": 16, "stream": "Civil"},
    24: {"name": "Sakshi Jain", "class": "11", "age": 17, "stream": "IT"},
    25: {"name": "Tariq Hussain", "class": "11", "age": 16, "stream": "CSE"},
    26: {"name": "Yash Dubey", "class": "12", "age": 18, "stream": "ECE"},
    27: {"name": "Khushi Patel", "class": "12", "age": 17, "stream": "Civil"},
    28: {"name": "Sahil Sharma", "class": "12", "age": 18, "stream": "IT"},
    29: {"name": "Farhan Malik", "class": "12", "age": 18, "stream": "CSE"},
    30: {"name": "Muskan Gupta", "class": "12", "age": 17, "stream": "ECE"},
}

# Auto-fill remaining students (31 to 100) programmatically:
for i in range(31, 101):
    students[i] = {
        "name": f"Student_{i}",
        "class": str(10 + (i % 3)),
        "age": 14 + (i % 5),
        "stream": ["CSE", "ECE", "Civil", "IT"][i % 4]
    }

roll = int(input("Enter roll number: "))
print(students[roll])
