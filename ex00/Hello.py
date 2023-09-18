ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "world!"

y = list(ft_tuple)
y[1] = 'Malaysia!'
ft_tuple = tuple(y)
ft_set.discard("tutu!")
ft_set.add("Kuala Lumpur")
ft_dict.update({"Hello" : "42KL!"})

# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)