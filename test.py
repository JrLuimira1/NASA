


#Authors:
#Luigi Miranda
#Paul SIlva
#Daniel Ortega

from PIL import Image

from numpy import asarray

import numpy as np

from scamp import*
import matplotlib.pyplot as plt



img = Image.open("MIRI_1.png")
numpydata = asarray(img)
#######################################################################################################################################################################
#This condition is when an image is not so complex. When It is only a 2D array, so we add an artificie. We add a third element in "amount" list for having a 3D array
amount = []
amount1 = numpydata.shape
for y in amount1:
    amount.append(y)



valores_promedio_1 = []
if len(amount)<3:
    amount.append(4)
    


print(amount1)
print(amount)


########################################################################################################
#Here we use "numpydata", and we make a vertical sum in order to make a resume of the values
valores_promedio_1 = []
for i in numpydata:
    for k in i:
        suma = (np.sum(k,axis=0)/amount[2])
        valores_promedio_1.append(round(suma))
        

print(valores_promedio_1[1])
#print(valores_promedio_1[1:5])
print(len(valores_promedio_1))
#print(valores_promedio_1)
print(numpydata[1])
print(numpydata)

##############################################################################################################
#EXPERIMENTO: Eliminate the repited elements of "no_repetidos_1"
no_repetidos_1 = []
for numero in valores_promedio_1:
    if numero not in no_repetidos_1:
        no_repetidos_1.append(numero)

print(no_repetidos_1)
print(len(no_repetidos_1))

###########################################################


print(max(no_repetidos_1))
#############################################################################################################
#We use Scamp library for creating the sound
s = Session(tempo=120)
#clarinet = s.new_part("clarinet")
piano = s.new_part("piano")
#jazz = s.new_part("jazz")
violin = s.new_part("violin")
oregan = s.new_part("Organ")
cello = s.new_part("cello")
#s.print_default_soundfont_presets()



##############################################################################################################
#Here dependen on the Pitch, some values are increse for making a more complex music
oregan.play_note(80,0.8,2)
i=0
for nota in no_repetidos_1:
    print(nota)
    if nota <50:
        cello.play_note(nota+20,0.8,1)
        piano.play_note(nota+38,0.8,0.5)
        violin.play_note(nota+31,0.8,1)
        piano.play_note(nota+27,0.5,0.5)
        violin.play_note(nota+17,0.8,1)
        #jazz.play_note(nota,0.8,0.5)
    if nota >50 and nota <100:
        cello.play_note(nota,0.8,1)
        #piano.play_note(nota+12,0.8,0.5)
        #violin.play_note(nota+9,0.8,1)
        #piano.play_note(nota+13,0.5,0.5)
        #violin.play_note(nota,0.8,1)
    if nota >100 and nota <150:
        #cello.play_note(nota,0.8,1)
        piano.play_note(nota-34,0.8,0.5)
        #violin.play_note(nota-58,0.8,1)
        piano.play_note(nota-40,0.5,0.5)
        #violin.play_note(nota,0.8,1)
    if nota >150 and nota <200:
        #cello.play_note(nota,0.8,1)
        #piano.play_note(nota-80,0.8,0.5)
        violin.play_note(nota-100,0.8,1)
        #piano.play_note(nota-90,0.5,0.5)
        violin.play_note(nota,0.8,1)
    if nota >200 and nota <255:
        cello.play_note(nota,0.8,1)
        #piano.play_note(nota-150,0.8,0.5)
        violin.play_note(nota-160,0.8,1)
        #piano.play_note(nota-160,0.5,0.5)
        violin.play_note(nota-175,0.8,1)

#####################################################################################################################################       
