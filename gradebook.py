last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["Physics", "Calculus", "Poetry", "History"]
print(subjects)

grades = [98, 97, 85, 88]
print(grades)

gradebook = [
  ["Physics", 98], 
  ["Calculus", 97], 
  ["Poetry", 85], 
  ["History", 88]
  ]
print(gradebook)

gradebook.append(["Computer Science", 100])
print(gradebook)

gradebook.append(["Visual Arts", 93])
print(gradebook)

gradebook[-1][1] = 98
print(gradebook)

gradebook[2].append("Pass")
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
