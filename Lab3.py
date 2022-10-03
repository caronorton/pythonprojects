year = int(input("Please enter number of years: "))

loopyear = year
population = 89.2

while loopyear > 0:
    population *= 1.023
    loopyear -= 1

print("The population of Mexico in", 1990 + year, "is", population, "million")




population = float(input("Enter the population"))
pop = 89.2
year = 0

if population > 89.2:
    while population >= pop:
        pop *= 1.023
        year += 1
    print("Pop in year:", year + 1990, "is equal to", population)
elif population < 89.2:
    while population <= pop:
        pop /= 1.023
        year += 1
    print("Pop in year:", 1990 - year, "is equal to", pop)
else:
    print("Pop in year:", 1990, "is equal to", 89.2)
