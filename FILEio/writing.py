# cities = ["New Delhi", "Bangalore", "Mumbai", "Chennai", "Kolkata", "Hyderabad"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)


# city_list =[]
# with open("cities.txt",'r') as city_file:
#     for city in city_file
#         city_list.append(city.strip("\n"))


# print(city_list)
# for x in city_list:
#     print(x)

#
# imelda = "More Mayhem", "Imelda May", "2011", \
#          ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    line = imelda_file.readline()

content_in_real_form = eval(line)
print(content_in_real_form)
print()
album, artist, year, tracks = content_in_real_form
print(album)
print(artist)
print(year)
print(tracks)