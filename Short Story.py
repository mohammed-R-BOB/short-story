print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝""")

print("you was saliling and your ship destroyed by a storm😢😢.....")

print("..., you wake up on a beach🐬🐬")

way_1 = input(

    "you found a way to the forest🌲 or a way to mountain⛰️, choose one:").lower()

if way_1 == "forest":

    print("you found gorilla🦍 and he attacked you🩸🩸")

    print("you are dead💀💀")

elif way_1 == "mountain":

    print("you found a cave and entered it🦇🦇")

    way_2 = input(

        "you found a way to the left or a way to the right, chose one:").lower()

    if way_2 == "left":

        print("you found a bear🐻 and he attacked you🩸🩸")

        print("you are dead💀💀")

    elif way_2 == "right":

        print("you found a way out the cave and you found a village🫂")

        print("you are safe now❤️❤️")

        print("You WON!!!🏆🏆")

    else:

        print("it not from the options😡😡")

else:

    print("it not from the options😡😡")
