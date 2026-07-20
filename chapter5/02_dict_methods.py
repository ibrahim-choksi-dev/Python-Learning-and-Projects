marks = {
    "Mohammad": 100,
    "Fatima": 100,
    "Ali": 99,
    "Hassan": 98,
    "Hussain": 97,
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ali": 100, "Zainab": "99"})
# print(marks)
# print(marks.get("Mohammad")) # Here i get Mohammad marks
# print(marks.get("Usman"))  # Here we gets none because there is no key 

print(marks.get("Mohammad2")) #Prints none
print(marks["Mohammad2"]) # Returns an error 
