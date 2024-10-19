check = " "
light_on = False
while check != "sleep":
    check = input("User switch on/off:").lower()
    if check == "on":
        if light_on:
            print("light is already on mode")
        else:
            light_on = True
            print("light on")
    elif check == "off":
        if not light_on:
            print("light is already off mode")
        else:
            light_on = False
            print("light off")
    elif check == "sleep":
        print("sleep mod")
        break

else:
    print("check the commmand")
