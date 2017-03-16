# -*- coding: utf-8 -*-

print "Welcome to the CSI forensics program!"

hair_color = {
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC"
}

facial_shape = {
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA"
}

eye_color = {
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC"
}

gender = {
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC"
}

race = {
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

for i in gender:
    if searched_dna.find(gender[i]) > 0: #mit find hinter einem string object, wird in diesem str nach dem str in der Klammer gesucht und wenn dieser gefunden wurde gibt Python eine positive Zahl wieder.
        print "\n\nThe criminal has the folowing gender:\n>>", i
        criminal.append(i)

for i in race:
    if searched_dna.find(race[i]) > 0:
        print "\nThe criminal has the following race:\n>>", i
        criminal.append(i)

for i in hair_color:
    if searched_dna.find(hair_color[i]) > 0:
        print "\nThe criminal has the following hair color:\n>>", i
        criminal.append(i)

for i in eye_color:
    if searched_dna.find(eye_color[i]) > 0:
        print "\nThe criminal has the following eye color:\n>>", i
        criminal.append(i)

for i in facial_shape:
    if searched_dna.find(facial_shape[i]) > 0:
        print "\nThe criminal has the following facial shape:\n>>", i
        criminal.append(i)



for i in suspects:
    if suspects[i] == criminal: #Mit suspects[i] greife ich auf die verschiedenen Listen im dict zu!
        print "\n\nYour criminal who ate the ice cream is:\n>>", i
