#!/usr/bin/python3
""" add item to json file """
json = __import__("json")
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
sys = __import__("sys")


obj = sys.argv
def write_to_json(obj):
    if len(obj) == 1:
        inpt = []
        save_to_json_file(inpt, "add_item.json")
        load_from_json_file("add_item.json")
    else:
        inpt = obj[1:] 
        save_to_json_file(inpt, "add_item.json")
        load_from_json_file("add_item.json")
   
if __name__ == "__main__":
    write_to_json(obj)
