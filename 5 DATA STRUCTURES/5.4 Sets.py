# Sets are a unique and unordered group of elements

# Note that even though China is declared twice inside the set, the set automatically eliminates the duplicate
countries = {"China", "China", "India"}
print(countries)

# We can use the set command to convert a list to a set
countries_list = ["China", "China", "India"]
countries = set(countries_list)
print(countries)

# Set comprehensions work by the same principle as list comprehensions
# To demonstrate a unique properties of a set, first let's create a non-unique list of numbers
l = [i % 5 for i in range(20)]
print(l)
# The set only keeps the elements under 3 and eliminates the duplicates
s_comp = {n for n in l if n < 3}
print(s_comp)
