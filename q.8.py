# Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary honi chahiye. 
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. 
# Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai. 

import json
dict1 ={
    "emp1": {
        "name": "neelam",
        "designation": "programmer",
        "age": "24",
        "salary": "2400"
    },
    "emp2": {
        "name": "komal",
        "designation": "Trainee",
        "age": "24",
        "salary": "20000"
    },
     "emp1": {
        "name": "Annuradha",
        "designation": "HR",
        "age": "25",
        "salary": "40000"
    },
    "emp4": {
        "name": "Abhishek",
        "designation": "Manegar",
        "age": "29",
        "salary": "63000"
    },
}
out_file = open("emp.json", "w")
json.dump(dict1,out_file, indent = 10)
out_file.close()