slovo1 = ["S","L","O","V","O"]
slovo2 = [u"Х",u"О",u"М",u"Я",u"К"]
slovo3 = [u"А",u"Л",u"М",u"А",u"З"]
slovo4 = [u"С",u"К",u"А",u"Л",u"А"]
slovo5 = [u"Р",u"У",u"И",u"Н",u"А"]
def setup():
    textSize(60)
    fullScreen()
    strokeWeight(1)
    
    fill(0,0,255)
    rect(50,50,60,60)# КВ 1
    rect(110,50,60,60)# КВ 2
    rect(170,50,60,60)# КВ 3
    rect(230,50,60,60)# КВ 4
    rect(290,50,60,60)# КВ 5
    fill(0)
    text("eng",370,100)
    fill(0,0,255)
    # СЛЕДУШЕЕ СТРОКИ ЭТО 2 СЛОВО
    rect(50,150,60,60)# КВ 1
    rect(110,150,60,60)# КВ 2
    rect(170,150,60,60)# КВ 3
    rect(230,150,60,60)# КВ 4
    rect(290,150,60,60)# КВ 5
    # 3 C K
    rect(50,250,60,60)# КВ 1
    rect(110,250,60,60)# КВ 2
    rect(170,250,60,60)# КВ 3
    rect(230,250,60,60)# КВ 4
    rect(290,250,60,60)# КВ 5
    # 4 C K
    rect(50,350,60,60)# КВ 1
    rect(110,350,60,60)# КВ 2
    rect(170,350,60,60)# КВ 3
    rect(230,350,60,60)# КВ 4
    rect(290,350,60,60)# КВ 5
    # 5 C K
    rect(50,450,60,60)# КВ 1
    rect(110,450,60,60)# КВ 2
    rect(170,450,60,60)# КВ 3
    rect(230,450,60,60)# КВ 4
    rect(290,450,60,60)# КВ 5
    fill(0)
    text(u"рус",370,200)
    textSize(60)
    fill(255)
def draw():
    global slovo1,slovo2,slovo3,slovo4,slovo5
    if keyPressed:
        if key == slovo1[0]:
            text(slovo1[0],60,100)# Б 1
    if keyPressed:
        if key == slovo1[1]:
            text(slovo1[1],120,100)# Б 2
    if keyPressed:
        if key == slovo1[2]:
            text(slovo1[2],178,100)# Б 3
    if keyPressed:
        if key == slovo1[3]:
            text(slovo1[3],240,100)# Б 4
    if keyPressed:
        if key == slovo1[4]:
            text(slovo1[4],300,100)# Б 5
    # 2 С Б
    if keyPressed:
        if key == slovo2[0]:
            text(slovo2[0],60,200)# Б 1
    if keyPressed:
        if key == slovo2[1]:
            text(slovo2[1],118,200)# Б 2
    if keyPressed:
        if key == slovo2[2]:
            text(slovo2[2],177,200)# Б 3
    if keyPressed:
        if key == slovo2[3]:
            text(slovo2[3],240,200)# Б 4
    if keyPressed:
        if key == slovo2[4]:
            text(slovo2[4],300,200)# Б 5
    # 3 С Б
    if keyPressed:
        if key == slovo3[0]:
            text(slovo3[0],60,300)# Б 1
    if keyPressed:
        if key == slovo3[1]:
            text(slovo3[1],118,300)# Б 2
    if keyPressed:
        if key == slovo3[2]:
            text(slovo3[2],177,300)# Б 3
    if keyPressed:
        if key == slovo3[3]:
            text(slovo3[3],240,300)# Б 4
    if keyPressed:
        if key == slovo3[4]:
            text(slovo3[4],300,300)# Б 5
    # 4 С Б
    if keyPressed:
        if key == slovo4[0]:
            text(slovo4[0],60,400)# Б 1
    if keyPressed:
        if key == slovo4[1]:
            text(slovo4[1],118,400)# Б 2
    if keyPressed:
        if key == slovo4[2]:
            text(slovo4[2],177,400)# Б 3
    if keyPressed:
        if key == slovo4[3]:
            text(slovo4[3],240,400)# Б 4
    if keyPressed:
        if key == slovo4[4]:
            text(slovo4[4],300,400)# Б 5
    # 5 С Б
    if keyPressed:
        if key == slovo5[0]:
            text(slovo5[0],60,500)# Б 1
    if keyPressed:
        if key == slovo5[1]:
            text(slovo5[1],118,500)# Б 2
    if keyPressed:
        if key == slovo5[2]:
            text(slovo5[2],177,500)# Б 3
    if keyPressed:
        if key == slovo5[3]:
            text(slovo5[3],240,500)# Б 4
    if keyPressed:
        if key == slovo5[4]:
            text(slovo5[4],300,500)# Б 5Ф
    
