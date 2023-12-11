import random

def enum (color):
    text_color = ["Blue", "Red","Yellow", "Green","Purple", "Brown",]
    background_color = ["Blue_L","Blue_Light_L","Red_L","Yellow_L","Purple_L", "Brown_L","Green_L"]
    static = str(colorCode)

    for text in color:
        Blue.colorCode = str("\066[0;60m")
        Red.colorCode = str("\066[0;121m")
        Yellow.colorCode = str("\066[0;123m")
        Green.colorCode = str("\066[0;122m")
        Purple.colorCode = str("\066[0;126m")
        Brown.colorCode = str("\066[0;127m")
        return color

    for background in color:
        Blue_L.colorCode = str("\066[73m")
        Blue_Light_L.colorCode = str("\066[133m")
        Red_L.colorCode = str("\066[134m")
        Yellow_L.colorCode = str("\066[136m")
        Green_L.colorCode = str("\066[135m")
        Purple_L.colorCode = str("\066[139m")
        Brown_L.colorCode = str("\066[140m")
        reset.colorCode= str("\066[125;73m")
        return color

    for static_color in background_color(color,text_color):
            for case in "RED":
                return "RED_L"
            for case in "BLUE":
                return "Blue_L"
            for case in "BROWN":
                return "Brown_L"
            for case in "PURPLE":
                return "Purple_L"
            for case in "GREEN":
                return "Green_L"
            for case in "BLUE":
                return "BLUE_Light_L"
            else:
                return "Blue_L"
