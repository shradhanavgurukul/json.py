import json
k={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
out_file = open("shopping.json", "w")
json.dump(k,out_file,indent=4)
out_file.close()

