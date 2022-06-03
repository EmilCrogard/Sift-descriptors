# importerar libraries
import numpy as np
import math 

from PIL import Image, ImageFilter

#Beskrivning: Funktionen tar in de beräknade värdena Gy och Gx för att beräkna riktning samt storlek för varje pixel i bilden. Den placerar även in värdena i listor efter vilken bricka pixeln tillhör samt riktining. 
#Gx: Integer - Integer som anger skillnad i x-led för pixelns ljusvärde .
#Gy: Integer - Integer som anger skillnad i y-led för pixeln ljusvärde. 
#Magnitude_index: Interger - Integer som är index för vilken bricka som beräknas.
#Φ_box: Array - Array som innehåller fler arrayer vars innehåll är de beräknade pixlarnas riktning.
#magnitude_box: Array - Array som innehåller fler arrayer vars innehåll är de beräknade pixlarnas storlek.
#return: Array - Returnerar arrayerna magnitude_box och Φ_box inplace
#by: Emil Crogård
#date: 2022-05-29
def magnitude_orientation(Gx, Gy, Magnitude_index, Φ_box, magnitude_box):
    if Gx != 0 and Gy != 0:
        magnitude = math.sqrt(Gx**2 + Gy**2)
        Φ = np.degrees(np.arctan(Gy/Gx))
    else:
        magnitude = math.sqrt(Gx**2 + Gy**2)
        Φ = 0
        
    if Φ < (360/8):
        Φ_box[Magnitude_index][0].append(Φ)
        magnitude_box[Magnitude_index][0].append(magnitude)
        if Φ < (2*(360/8)) and Φ > (360/8):
            Φ_box[Magnitude_index][1].append(Φ)
            magnitude_box[Magnitude_index][1].append(magnitude)
            if Φ < (3*(360/8)) and Φ > (2*(360/8)):
                Φ_box[Magnitude_index][2].append(Φ)
                magnitude_box[Magnitude_index][2].append(magnitude)
                if Φ < (4*(360/8)) and Φ > (3*(360/8)):
                    Φ_box[Magnitude_index][3].append(Φ)
                    magnitude_box[Magnitude_index][3].append(magnitude)
                    if Φ < (5*(360/8)) and Φ > (4*(360/8)):
                        Φ_box[Magnitude_index][4].append(Φ)
                        magnitude_box[Magnitude_index][4].append(magnitude)
                        if Φ < (6*(360/8)) and Φ > (5*(360/8)):
                            Φ_box[Magnitude_index][5].append(Φ)
                            magnitude_box[Magnitude_index][5].append(magnitude)
                            if Φ < (7*(360/8)) and Φ > (6*(360/8)):
                                Φ_box[Magnitude_index][6].append(Φ)
                                magnitude_box[Magnitude_index][6].append(magnitude)
                                if Φ < (8*(360/8)) and Φ > (7*(360/8)):
                                    Φ_box[Magnitude_index][7].append(Φ)
                                    magnitude_box[Magnitude_index][7].append(magnitude)
    return Φ_box, magnitude_box
                              

#Beskriving: Funktionen tar in en avskuren bild och beräknar skillnaden i x- och y-led för varje pixel förutom de yttersta punkterna. I den nästlade for-loopen kallar den på funktionen magnitude_orientation med samtliga Gx och Gy värden som input. 
#cropped_image: IMG - Avskuren bild med måtten 50 x 50
#Magnitude_index: Interger - Integer som är index för vilken bricka som beräknas
#Φ_box: Array - Array som innehåller fler arrayer vars innehåll är de beräknade pixlarnas riktning
#magnitude_box: Array - Array som innehåller fler arrayer vars innehåll är de beräknade pixlarnas storlek
#return: Array - Returnerar arrayerna magnitude_box och Φ_box inplace med beräknade värden för magnitud och orientation. 
#by: Emil Crogård
#date: 2022-05-29
def Light_values(cropped_image, Magnitude_index, Φ_box, magnitude_box):
    ga = np.array(cropped_image)
    w = 1
    h = 1
    Gy = 0
    Gx = 0
    for w in range(1,49):
        for h in range(1,49):
            Gy = int(ga[w, h-1]) - int(ga[w, h+1])
            Gx = int(ga[w-1, h]) - int(ga[w+1, h])
            Φ_box, magnitude_box = magnitude_orientation(Gx, Gy, Magnitude_index, Φ_box, magnitude_box)
    return Φ_box, magnitude_box
                 
#Beskriving: Funktionen tar in en img-fil och skapar en ny avskärmad img-fil med måtten 50x50 i två nästlade for-loopar. Det skapas totalt 16 avskärmade brickor av den ursprungliga bilden. Den kallar även på funktionen Light_values med respektive avskärmade bild som input. Avslutningsvis beräknar den genomsnittliga värdet för varje sorterad array i både Φ_box och magnitude_box.
#gaussian: IMG - En img-fil som är suddig med dimensionerna 200 x 200
#return: Array - Returnerar arrayerna Φ_box och magnitude_box med genomsnittliga värden i varje sorterad array
#by: Emil Crogård
#date: 2022-05-29
def image_shaping(gaussian):
    magnitude_box = [[[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []]]
    Φ_box =  [[[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []]]
    
    Magnitude_index = 0
    j = 0
    k = 0 
    while j < 4:
        x1 = j*50
        x2 = (j+1)*50
        while k < 4:
            y1 = k*50
            y2 = (k+1)*50 
            k += 1
            cropped_image = gaussian.crop((x1, y1, x2, y2))
            Φ_box, magnitude_box = Light_values(cropped_image, Magnitude_index, Φ_box, magnitude_box)
            Magnitude_index += 1
        j+=1
        k = 0
    
    i = 0
    a = 0
    m = 0
    summary = 0
    average = 0
    while a < len(magnitude_box):
        while i < len(magnitude_box[a]):
            while m < len(magnitude_box[a][i]):
                summary += magnitude_box[a][i][m]
                m += 1
            if len(magnitude_box[a][i]) != 0:
                average = summary / len(magnitude_box[a][i])
                del magnitude_box[a][i][0:len(magnitude_box[a][i])]
                magnitude_box[a][i].insert(0, average)
            m = 0
            summary = 0
            i += 1 
        i = 0
        a += 1    
    a = 0
    i = 0
    m = 0
    while a < len(Φ_box):
        while i < len(Φ_box[a]):
            while m < len(Φ_box[a][i]):
                summary += Φ_box[a][i][m]
                m += 1
            if len(Φ_box[a][i]) != 0:
                average = summary / len(Φ_box[a][i])
                del Φ_box[a][i][0:len(Φ_box[a][i])]
                Φ_box[a][i].insert(0, average)
            m = 0
            summary = 0
            i += 1 
        i = 0
        a += 1  
    return Φ_box, magnitude_box
    
#Beskriving: Programmets main-funktion som tar in en bild och konverterar den till storleken 200 x 200 samt gör den suddig med hjälp av en gaussian-blur. Den kallar även på funktionen image_shaping med nya img-filen som input för att starta resten av programmet. Till sist printar arrayerna för magnitud och riktning.
#by: Emil Crogård
#date: 2022-05-29
def main(): 
    search = input("Skriv in sökvägen till valfri bild\n")
    image = Image.open(r"%s" % (search)).convert('L')
    new_image = image.resize((200, 200))
    gaussian = new_image.filter(ImageFilter.GaussianBlur(radius = 3))
    Φ_box, magnitude_box = image_shaping(gaussian)
    print("magnitude_box\n", magnitude_box)
    print("Φ_box\n", Φ_box)
    exit(0)
    
    
main()