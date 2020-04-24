# def album_cover(artist, album_title, year=''):
#   if year:
#       album = {'artist': artist, 'album_title': album_title, 'year': year}
#   else:
#       album = {'artist': artist, 'album_title': album_title}
#   return album


#artist = input("What is the name of artist: ")
#album_title = input("What is the title of the album: ")
#year = ("What year was the album released: ")

#musician = album_cover(artist, album_title, year)
# print(musician)

# names = ['pete', 'dawg', 'mars', 'steve']


# def roll_call(name):
#     for name in names:
#         print("Hi "+name+" !")


# roll_call(names)

# unprinted_models = ['spiderman 3d', 'iphone case', 'robot pendant']
# printed_models = []

# while unprinted_models:
#     current_model = unprinted_models.pop()
#     print("printing "+current_model)
#     printed_models.append(current_model)

# for printed_model in printed_models:
#     print(printed_model)


# def print_models(models):
#     while models:
#         current_model = models.pop()
#         print("printing "+current_model)
#         printed_models.append(current_model)

#     for printed_model in printed_models:
#         print(printed_model)


# print_models(unprinted_models[:])
# print(unprinted_models)


# def make_pizza(*toppings):
#     print("Making pizza with the following toppings:\n")
#     for topping in toppings:
#         print("- "topping)


# make_pizza('mushroom')

# make_pizza('mushroom', 'cheese', 'green pepper')


# def make_pizza(size, *toppings):
#     print("making a "+str(size)+" inch pizza with the following topping(s)")
#     for topping in toppings:
#         print("- "+topping)


# make_pizza(14, 'mushroom', 'extra cheese', 'green pepper')

def build_profile(first, last, **user_profile):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_profile.items():
        profile[key] = value
    return profile


user_profile = build_profile('Emmanuel', 'Ebo', location='Nkawkaw', field='IT')
print(user_profile)
