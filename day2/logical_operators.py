# logical operators = evaluate multiple expressions (and, or, not)
#                     or = at least one expression is True
#                    and = all expressions are True
#                   not = reverse the result, True -> False, False -> True

# or
# temp = 20
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# and & not
# temp = 20
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is SUNNY 🌞")
# elif temp <= 0 and is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is SUNNY 🌞")
# elif 28 > temp > 0 and is_sunny:
#     print("It is Warm outside")
#     print("It is SUNNY 🌞")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is CLOUDY ☁")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is CLOUDY ☁")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is Warm outside")
#     print("It is CLOUDY ☁")