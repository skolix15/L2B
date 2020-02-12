def Lp2_Gram_Problem():

    # Arxh tou kwdika
    global fp
    file_name = "LP-1.txt"

    try:

        fp = open(file_name,"r")  # Anoigei to arxeio me to onoma pou dwthike apo ton xrhsth kai apothikeythke sthn metabliti file_name

    except IOError:

        print("The file you wanted to open, it doesn't exist..")
        exit (1)

    gram_problem = []         # Pinakas pou tha filoxenisei olo to grammiko problima
    c = []                    # Pinakas pou tha periexei olous tous syntelestes ths antikeimenikis synarthshs
    b = []                    # Pinakas pou tha periexei olous tous arithmitikous periorismous twn grammwn-periorismwn
    Eqin = []                 # Pinakas pou tha periexei katalliles times analoga me to symbolo isotitas/anisotitas kathe grammis
    MinMax = []               # Pinakas pou tha periexei katallilh timh analoga me to an to grammiko problima einai megistopoihshs
                                  # h an einai elaxistopoihshs
    A = []                    # Pinakas pou tha perixei olous tou syntelestes twn grammwn/periorismwn
    count_lines = 0           # Metabliti pou katagrafei to plithos twn grammwn pou periexei to arxeio/grammiko problima
    x = []                    # Pinakas pou tha periexei ta "x"
    lines = ""                # Metabliti mesw ths opoias tha diabazetai grammi grammi to arxeio/grammiko problima
    its_last_line = False     # Metabliti mesw ths opoias tha ginetai gnwsto mesa ston kwdika an kapoia grammi pou
                              # diabastike einai h teleytaia grammi tou arxeiou/grammikou problimatos

    # Se auto to shmeio xekinaei h anagnwsi tou arxeiou/grammikou problimatos, grammi grammi

    for line in fp:

        lines = line

    # An yparxei kenh grammi mesa sto arxeio prospernatai

        if (lines.isspace()):
            continue

    # Aparithmeitai to plithos twn symbolown (-) kai (+) sthn kathe grammi

        crowd_of_symbols = lines.count('+')
        crowd_of_symbols += lines.count('-')

    # Me ta parakatw if aparithmeitai to plithos twn sygkritikwn symbolwn sthn kathe grammi

        if (lines.find('>=') != -1):
            crowd_of_comparison_symbol = lines.count('>=')

        elif (lines.find('<=') != -1):
            crowd_of_comparison_symbol = lines.count('<=')

        elif (lines.find('=') != -1):
            crowd_of_comparison_symbol = lines.count('=')

    # Me auto to if ginetai antilipto ston kwdika mesa an einai h teleutaia grammi tou arxeiou/grammikou problimatos

        if (crowd_of_comparison_symbol > 1):
            crowd_of_comparison_symbol = lines.count('=')
            its_last_line = True

    # Me ta parakatw if perniountai oi katallhles times ston pinaka Eqin analoga me to eidos twn periorismwn

        if (lines.find('>=') != -1 and count_lines != 0 and not (its_last_line)):
            Eqin.append(1)

        elif (lines.find('<=') != -1 and count_lines != 0 and not (its_last_line)):
            Eqin.append(-1)

        elif (lines.find('=') != -1 and count_lines != 0 and not (its_last_line)):
            Eqin.append(0)

    # Ginontai kapoioi parapanw elegxoi eidika sthn prwth grammi tou arxeiou/grammikou problimatos logw kapoiwn
    # idiaiterwn xarakthristikwn pou ayth exei, opws px o prosdiorismos tou problimatos me tis lexeis "Min" h "Max"

        if (count_lines == 0):

            crowd_of_x = lines.count('x')

            if (lines.find('max') != -1):
                crowd_of_x -= 1

            if (lines.find('max') == -1 and lines.find('min') == -1):
                print("It doesn't exist the word 'min' or 'max' in your problem.")

            elif (lines.find('max') != -1):
                MinMax.append(1)

            else:
                MinMax.append(-1)

    # Ginontai kapoioi parapanw elegxoi eidika sthn deuteri grammi tou arxeiou/grammikou problimatos logw kapoiwn
    # idiaiterwn xarakthristikwn pou ayth exei, opws px h lexi "s.t." pou prosdiorizei thn arxh katagrafis twn periorismwn

        if (count_lines == 1):

            if (lines.find('s.t.') == -1 and lines.find('st') == -1 and lines.find('subject to') == -1):
                print("It doesn't exist a word that specifies the technological restrictions.")

    # 1. Fainetai me to prwto if an den yparxei to sygkritiko symbolo se kathe enan periorismo
    # 2. Fainetai me to deutero if an den yparxei to anamenomeno plithos sygkritikwn symbolwn
    #    sthn teleutaia grammi tou problimatos sygkekrina

        if (count_lines != 0 and crowd_of_comparison_symbol == 0 and (not its_last_line)):
            print("It doesn't exist comparison symbol in the restriction", count_lines)

        elif (its_last_line and crowd_of_comparison_symbol != crowd_of_x):
            print("It doesn't exist comparison symbol in the last restriction")

    # Kathe grammi diaspatai se kathe melos ths csexwrista kai apomakrinei tyxon keno (white spaces genikotera)

        lines = lines.split()

    # 1. Me to prwto if elegxetai an yparxei arithmos meta to sygkritiko symbolo se kathe grammi/periosmo
    # 2. Me to deutero if elegxetai an yparxei '0' meta ta sygkritika symbola sthn teleytaia grammi/periosmo tou problimatos

        if (lines[lines.__len__() - 1].find('=') != -1 or lines[lines.__len__() - 1].find('>') != -1 or lines[
            lines.__len__() - 1].find('<') != -1
                and (not its_last_line) and count_lines != 0):
            print("It doesn't exist any number after the comparison symbol in restriction", count_lines)

        elif (its_last_line and (lines.count('0') + lines.count('0,') != crowd_of_comparison_symbol)):
            print("It doesn't exist '0' after a comparison symbol in the last restriction")

    # H diaspasmeni grammi pernietai ston pinaka gram_problem poy anamenetai na filoxenisei olo to grammiko problima

        gram_problem.append(lines)

    # 1. Me to prwto if ginetai elegxos gia ta symbola (-) kai (+) sthn antikeimenikh synarthsh
    # 2. Me to deutero if ginetai elegxos gia ta symbola (-) kai (+) stous periorismous

        if (count_lines == 0 and crowd_of_symbols < (crowd_of_x - 1)):
            print("It exists a mistake with the signs in the objective function.")

        elif (count_lines != 0 and crowd_of_symbols < (crowd_of_x - 1)):
            if (not its_last_line):
                print("It exists a mistake with the signs in the restriction", count_lines)

    # Teleiwnoun oi elegxoi sthn proigoumeni grammi tou problimatos, ayxanetai h metabliti count_lines kai teleiwnei to kommati
    # tou while

        count_lines += 1

    fp.close()

    # Me to parakatw kommati tou kwdika afairountai apo ton pinaka gram_problem apo thn kathe grammi tou, opoiadhpote timi den periexei
    # "x" h "-" h apla kapoion arithmo
    # Ystera egxwrountai ston pinaka b oi arithmoi pou yphrxan se kathe periorismo meta to sygkritiko symbolo
    # Afou perastoun oi parapanw arithmoi ston pinaka b, afairountai apo ton pinaka gram_problem
    # Telika ston pinaka gram_proble periexontai mono oi times pou periexoun "x" kai oi times pou periexoun "-"

    j = 0
    negative_sign = '-'

    while (j != count_lines):

        gram_problem[j] = [i for i in gram_problem[j] if (
                    i != "=" and i != "<=" and i != ">=" and i != "max" and i != "s.t." and i != "z" and i != "+"
                    and i != "st" and i != "subject to") and i !="min"]

        for k in range(1, len(gram_problem[j]) - 1):

            if (gram_problem[j][k].find('-') != -1 and j != (count_lines - 1)):

                if (not gram_problem[j][k].__contains__("x")):
                    gram_problem[j][k + 1] = negative_sign + gram_problem[j][k + 1]

        if (j != 0 and j != count_lines - 1):
             b.append(gram_problem[j][len(gram_problem[j]) - 1])

        gram_problem[j] = [i for i in gram_problem[j] if (i != "-" or (i.__contains__("x")))]

        j += 1

    # Me to parakatw kommati tou kwdika afairountai apo ton pinaka gram_problem apo thn kathe grammi tou kai apo thn kathe timi tou,
    # ta "x" mazi me ton deikti tous ( px x1, x2, ...)
    # Epipleon kataxwrountai oi syntelestes twn "x" ths antikeimenikhss synarthshss ston pinaka c kai oi syntelestes twn
    # "x" twn periorismwn ston pinaka A

    j = 0
    g = "x"
    f = "w"
    w = []          # Pinakas pou tha periexei ta w

    while (j != count_lines):

        if (j != count_lines - 1 and j != 0):
            A.append([])

        for i in range(crowd_of_x):
            g += str(i + 1)
            f += str(i + 1)
            gram_problem[j][i] = gram_problem[j][i].replace(g, '')

            if (j == 0):
                c.append(gram_problem[j][i])

            elif (j > 0 and j != count_lines - 1):
                A[j - 1].append(gram_problem[j][i])

            elif (j == count_lines - 1):
                x.append(x)
                w.append(f)


            g = "x"
            f = "w"

        j += 1

    # Metatropi twn pinakwn apo grammiki morfi se dyikh morfi

    temp = c        # O temp einai bohthitikos pinakas gia thn antallagi timwn twn dyo pinakwn ( c kai b )
    c = b
    b = temp

    new_A = []      # Pinakas pou periexei tous kainourgioys syntelestes twn "w"
    count = 0       # Arithmitis

    # Se periptwsh mh yparcsis syntelesti se kapoion agnwsto, opote ennoeitai to 1 h to -1, ginetai elegxos kai pernietai h timh 1 an
    # yparxei nwritera to symbolo "+" h -1 an yparxei nwritera to symbolo "-"
    # Ayto ginetai gia tis times tou b ( paliou c ), diladi gia tous syntelestes thn antikeimenikis synarthshs

    for i in range(len(b)):
        if (b[i] == " " or b[i] == "" or b[i] == "-"):
            if (b[i]== "-"):
                b[i] = "-1"
            else:
                b[i] = "1"

    # Antistrofi grammwn kai stilwn tou Pinaka A kai topothetisi katallila ston pinaka new_A
    # Epipleon, se periptwsh mh yparcsis syntelesti se kapoion agnwsto, opote ennoeitai to 1 h to -1,
    # ginetai elegxos kai pernietai h timh 1 an
    # yparxei nwritera to symbolo "+" h -1 an yparxei nwritera to symbolo "-"
    # Ayto ginetai gia tis times tou A, diladi gia tous syntelestes twn periosmwn

    for j in range(len(A[0])):
        new_A.append([])
        for i in range(len(A)):
            if(A[i][j] == " " or A[i][j] == "" or A[i][j] == "-"):
                if(A[i][j] == "-"):
                    new_A[count].append("-1")
                else:
                    new_A[count].append("1")
            else:
                new_A[count].append(A[i][j])
        count += 1

    # Eggrafh tou grammikou problimatos sto kainourgio arxeio me th nea morfh tou

    try:

    # Dimiourgia enos kainourgiou txt arxeiou, pros grapsimo, me to onoma "lp_2.txt"

        lp_2 = open("LP-2.txt", "w")

    # Dimiourgia mias metablhths string pou se aythn tha katagraftoun ola ta apotelesmata kai ystera ayth tha perastei
    # sto kainourgio arxeio

        string_text = ''

    # Katagrafetai h lexi "Max" h "Min" sthn metabliti string_text analoga me thn timh pou periexetai ston pinaka MinMax

        if (MinMax[0] == 1):
            string_text += "Min"

        elif (MinMax[0] == -1):
            string_text += "Max"

    # Katagrafetai sthn metablhth string_text olos o pinakas pou periexei tous syntelestes twn w ths antikeimenikhs synarthshs

        string_text += "\t[  "
        for i in range(len(c)):
            string_text += c[i] + "  "

        string_text += "] [  "

    # Katagrafetai sthn metablhth string_text olos o pinakas pou periexei ta "w"

        for i in range(len(w)):
            string_text += w[i] + "  "

        string_text += "]\n"

    # Katagrafetai sthn metablhth string_text h frash "s.t." pou ypodeiknyei thn enarxh katagrafis twn periorismwn

        string_text += "\ns.t.\t[  "

    # Katagrafetai sthn metablhth string_text olos o pinakas pou periexei tous syntelestes twn "w" twn periorismwn

        for i in range(len(new_A)):
            string_text += "[  "
            for j in range(len(new_A[i])):
                string_text += new_A[i][j] + "  "
            string_text += "] "

        string_text += "]\t[  "

    # Katagrafetai sthn metablhth string_text olos o pinakas pou periexei ta "w"

        for i in range(len(w)):
            string_text += w[i] + "  "

        string_text += "]\t[  "

    # Katagrafontai sthn metablhth string_text ta katallhla sygkritika symbola twn periorismwn
    # analoga me tis times pou periexei o pinakas Eqin

        if (MinMax[0] == -1):
           for i in range(len(Eqin)):
               string_text += "<= "

           string_text += "]\t[  "

        elif (MinMax[0] == 1):
           for i in range(len(Eqin)):
               string_text += ">= "

           string_text += "]\t[  "

    # Katagrafetai sthn metablhth string_text olos o pinakas pou periexei tis times pou briskontai
    # meta ta sygkritika symbola stis grammes twn periorismwn tou grammikou problimatos

        for i in range(len(b)):
            string_text += b[i] + "  "

        string_text += "]\n\n\t\t"

        string_w= "w"

    # Katagrafetai sthn metablhth string_text olos o pinakas pou periexei ta "w", mazi me ton periosmo tous

        if (MinMax[0] == -1):

            for i in range(crowd_of_x - 1):

                string_text += w[i]

                if(Eqin[i] == -1):
                    string_text += " >= 0 , "
                elif(Eqin[i] == 0):
                    string_text += " free , "
                elif(Eqin[i] == 1):
                    string_text += " <= 0 , "

            string_w += str(i + 2)
            string_text += string_w

            if (Eqin[i] == -1):
                string_text += " <= 0"
            elif (Eqin[i] == 0):
                string_text += " free"
            elif (Eqin[i] == 1):
                string_text += " >= 0"

        elif (MinMax[0] == 1):

            for i in range(crowd_of_x - 1):

                string_text += w[i]

                if (Eqin[i] == -1):
                    string_text += " <= 0 , "
                elif (Eqin[i] == 0):
                    string_text += " free , "
                elif (Eqin[i] == 1):
                    string_text += " >= 0 , "

            string_w += str(i + 2)
            string_text += string_w

            if (Eqin[i] == -1):
                string_text += " >= 0"
            elif (Eqin[i] == 0):
                string_text += " free"
            elif (Eqin[i] == 1):
                string_text += " <= 0"

    # Telos katagrafetai h metablhth string_text sto arxeio pou dhmiourgithike

        lp_2.write(string_text)

    finally:
        lp_2.close()

    # Telos tou kwdika

Lp2_Gram_Problem()



