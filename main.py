print("WELCOME TO THE LOVE CALCULATOR")
name1 = input("WHAT IS YOUR NAME?\n   ")
name2 = input("WHAT IS THEIR NAME?\n   ")

combined_string = name1+name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"YOUR LOVE SCORE  IS {love_score},YOU GO TOGETHER LIKE COKE AND MENTOS")

elif (love_score < 40) or (love_score > 50):
    print(f"YOUR LOVE SCORE IS {love_score}, YOU ARE ALRIGHT")

else:
    print(f"YOUR SCORE IS {love_score}")
