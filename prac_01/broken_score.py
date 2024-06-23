"""
CP1404/CP5632 - Practical
Broken program to determine score status
Changes Made:
Removed a redundant > 100 line
Changed else: ifs, to elifs
Rearranged the score boundaries to descending order.
"""
# Old Code
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")


# Fixed Code
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
if score < 50:
    print("Bad")
