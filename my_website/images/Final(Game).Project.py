def getResponseBoolean(question):
    response = raw_input(question + " (Y/N): ")
    if response.lower() == "y":
        return True
    else:
        return False

def APCODOOD():
    print("Be you Dood in the apcolispe,you are thirsty and hungry")
    print("TO start again, type(APCODOOD())")
    if getResponseBoolean("Go to box to look for food?"):
        print("Its got a single can of water and a rock")
        if getResponseBoolean("Take the stuff?"):
            print("You drink the water, also you take the rock,(Why tho)")
            print("You are now just hungry, you decide to leave, you find a body ouside") 
            if getResponseBoolean("Take the map, next to the body?"):
                print("You take the map, its a map to the MEAT-MAN")
                if getResponseBoolean("You arrive at the MEAT MAN SHOP, you see some MEAT, Take some of it?"):
                    print("You dont take the MEAT, GOOD as the MAN himself comes out")

                else:
                    print("You take the meat, and eat it, and the MAN himself comes out")
                    print("Sadly the MEAT-MAN doesnt take kindly to STEALERS, you DIE at the hands of of the MEAT MAN")

            else:
                print("You decided to try your luck and move forward")
                print("You die in the TOXIC WASTE LAND,(LOSER)")
        else:
            print("Again this is not your stuff you decide to go outside instead")
            if getResponseBoolean("You see a bodywith a map, take it?"):
                print("You take the map,it says MEAT-MAN, and what seems to a house")

            else:
                print("You dont take the map, you soon die from GOING INTO THE TOXIC WASTE LAND")
    else:
        print("You dont go to the box since this isnt your house, and it could be a trap")
        if getResponseBoolean("You are outside, theres a dead body and a map, take it?"):
            print("You take the map, the man is dead,(what a loser)")
            print("The map is badly drawn, all it says is MEAT MAN")
        else:
            print('You decide not to take the map since it may be trapped')
            print("You soon die from heat exhaustion, You DIE IN THE WASTE LAND")
                       
                     
                                