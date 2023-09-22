def voornaam_check(voornaam: str):
    if len(voornaam) > 2 and len(voornaam) < 10 and voornaam.isalpha() is True and voornaam[0] == voornaam[0].upper():
        return False
    else:
        return True


def achternaam_check(achternaam: str):
    if len(achternaam) > 2 and len(achternaam) < 10 and achternaam.isalpha() is True and achternaam[0] == achternaam[0].upper():
        return False
    else:
        return True


def werk_check(functie: str):
    if len(functie) >= 10 and functie.isalpha() is True:
        return False
    else:
        return True


def salary_check(salaris: str):
    if salaris[2] == "." and salaris[6] == ",":

        salaris = salaris.replace(".", "")
        salaris = salaris.replace(",", ".")
        salaris = float(salaris)

        if salaris >= 20000 and salaris <= 80000:
            return False
    else:
        return True


def datum_check(datum:str):
    
    datum = datum.split("-")
    
    jaar = int(datum[0])
    maanden = int(datum[1])
    dagen = int(datum[2])

    if maanden not in range(1, 13):
        print("input error")
        return True
    elif dagen not in range(1, 32):
        print("input error")
        return True

    elif jaar == 2021 or jaar == 2022:

        return False
    else:
        print("input error")
        return True

running = True
while running is True:
    letters = input("more letters? (Yes or No): ")

    if letters == "yes":
        job_offer = input("job offer or rejection: ")
        if job_offer == "job offer":

            voornaam_check_2 = True
            while voornaam_check_2:
                voornaam = input("vul je voornaam in: ")
                voornaam_check_2 = voornaam_check(voornaam)

            achternaam_check_2 = True
            while achternaam_check_2:
                acthernaam = input("vul je achternaam in: ")
                achternaam_check_2 = achternaam_check(acthernaam)

            werk_check_2 = True
            while werk_check_2:
                functie = input("vul je funcie in: ")
                werk_check_2 = werk_check(functie)

            salary_check_2 = True
            while salary_check_2:
                salaris = input("vul je salaris in: ")
                salary_check_2 = salary_check(salaris)

            datum_check_2 = True

            while datum_check_2:
                datum = input("vul je datum in: ")
                datum_check_2 = datum_check(datum)
            print(f"""Here is the final letter to send:
                            Dear {voornaam} {acthernaam}, 
                            After careful evaluation of your application for the position of {functie}, 
                            we are glad to offer you the job. Your salary will be {salaris} euro annually. 
                            Your start date will be on {datum}. Please do not hesitate to contact us with any questions. 
                            Sincerely, 
                            HR Department of XYZ """)    

        if job_offer == "rejection":
            voornaam_check_2 = True
            while voornaam_check_2:
                voornaam = input("vul je voornaam in: ")
                voornaam_check_2 = voornaam_check(voornaam)

            achternaam_check_2 = True
            while achternaam_check_2:
                acthernaam = input("vul je achternaam in: ")
                achternaam_check_2 = achternaam_check(acthernaam)

            werk_check_2 = True
            while werk_check_2:
                functie = input("vul je funcie in: ")
                werk_check_2 = werk_check(functie)

            feedback = input("yes or no feedback: ")

            if feedback == "yes":
                feedback_twee = input("feedback: ")

                print(f"""Here is the final letter to send:
                            Dear {voornaam}{acthernaam}, 
                            After careful evaluation of your application for the position of {functie}, 
                            at this moment we have decided to proceed with another candidate. 
                            Here we would like to provide you our feedback about the interview.
                            {feedback} 
                            We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
                            Sincerely, 
                            HR Department of XYZ """)
            if feedback == "no":
                print(f"""Here is the final letter to send:
                            Dear {voornaam}{acthernaam}, 
                            After careful evaluation of your application for the position of {functie}, 
                            at this moment we have decided to proceed with another candidate. 
                            We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
                            Sincerely, 
                            HR Department of XYZ """)
        
    elif letters == "no":
        quit()