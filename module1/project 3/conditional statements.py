temperature=int(input("what is the temperature today?"))
if temperature <20:
    outfit="jacket"
    print("its a cold day!")
    print("wear a",outfit)
else:
    outfit="t-shirt"
    print("its a warm day.")
    print("wear a",outfit)
is_raining=(input("is it raining?"))
if is_raining=="yes":
    print("it is raining!")
    print("take an umbrella")
else:
    print("take some sunglasses")
windspeed=int(input("what is the windspeed?"))
if windspeed >50:
    outfit="t-shirt"
    print("it is a windy day!")
    print("wear a windbreaker over your",outfit)
else:
    print("its a calm day.")
    print("no need to wear a windbreaker")
puddle=input("are there puddles on the road?")
if puddle=="yes":
    shoes="boots"
    print("the road has puddles")
    print("wear your",shoes)
else:
    shoes="slipper"
    print("the road has no puddles")
    print("wear your ",shoes)
