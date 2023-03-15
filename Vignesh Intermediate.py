playlist1 = ["Solo by Future", "After Dark by Mr.Kitty","Those Eyes by New West","Golden Hour by JVKE","505 by Arctic Monkeys"]
         
playlist2 = ["No Surprises by Radiohead", "Viva La Vida by Coldplay","Woo by Rihanna", "Bad habit by Steve Lacy", "Hope by NF"]

playlist3 = ["Glue Song by beabadoobee", "About You by 1975","Nonsense by Sabrina Carpenter", "Bad habit by Steve Lacy", "Midnight Rain by Taylor Swift"]

song = input("What song do you want to check? ")
num_of_appears = 0


def exclusive(song,num_of_appears, playlist1, playlist2, playlist3):
    for i in range (0,5):
        if song == playlist1[i]:
            num_of_appears = num_of_appears + 1
    for i in range (0,5):
        if song == playlist2[i]:
            num_of_appears = num_of_appears + 1
    for i in range (0,5):
        if song == playlist3[i]:
            num_of_appears = num_of_appears + 1
    print ("this song appears " + str(num_of_appears) + " times")
    if num_of_appears != 1:
        return False
    else:
        return True
    

print (exclusive(song,num_of_appears, playlist1, playlist2, playlist3))
