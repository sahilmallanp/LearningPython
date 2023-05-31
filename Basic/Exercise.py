weight = int(input("Enter your weight"))
unit = input("Enter (K)g_or_(l)bs")
if unit.upper() == "K" :
    converted = weight / 0.45
    print("Weights in Kgs is : " + str(converted))
else :
    converted = weight * 0.45
    print("Weights in lbs is : " + str(converted))
