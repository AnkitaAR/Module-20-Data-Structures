student_data={id: {'name': 'Alice', 'grades': [85, 90, 78]},id: { 'name': 'Bob', 'grades': [88, 76, 92]},id: { 'name': 'Charlie', 'grades': [95, 89,84]},id: { 'name': 'David', 'grades': [70, 80, 65]}}
result={} # empty dictionary to store results
for key,value in student_data.items():
   if value not in result.values():
      result[key]=value
      print("Unique student added:",value)
      print("Student data :",result)