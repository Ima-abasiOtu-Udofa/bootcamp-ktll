def multiply_firstname_by_3(firstname):
    result = firstname * 3
    return result

result = multiply_firstname_by_3("ima")
print(result)

def greet_specific_me(name, age, state):
    return f"Hello {name} you are {age} years old, You come from {state}. Welcome here"

print(greet_specific_me("Purple", 98, "Mecury"))
print(greet_specific_me("White", 128, "Pluto"))
print(greet_specific_me("Green", 10, "Jupiter"))

def resident_place():
    location = "Amsterdam"
    return f"I live in {location} and I love it" 
print(resident_place())   

def dog_names(laika, jax, orion):
    return len(laika) + len(jax) + len(orion)

print(dog_names("laika", "jax", "orion"))

def numbers(value1, value2):
    result = value1 * 2
    return result + value2
print(numbers(12, 25))

def arguments(vol, dist):
    result = (vol + dist) *2
    return result
print (arguments(12,24))

def upper_case(animal):
    return animal.upper()
print(upper_case("dogs"))

number = 5
while number<=10:
    print(number)
    number =number +1

    num = -2
    word = "hippopotamus"
    while len(word) >=2:
        print(word)
        word = word[2:]

greet_name = ["joy", "arit", "agnes"]:
    for names in name
    print("Hi (greet_name)")

