temperature_array = []
lowscore = 0
highscore = 0
    
for i in range(0,18):
    temperature = float(input("Input the baby's temperature "))
    temperature_array.append(temperature)
    print(temperature_array)
    if temperature > 37.5:
            print("Temperature is too high")
            highscore += 1
    elif temperature < 36.0:
            print("Temperature is too low")
            lowscore += 1
    else:
        print("Temperature is in correct range")
    
    
highesttemperature = max([i for i in temperature_array])
print(f"The baby's highest temperature was {highesttemperature}")

lowesttemperature = min([i for i in temperature_array])
print(f"The baby's lowest temperature was {lowesttemperature}")

rangetemperature = highesttemperature - lowesttemperature
print(f"The baby's temperature range is {rangetemperature}")

if rangetemperature > 1:
    print("The baby's temperature range is more than 1 degrees, baby requires stabilisation")

else:
    print("The baby is in a good temperature range")


if highscore > 1:
    print("The baby's temperature has been too high more than once.")

elif lowscore > 1:
    print("The baby's temperature has been too low more than once.")

else:
    print("The baby's temperature has not exceeded the max temperature twice or more and the minimum temperature twice or more.")



