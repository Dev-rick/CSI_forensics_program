# -*- coding: utf-8 -*-

print "Welcome to the CSI forensics program!"

hair_colors = {
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC"
}

facial_shapes = {
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA"
}

eye_colors = {
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC"
}

genders = {
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC"
}

races = {
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG"
}

suspects = {
    "Eva":["Female", "White", "Blonde", "Blue", "Oval"],

    "Larisa":["Female", "White", "Brown", "Brown", "Oval"],

    "Matej":["Male","White","Black","Blue","Oval"],

    "Miha":["Male", "White", "Brown", "Green", "Square"]

}

dna_file = open('dna.txt', 'r')
searched_dna = dna_file.read()
dna_file.close()

criminal = []

for gender in genders:
    if searched_dna.find(genders[gender]) > 0: #mit find hinter einem string object, wird in diesem str nach dem str in der Klammer gesucht und wenn dieser gefunden wurde gibt Python eine positive Zahl wieder.
        print "\n\nThe criminal has the folowing gender:\n>>", gender
        criminal.append(gender)

for race in races:
    if searched_dna.find(races[race]) > 0:
        print "\nThe criminal has the following race:\n>>", race
        criminal.append(race)

for hair_color in hair_colors:
    if searched_dna.find(hair_colors[hair_color]) > 0:
        print "\nThe criminal has the following hair color:\n>>", hair_color
        criminal.append(hair_color)

for eye_color in eye_colors:
    if searched_dna.find(eye_colors[eye_color]) > 0:
        print "\nThe criminal has the following eye color:\n>>", eye_color
        criminal.append(eye_color)

for facial_shape in facial_shapes:
    if searched_dna.find(facial_shapes[facial_shape]) > 0:
        print "\nThe criminal has the following facial shape:\n>>", facial_shape
        criminal.append(facial_shape)



for i in suspects: #i ist hier ein str, passt sich immer dem Inhalt (hier ein dict, also strings) an.
    if suspects[i] == criminal: #Mit suspects[i] greife ich auf die verschiedenen Listen im dict zu!
        print "\n\nYour criminal who ate the ice cream is:\n>>", i
