import time
import os
import random

water_counter = 20

def sommen_oplossen():
    print("1. 15 + 27 = ?")
    print("2. 48 - 19 = ?")
    print("3. 6 x 8 = ?")
    print("4. 72 ÷ 9 = ?")
    print("5. 3² + 4² = ?")

    # Start een timer van 10 seconden
    start_time = time.time()
    end_time = start_time + 30

    while time.time() < end_time:
 
 
        wachtwoord_controle = input(">> ")

        if time.time() > end_time:
            print("Je bent te laat")
            return 

        if wachtwoord_controle == "422948825":
            print("Je bent net op tijd met het invullen van het wachtwoord en met een beetje ruwe landing land je op Saturnus.")
            return True
        
        else:
            print("Helaas, het wachtwoord is niet correct.")
            
    # Als de timer afloopt zonder het wachtwoord in te voeren
    print("Helaas, je bent te laat met het invullen van het wachtwoord.")
    print("De deur blijft gesloten.")


def clear_screen():
    os.system('cls')

def water_visual_functie():
    global water_visual
    print("WATER COUNTER:")
    water_visual = "⬜ "*water_counter
    print(f"[{water_visual}]")

def timer_functie():
    global seconden
    seconden = 10
    while seconden > 0:
        time.sleep(1)
        seconden -= 1
        if seconden == 100:
            print("Je hebt nog 100 seconden")
        if seconden == 0:
            print("Je bent gestorven")
            return False


def mercury_landing():
    print(f"Het ruimteschip van {speler_naam} landt veilig op Mercurius.\n")
    time.sleep(5)
    print(f"De omgeving voelt anders aan dan verwacht; het is verrassend koel en mistig.\n")
    time.sleep(5)
    print(f"{speler_naam} stapt uit het schip en begint zijn verkenning van deze vreemde planeet.\n")
    time.sleep(5)
    if mercury_completion == False:
        print(f"**Doel op Mercurius**: {speler_naam} is op zoek naar leven zodat die hem kunnen helpen met de zoektocht naar de zender van de boodschap.\n")
        time.sleep(5)
    print(f"{speler_naam} begint zijn zoektocht in de dichte mistige laaglanden van Mercurius.\n")
    time.sleep(5)
    print("De mist belemmert het zicht, waardoor je niet kan zien welke kant je op gaat.\n")
    time.sleep(5)
    print("...")
    time.sleep(5)
    clear_screen()


def venus_landing():
    global water_counter

    print(f"Het schip landt op Venus.\n")
    time.sleep(5)
    print(f"{speler_naam} begint meteen te zweten door de hitte.\n")
    time.sleep(5)
    print(f"{speler_naam}: Het is hier ongelofelijk heet. Ik moet dringend op zoek naar water!\n")
    time.sleep(3)
    if venus_completion == False:
        print("WATER COUNTER TOEGEVOEGD\n ")
        water_counter = 10
        water_visual_functie()
    
    time.sleep(5)
    print(f"{speler_naam} staat nu op de verzengende oppervlakte van Venus, en de hitte is overweldigend. De zoektocht naar water wordt dringend, want overleven in deze extreme omstandigheden is geen gemakkelijke taak.\n")
    time.sleep(5)
    if venus_completion == False:
        print(f"Doel op Venus: {speler_naam} moet water vinden om te kunnen overleven en tegelijkertijd op zoek gaan naar aanwijzingen over de herkomst van het buitenaardse bericht.\n")
        time.sleep(7)
        
    print("De oppervlakte is bezaaid met rotsen en vulkanische formaties. Je voelt de zon branden op je huid samen met de zure regen.\n")
    time.sleep(5)


def speel_galgje():
    woord = "draai"  # Het geheime woord
    geraden_letters = []
    pogingen_over = 5
    
    print("Je hebt besloten om het galgje-spel te spelen. Je hebt 5 pogingen om het woord te raden.")
    
    while pogingen_over > 0:
        weergave = ""
        for letter in woord:
            if letter in geraden_letters:
                weergave += letter
            else:
                weergave += "_"
        
        print(f"Weergave: {weergave}")
        print(f"Pogingen over: {pogingen_over}")
        
        letter = input("Kies een letter: ").lower()
        
        if letter in geraden_letters:
            print("Je hebt deze letter al geraden.")
        elif letter in woord:
            geraden_letters.append(letter)
            print("Goed geraden!")
            if all(letter in geraden_letters for letter in woord):
                print("Je hebt het woord geraden!")
                return True
        else:
            geraden_letters.append(letter)
            print("Foute letter.")
            pogingen_over -= 1
    
    print("Je hebt al je pogingen opgebruikt.")
    return False


def dobbelsteen_gooien():
    return random.randint(1, 6)


def blackjack_game ():
    alien_score = 0
    player_score = 0
    

    blackjack_game = True
    while blackjack_game:
        alien_worp = dobbelsteen_gooien()
        player_worp = dobbelsteen_gooien()

        print(f"De alien gooit de dobbelsteen, hij gooit {alien_worp}.")
        print(f"Jij besluit ook de dobbelsteen te gooien, je gooit {player_worp}.")

        alien_score += alien_worp
        player_score += player_worp

        print(f"Jouw score: {player_score}")
        print(f"Alien score: {alien_score}")

        if (player_score > 21 and alien_score < 21) or (player_score > 21 and alien_score < player_score) or alien_score == 21 or player_score > 21:
            bj_game_gewonnen = False
            blackjack_game = False

        elif (alien_score > 21 and player_score < 21) or (alien_score > 21 and player_score < alien_score) or player_score == 21 or alien_score > 21:
            bj_game_gewonnen = True
            blackjack_game = False
            

        if blackjack_game is True:
            choice = input("Wil je doorgaan met gooien (d) of stoppen (s)? ").lower()
            if choice == 's':
                blackjack_game = False
            elif choice == "d":
                blackjack_game = True
            else:
                print("Kies de juiste optie!")
    
    if bj_game_gewonnen is False:
        print("Alien: Helaas, geen prijs, geen feestelijk cadeau,")
        
        print("Maar vertrek niet met een zwaar gemoed, gauw.")
        
        print("Dank voor je deelname, je inzet was fijn,")
        
        print("Ooit zal er een beloning zijn.")
        return True

    elif bj_game_gewonnen is True:
        print("Gefeliciteerd! Je hebt gewonnen.")
        
        print("De alien verdwijnt en de deur gaat open.")
        
        print("In het gat zie je een stel werpsterren liggen.")
        
        print("Je besluit de werpsterren mee te nemen.")
        return False

def planet_travel():
    if (saturn_completion and venus_completion and mercury_completion and story_end) is True:
        global planeet_mercurius
        global planeet_venus
        global planeet_saturnus

        print("Naar welke planeet wil je?\n")
        if planeet_mercurius is True:
            planeet_venus = False
            planeet_saturnus = False
            print("-[A] Venus\n")
            print("-[B] Saturnus\n")
            print("-[C] Aarde")
            planeet_selectie = input(">> ").lower()

            if planeet_selectie == "venus" or planeet_selectie == "a" :
                planeet_venus = True

            elif planeet_selectie == "saturnus" or planeet_selectie == "b":
                planeet_saturnus= True

            elif planeet_selectie == "aarde" or planeet_selectie == "c":
                story_end = True

        elif planeet_venus is True:
            planeet_mercurius = False
            planeet_saturnus = False
            print("-[A] Mercurius\n")
            print("-[B] Saturnus\n")
            print("-[C] Aarde")
            planeet_selectie = input(">> ").lower()

            if planeet_selectie == "mercurius" or planeet_selectie == "a" :
                planeet_mercurius = True

            elif planeet_selectie == "saturnus" or planeet_selectie == "b":
                planeet_saturnus= True
            
            elif planeet_selectie == "aarde" or planeet_selectie == "c":
                story_end = True

        elif planeet_saturnus is True:
            planeet_mercurius = False
            planeet_venus = False
            print("-[A] Mercurius\n")
            print("-[B] Venus\n")
            print("-[C] Aarde")
            planeet_selectie = input(">> ").lower()

            if planeet_selectie == "mercurius" or planeet_selectie == "a" :
                planeet_mercurius = True

            elif planeet_selectie == "venus" or planeet_selectie == "b":
                planeet_venus = True

            elif planeet_selectie == "aarde" or planeet_selectie == "c":
                story_end = True

        elif story_end is True:
            planeet_mercurius = False
            planeet_saturnus = False 
            planeet_venus = False
            print("-[A] Mercurius\n")
            print("-[B] Venus\n")
            print("-[C] Saturnus\n")
            planeet_selectie = input(">> ").lower()

            if planeet_selectie == "mercurius" or planeet_selectie == "a" :
                planeet_mercurius = True

            elif planeet_selectie == "venus" or planeet_selectie == "b":
                planeet_venus = True
            
            elif planeet_selectie == "saturnus" or planeet_selectie == "c":
                planeet_saturnus = True


def endboss_battle():
    raadsels = ["Ik ben altijd vooruit te krijgen, maar nooit achteruit. Wat ben ik?",
        	    "Het is groen en het zit in een boom, maar je kunt het niet eten. Wat is het?",
                "Het is rond en rond, maar altijd recht vooruit. Wat is het?",
                "Ik ben groot als ik word geboren, maar ik word kleiner naarmate ik ouder word. Wat ben ik?",
                "Wat is altijd nat, zelfs als het niet regent?",
                "Het begint en heeft geen einde, en is overal aanwezig. Wat is het?",
                "Het wordt 's nachts wakker, slaapt overdag en vliegt. Wat is het?",
                "Wat begint en heeft geen einde, en is toch eindeloos?",
                "Je kunt me vastpakken, maar ik kan niet worden vastgehouden. Wat ben ik?",
                "Ik ben altijd in beweging, maar ik beweeg nooit. Wat ben ik?",
                "Het heeft een hart dat nooit slaat, het kan rondlopen zonder voeten en het kan nooit ouder worden. Wat is het?",
                "Ik kan vliegen zonder vleugels. Ik kan huilen zonder ogen. Waar ik heen ga, komt de duisternis. Wat ben ik?",
                "Ik ben te zien in de nacht, maar niet in de dag. Ik verstop me achter sterren, maar ben geen planeet. Wat ben ik?",
                "Ik heb steden, maar geen huizen. Ik heb bossen, maar geen bomen. Ik heb rivieren, maar geen water. Wat ben ik?",
                "Ik ben altijd nat, zelfs als het niet regent. Ik kom omhoog, maar kom nooit naar beneden. Wat ben ik?"]
    
    raadsel_antwoord = ["toekomst", "vogelhuis", "wiel", "kaars", "vis", "oceaan","vleermuis", "cirkel", "ademhaling", "tijd", "klok","wolk", "maan", "kaart", "fontein"]
    
    boss_HP = 50
    user_HP = 50
    x = 0

    while boss_HP > 0 and user_HP > 0 :
        time.sleep(2)
        clear_screen()
        print(f"BOSS HP: {boss_HP}")
        print(f"{speler_naam} HP: {user_HP}")
        
        print(raadsels[x])
        print("geef hier 1 woord als antwoord")
        
        user_input = input(">> ").lower()
        if user_input == raadsel_antwoord[x]:
            if dolk is True and werpsterren is True:
                boss_HP -=9
                print()
                print("9 DMG dealt to the boss!")

            elif dolk is True and werpsterren is False:
                boss_HP -=7
                print()
                print("7 DMG dealt to the boss!")

            elif dolk is False and werpsterren is True:
                boss_HP -=7
                print()
                print("7 DMG dealt to the boss!")

            elif dolk is False and werpsterren is False:
                boss_HP -=5
                print()
                print("5 DMG dealt to the boss!")
            
        elif user_input != raadsel_antwoord[x]:
            user_HP -= 5
            print("You took 5 DMG")

        x +=1

        if x == 15:
            x = 0

    if user_HP == 0:
        print("Je hebt verloren, probeer opnieuw.")
        return True

    elif boss_HP == 0:
        print(f"Na een intens gevecht met de eindbaas en het oplossen van een reeks raadsels, slaagt {speler_naam} erin om de eindbaas te verslaan.\n")
        
        print(f"Uitgeput en opgelucht kijken {speler_naam} en zijn medegevangene elkaar aan.\n")
        
        print("Deadalus: Je hebt gewonnen!\n")
        
        print("Dankzij jou zijn we vrij.\n")
        
        print("Ik ben Deadalus, en ik ben hier al een tijdje gevangen.\n")
        
        print("Ik ben heel blij dat je mijn bericht hebt ontvangen.\n")
        
        print("Gezamenlijk vliegen ze in het ruimteschip terug naar de aarde.\n")
        return False


# Het begin van de game
speler_naam = input("Vul je naam in: ").capitalize()

print(f"""In het jaar 2045 gaat {speler_naam} de ruimte in om informatie te verzamelen over ons sterrenstelsel nadat een buitenaards bericht is ontvangen met de boodschap: 
"6b 6f 6d 20 6e 61 61 72 20 6d 69 6a". Dit vertaald naar: Kom naar mij.\n""")
time.sleep(5)

print(f"""{speler_naam} wil achterhalen of er leven aanwezig is op de planeet van waar het bericht afkomstig is en van wie het is...
Maar {speler_naam} moet eerst weten van welke planeet het bericht verzonden is""")
time.sleep(5)

print(f"""{speler_naam} begint op aarde met het in elkaar zetten van zijn ruimteschip door op zoek te gaan naar de benodigde onderdelen.\n""")
time.sleep(5)

print(f"""Je staat in je lanceerbasis. Je moet vijf belangrijke onderdelen verzamelen voordat je de reis kan beginnen.\n""")
time.sleep(5)

print(f"""Kies een ruimte om te doorzoeken: 
      
-[A] Lunchzaal
      
-[B] Planetarium
      
-[C] Engineering room
      
-[D] Ruimteschip opslag
      
-[E] Kantoren
      
-[F] Uitkijktoren
      
-[G] Tuin\n""")

stuur = False
ladder = False
thrusters = False
spacesuit = False
stoel = False

##collectibles
kristallen = False
flesje = False
dolk = False
werpsterren = False

ruimtebasis_check = True
while ruimtebasis_check:
    ruimtebasis_keuze = input(">> ").lower()

    if ruimtebasis_keuze == "lunchzaal" or ruimtebasis_keuze == "a" and stuur == False:
        print("Je besluit de lunchzaal in te gaan en vindt: *Stuur*\n")
        stuur = True

    elif ruimtebasis_keuze == "lunchzaal" or ruimtebasis_keuze == "a" and stuur == True:
        print("Je besluit de lunchzaal in te gaan maar er valt niks meer te vinden! Kijk in een andere ruimte.\n")

    elif ruimtebasis_keuze == "planetarium" or ruimtebasis_keuze == 'b' and ladder == False:
        print("Je besluit de planetarium in te gaan en vindt: *Ladder*\n")
        ladder = True

    elif ruimtebasis_keuze == "planetarium" or ruimtebasis_keuze =='b' and ladder == True:
        print("Je besluit de planetarium in te gaan maar er valt niks meer te vinden! Kijk in een andere ruimte.\n")

    elif ruimtebasis_keuze == "engineering room" or ruimtebasis_keuze == 'c' and thrusters == False:
        print("Je besluit de engineering room in te gaan en vindt: *Thrusters*\n")
        thrusters = True

    elif ruimtebasis_keuze == "engineering room" or ruimtebasis_keuze == 'c' and thrusters == True:
        print("Je besluit de engineering room in te gaan maar er valt niks meer te vinden! Kijk in een andere ruimte.\n")

    elif ruimtebasis_keuze == "ruimteschip opslag" or ruimtebasis_keuze == 'd':
        print("Je besluit de ruimteschip opslag in te gaan maar er is niks te vinden. Kijk in een andere ruimte.\n")

    elif ruimtebasis_keuze == "kantoren" or ruimtebasis_keuze == 'e' and spacesuit == False:
        print("Je besluit de kantoren in te gaan en vindt: *Spacesuit*\n")
        spacesuit = True

    elif ruimtebasis_keuze == "kantoren" or ruimtebasis_keuze == 'e' and spacesuit == True:
        print("Je besluit de kantoren in te gaan maar er valt niks meer te vinden! Kijk in een andere ruimte.\n")

    elif ruimtebasis_keuze == "tuin" or ruimtebasis_keuze == 'g' and stoel == False:
        print("Je besluit de tuin in te gaan en vindt: *Stoel*\n")
        stoel = True

    elif ruimtebasis_keuze == "tuin" or ruimtebasis_keuze == 'g' and stoel == True:
        print("Je besluit de tuin in te gaan maar er valt niks meer te vinden! Kijk in een andere ruimte.\n")

    elif ruimtebasis_keuze == "uitkijktoren" or ruimtebasis_keuze == 'f':
        print("Je besluit de uitkijktoren in te gaan maar er is niks te vinden. Kijk in een andere ruimte.\n")

    else:
        print("Je kunt niet verder zonder alle onderdelen te vinden!\n")

    if (stuur and ladder and thrusters and spacesuit and stoel) == True:
        ruimtebasis_check = False
        print("Je hebt alle onderdelen gevonden!")
        time.sleep(2)
        print(
            "Het zal een paar tellen duren voordat het ruimteschip klaar is voor vertrek.\n")
        time.sleep(5)
        print(
            f"Het ruimteschip van {speler_naam} is nu volledig in elkaar gezet. Je begint jouw reis naar de planeet Mercurius\n")
        time.sleep(5)
        clear_screen()
####

# Voor planet travel en storyline dialogue
mercury_completion = False
venus_completion = False
saturn_completion = False
story_end = False

# planeten states, True runned het verhaal op dat planeet
planeet_mercurius = True
planeet_venus = True
planeet_saturnus = True

# backpack
spullen_in_backpack = []

alive = True  # Levend of dood systeem begint na intro
while alive:

    if water_counter == 0:
        water_visual_functie()
        time.sleep(2)
        print("Je hebt geen water meer over!!!")
        alive = timer_functie()
        time.sleep(2)
        print("Wil je doorgaan of opzoek gaan naar water?: \n")


    while planeet_mercurius:
        time.sleep(4)
        clear_screen()
        mercury_landing()

        controle_directie_mercurius_landing = True
        while controle_directie_mercurius_landing:
            clear_screen()
            print("Je pakt je kompas uit je tas en besluit: ")
            print("-[A] Noord\n")
            print("-[B] Oost\n")
            print("-[C] Zuid\n")
            print("-[D] West\n")
            directie_mercurius_landing = input(">> ").lower()

            if directie_mercurius_landing == "noord" or directie_mercurius_landing == "a":
                print("Je besluit noordwaarts te gaan, maar na enkele stappen merk je dat de grond steeds zachter wordt")
                time.sleep(4)
                print("Besluit je door te gaan of om te draaien en terug te keren.\n")
                time.sleep(4)
                print("-[A] Doorgaan") 
                print("-[B] Terugkeren")
                modderpoel_directie = input(">> ").lower()

                if modderpoel_directie == "doorgaan" or modderpoel_directie == "a":
                    print("Je kiest ervoor om door te gaan...")
                    time.sleep(3)
                    print("Je zit vast in de modder en kunt niet meer er uit komen")
                    time.sleep(3)
                    print("Je sterft..\n")
                    time.sleep(2)
                    print("Je respawned over 5 seconden")
                    time.sleep(5)
                    clear_screen()
                    
                elif modderpoel_directie == "terugkeren" or modderpoel_directie == "b":
                    print("Je kiest ervoor om terug te keren")
                    time.sleep(3)
                    clear_screen()
                    controle_directie_mercurius_landing = True

            elif directie_mercurius_landing == "oost" or directie_mercurius_landing == "b":
                clear_screen()
                print("Je kiest ervoor om oostwaarts te gaan, maar onderweg hoor je vreemde, zachte geluiden in de mist.")
                time.sleep(2)
                print("Nieuwsgierig besluit je de bron van het geluid te onderzoeken.")
                time.sleep(2)
                print("Na een tijdje vind je een kleine groep inheemse wezens die vreedzaam in de mist leven.")
                time.sleep(2)
                print("Ze blijken vriendelijk te zijn en wijzen je naar hun leider.\n")
                time.sleep(2)
                controle_directie_mercurius_landing = False

            elif directie_mercurius_landing == "zuid" or directie_mercurius_landing == "c":
                clear_screen()
                print("Je besluit zuidwaarts te gaan en komt uiteindelijk uit de mist op een open plek met glinsterende rotsen en kristallen.")
                time.sleep(2)
                print("Je verzamelt enkele van deze mineralen voor later gebruik en vervolgt dan je weg.")
                time.sleep(2)
                print("Terwijl je verder gaat, leidt een subtiele glinstering in de lucht je naar een buitenaardse wezen.\n")
                time.sleep(2)
                controle_directie_mercurius_landing = False
                kristallen = True
                print("+ Kristallen\n")
                spullen_in_backpack.append("Kristallen")

            elif directie_mercurius_landing == "west" or directie_mercurius_landing == "d":
                clear_screen()
                print("Je gaat westwaarts en merkt dat de mist zich verdikt en een zoete geur verspreidt.")
                time.sleep(2)
                print("Je besluit voorzichtig door te gaan en ontdekt uiteindelijk een gebied met prachtige, bioluminescente flora.")
                time.sleep(2)
                print("Je gaat verder en merkt een groep wezens op die lijken te communiceren via lichtsignalen.")
                time.sleep(2)
                print("Ze wijzen je naar hun opperhoofd waarmee je wel kan communiceren.\n")
                time.sleep(2)
                controle_directie_mercurius_landing = False
            
            else:
                print("Maak een keuze uit de volgende directies: ")
                controle_directie_mercurius_landing = True

        # Wezen approachen
        print("Je loopt richting het wezen en vraagt deze om hulp in je zoektocht.\n")
        time.sleep(6)
        print("Wezen: Hallo vreemdeling, wat brengt jou hier op onze planeet?\n")
        time.sleep(5)
        print(f"{speler_naam}: Ik ben op zoek naar de bron van het vreemde bericht dat ik heb ontvangen\n")
        time.sleep(5)
        print("Wezen: Dat was niet van mij, maar ik kan je helpen! Los dit raadsel op om verder te komen op je reis.\n")
        time.sleep(5)

        # Raadsel
        raadsel_mercurius_check = True
        while raadsel_mercurius_check:
            print("Mijn naam is die van de godin van de liefde, vol pracht en schoonheid.")
            time.sleep(2)
            print("Mijn oppervlak is heet, met wolken die mysterie verhullen.")
            time.sleep(2)
            print("Welke planeet ben ik? Raad maar, als je durft!\n")

            raadsel_mercurius_antwoord = input(">> ").lower()
            if raadsel_mercurius_antwoord == "venus":
                print("Wezen: Dat is het juiste antwoord! Daar moet je naartoe gaan!\n")
                time.sleep(2)
                print(f"{speler_naam}: Bedankt voor je hulp, nu weet ik hoe ik mijn reis moet voortzetten.\n")
                raadsel_mercurius_check = False

                mercury_completion = True
                planet_travel()
                planeet_mercurius = False
                time.sleep(4)

            else:
                print("Dat is niet het juist antwoord!")
                time.sleep(2)
                clear_screen()
        
        clear_screen()
        time.sleep(2)
        print("Je keert terug naar je ruimteschip om door te gaan met je reis.")
        time.sleep(2)
        print("Je lanceert! Dit kan enkele momenten duren...")


    while planeet_venus:
        time.sleep(4)
        clear_screen()
        venus_landing()

        keuze_rots_check = True
        keuze_plant_check = True
        keuze_water_check = True
      
        waterfles_meenemen = False
        kristallen_meenemen = False
        niks_meenemen = False

        controle_keuze_venus_landing = True
        while controle_keuze_venus_landing:
            print("Welke spullen besluit je mee te nemen kies uit: ")
            
            print("-[A] Waterfles (met een klein laagje water)")
            if kristallen == True:
                print("-[B] Kristallen")
                print("-[C] Niks")
            elif kristallen == False:
                print("-[B] Niks")


            keuze_venus_landing = input(">> ").lower()
            if keuze_venus_landing == "waterfles" or keuze_venus_landing == 'a':
                print("Je besluit om je waterfles mee te nemen\n")
                time.sleep(2)
                print("+ Waterfles\n")

                controle_keuze_venus_landing = False
                waterfles_meenemen = True

            elif kristallen == True and (keuze_venus_landing == "kristallen" or keuze_venus_landing == "b") :
                print("Je besluit om kristallen mee te nemen\n")
                time.sleep(2)
                print("+ Kristallen\n")

                controle_keuze_venus_landing = False
                kristallen_meenemen = True

            elif kristallen == True and (keuze_venus_landing == "niks" or keuze_venus_landing == "c") :
                print("Je besluit om niks mee te nemen")

                controle_keuze_venus_landing = False
                niks_meenemen = True

            elif kristallen == False and (keuze_venus_landing == "niks" or keuze_venus_landing == "b") :
                print("Je besluit om niks mee te nemen")

                controle_keuze_venus_landing = False
                niks_meenemen = True

            else:
                print("Kies één van de items!")
                controle_keuze_venus_landing = True
                time.sleep(2)
                clear_screen()

            controle_directie_venus_landing = True
            while controle_directie_venus_landing:
                time.sleep(3)
                print("Je hebt het ontzettend heet. Je kunt twee dingen doen: ")
                print("-[A] Op zoek naar schaduw.\n")
                print("-[B] Verder zoeken naar water.\n")

                directie_venus_landing = input(">> ").lower()
                if directie_venus_landing == "a":
                    print("Je besluit schaduw te zoeken om de ergste hitte te ontlopen.")
                    time.sleep(3)
                    print("Na enige tijd vind je een grote rotsformatie die verkoelende schaduw biedt.\n")
                    time.sleep(3)
                    
                    if waterfles_meenemen == True:
                        print("Hier kun je even op adem komen en jezelf hydrateren met je watervoorraad.")
                        time.sleep(3)
                        water_counter = 0
                        print("Je watervoorraad is nu zo goed als op")
                        time.sleep(3)
                        water_visual_functie()
                        time.sleep(3)
                        clear_screen()
                        print("Als je niet snel genoeg water vindt, zul je straks sterven!")
                        time.sleep(6)


                    elif niks_meenemen == True:
                        print("Hier kun je even op adem komen")
                        time.sleep(3)
                        print("Je begint heel veel dorst te krijgen dus je pakt je waterfles")
                        time.sleep(5)
                        print("Maar die heb je niet meegenomen!!!!")
                        time.sleep(5)
                        print("Je sterft van dehydration...")
                        time.sleep(5)
                        print("Je respawned over 5 seconden")
                        time.sleep(5)
                        clear_screen
                        niks_meenemen = False

                        controle_directie_venus_landing = False
                        controle_keuze_venus_landing = True

                elif directie_venus_landing == "b" and waterfles_meenemen == False:
                    print("Neem eerst je waterfles mee en zoek daarna verder!")
                    controle_directie_venus_landing = False
                    controle_keuze_venus_landing = True


                elif directie_venus_landing == "b" and waterfles_meenemen == True:
                    print("Je hebt dorst en bent vastbesloten om water te vinden.")
                    time.sleep(3)
                    print("Je gaat verder over de verzengende vlakten, op zoek naar tekenen van water.\n")
                    time.sleep(3)
                    print("Terwijl je loopt, merk je iets glinsterends op in de verte.")
                    time.sleep(3)
                    print("Je nadert de glinstering en ontdekt een ondergrondse waterbron, verstopt onder een rotsachtige overhang.")
                    time.sleep(3)
                    print("Je kunt je dorst lessen en watervoorraden aanvullen.")
                    water_counter = 20
                    time.sleep(3)
                    water_visual_functie()
                    time.sleep(6)
                    clear_screen()
                    print("Nu dat je watervoorraad is aangevuld besluit je even rustig om je heen te kijken")
                    controle_directie_venus_landing = False
                    controle_keuze_venus_landing = False
                    time.sleep(4)

                else:
                    print("Kies een juiste optie!")
                    time.sleep(3)
                    
        grot_keuze_check = True
        while grot_keuze_check:
            ("Waar wil je kijken?")
            if keuze_water_check is True:
                print("-[A] Het water.\n")
            if keuze_rots_check is True:
                print("-[B] De rotswand\n")
            if keuze_plant_check is True:
                print("-[C] De planten die over de vloer woekeren\n")
            print("-[D] Verlaat de grot")
            
            voortgang_grot = input(">> ").lower()

            if voortgang_grot == "a" and keuze_water_check is True:
                print("Als je het water goed bestudeerd zie je dat het een groenige kleur heeft,\nIn eerste instantie zie je niks maar als je goed kijkt zie je kleine glimmende dingen op de bodem van het water.\n")
                time.sleep(3)
                print("Het water leek inderdaad op het eerste gezicht kalm en rustig,\nmaar de groenige kleur en de glimmende voorwerpen op de bodem wekten je nieuwsgierigheid.\n")
                time.sleep(3)
                print("Je knielt voorzichtig neer aan de rand van het water en stak je hand uit om een van de glimmende objecten op te rapen.\n")
                time.sleep(3)
                print("Het voelde glad en koel aan in je hand. Het bleek een klein, glazen flesje te zijn met een kurken stop.\n")
                time.sleep(3)
                print("De ontdekking van het glazen flesje wekt je interesse.\n")
                time.sleep(3)
                print("Voorzichtig haal je de kurken stop eraf en bekijk je de inhoud. Binnenin vind je een stukje verweerd papier,\ndat eruitziet alsof het al eeuwenlang in het flesje heeft gezeten.\n")
                time.sleep(3)
                print("wat kies je?\n")
                time.sleep(3)
                print("-[A] Dit is vast niet bedoelt voor mij.\n")
                print("-[B] Wat is dit?\n")

                while keuze_water_check:
                    keuze_water = input(">> ").lower()
                    if keuze_water == "a":
                        print("Je keert terug..")
                        time.sleep(3)
                        clear_screen()
                        keuze_water_check = False
            
                    elif keuze_water == "b":
                        print("Op het papier staat een vreemde reeks tekens en symbolen, en het lijkt een soort boodschap te zijn.\n")
                        time.sleep(3)
                        print("Je haalt je notitieblok tevoorschijn en begint de tekens te noteren. \n")
                        time.sleep(3)
                        print("Het lijkt op een code of een cryptische boodschap, maar je hebt nog geen idee wat het betekent.\n")
                        time.sleep(3)
                        print("Je besluit het flesje en het stukje papier mee te nemen, want wie weet kan het je later nog van pas komen in je zoektocht naar de herkomst van het buitenaardse bericht.\n")
                        keuze_water_check = False
                        flesje = True
                        print("+ Flesje\n")
                        spullen_in_backpack.append("Flesje")
                        time.sleep(4)
                        clear_screen()
                    
                    
            elif voortgang_grot == "b" and keuze_rots_check is True:
                print("Je loopt richting de rotswand en ziet een aantal losliggende stenen")
                time.sleep(3)
                print("Als je deze rustig aan de kant duwt zie je een deur die duidelijk moet leiden naar een geheim compartiment. \n")
                time.sleep(3)
                print("Op de deur zie je: 5 streepjes en een aantal stenen letters erboven liggen. \n")
                time.sleep(3)
                print("-[A] Dit is niks voor mij.\n")
                print("-[B] Ik ga dit oplossen!\n")
                

                while keuze_rots_check:
                    keuze_rots = input(">> ").lower()
                    if keuze_rots == "a":
                        print("Je keert terug..")
                        keuze_rots_check = False
                        time.sleep(4)
                        clear_screen()

                    elif keuze_rots == "b":
                        if speel_galgje():
                            print("Er verschijnt een grote draaiknop, je draait deze om en de deur gaat met een luide knal open")
                            time.sleep(3)
                            print("In het midden van het vak zie je een met goud omhulde dolk liggen!\n")
                            time.sleep(3)
                            print("+ Gouden Dolk\n")
                            spullen_in_backpack.append("Gouden Dolk")

                        else:
                            print("Je hebt meer dan 5 fouten gemaakt en ziet langzaam de deur in de muur verdwijnen.")
                            time.sleep(4)
                        keuze_rots_check = False

                    elif keuze_rots == "b":
                        keuze_rots_check = False
                    
                    else: 
                        print("Kies een van deze opties!")
                        time.sleep(3)
                        
                

            elif voortgang_grot == "c" and keuze_plant_check is True:
                print("Je zet een stap richting de grote plantenberg.\n")
                time.sleep(3)
                print("Je duwt de planten aan de kant en ziet een grote plaat met een slot er aan.\n")
                time.sleep(3)
                print("Je bekijkt het slot uitvoerig maar je ziet helemaal niks.\n")
                time.sleep(3)
                print("-[A] Ik geef op ")
                print("-[B] Ik blijf nog zoeken  ")

                while keuze_plant_check:
                    keuze_plant = input(">> ").lower()
                    if keuze_plant == "a":
                        print("Je keert terug..")
                        keuze_plant_check = False

                    elif keuze_plant == "b":
                        print("Je duwt nog wat planten weg en ziet een dobbelsteen liggen.")
                        time.sleep(3)
                        print("Zodra je deze optilt verschijnt er een kleine blauwe alien.\n")
                        time.sleep(3)
                        print(f"Hij is niet groter dan {speler_naam} zijn onderarm")
                        time.sleep(3)
                        print("Alien: Probeer jij mijn kluis te kragen, let dan maar op. Degene die het verwegst zit van 21 bokt maar op.\n")
                        time.sleep(3)
                        print("Je duwt nog wat planten weg en ziet een dobbelsteen liggen.")
                        time.sleep(3)
                        print("Zodra je deze optilt verschijnt er een kleine blauwe alien.\n")
                        time.sleep(3)
                        clear_screen()
                        bj_game = blackjack_game()
                        
                        if bj_game is True:
                            time.sleep(2)
                            print("+ Werpsterren\n")
                            spullen_in_backpack.append("Werpsterren")
                            time.sleep(4)
                            clear_screen()
                            keuze_plant_check = False
                            
                        elif bj_game is False:
                            keuze_plant_check = False
                    
                    else: 
                        print("Kies een van deze opties!")
                        time.sleep(3)
                        clear_screen()

            elif voortgang_grot == "d":
                grot_keuze_check = False
                time.sleep(3)
                print("Je verlaat de grot en gaat verder op reis")

        time.sleep(3)        
        print("Wanneer je de grot verlaat zie je een bord.\n")
        time.sleep(3)
        print("Hierop staat:")
        time.sleep(3)
        print("VOLGENDE HALTE : SATURNUS")
        time.sleep(3)
        print(f"Na het vinden van water, is {speler_naam} klaar om zijn reis voort te zetten. \n")
        time.sleep(3)
        print("Je gaat opzoek naar de volgende planeet\n")
        time.sleep(5)
        clear_screen()
        venus_completion = True
        planet_travel()
        planeet_venus = False

        
    
    while planeet_saturnus:
        time.sleep(4)
        clear_screen()
        print("De vliegreis gaat helemaal prima totdat je opeens merkt dat het schip een kant op word getrokken, ohw nee je was totaal vergeten dat saturnus ringen heeft.\n")
        time.sleep(3)
        print("De meteorieten vliegen je om de oren. Je moet NU wat doen.\n")
        time.sleep(3)
        print("Je hebt de noodknop vergrendeld met een wachtwoord, maar die ben je vergeten.")
        time.sleep(3)
        print("Je hebt een blaadje met sommen die samen het wachtwoord geven.")
        time.sleep(6)
        print("Speler heeft 30 seconden om 5 sommen op te lossen en het wachtwoord in te vullen: ")
        time.sleep(6)
        sommen_oplossen_check = sommen_oplossen()

        if sommen_oplossen_check is True:
            print(f"{speler_naam} kijkt zijn ogen uit, de ringen zijn misschien heel eng maar de omgeving is buitenaards mooi, maar je beseft dat je hier niet alleen voor de schoonheid bent.\n")
            time.sleep(3)
            print("Je moet op zoek gaan naar aanwijzingen over de herkomst van het buitenaardse bericht en mogelijk contact leggen met de wezens die hier wonen.\n")
            time.sleep(3)
            print("Je ziet niks anders dan een paar bomen dus je besluit daar naartoe te lopen.\n")
            time.sleep(5)
            clear_screen()

           
            if flesje is True:
                print("Er hangt een een bord met wat lijkt op random tekens aan een van de bomen")
                time.sleep(3)
                print("Je herkent de letters ergens van...\n")
                time.sleep(5)
                print("Het perkament uit de fles natuurlijk!\n")
                time.sleep(3)
                print(f"{speler_naam} vist het snel uit zijn tas.\n")
                time.sleep(3)
                print("VERTALING: KOM DAT ZIEN KOM DAT ZIEN! HET JAARLIJKSE CIRCUS! LOOP RICHTING HET OOSTEN WAAR DE ZOM OPKOMT DAN ZIE JE ONS VANZELF.\n")
                time.sleep(3)
                print("Je besluit richting het oosten te blijven lopen en jahoor daar zie je een circus.\n")
                time.sleep(3)
                print("Je kijkt eerst even rond, je ziet hier en daar wat aliens lopen.\n")
                time.sleep(3)
                print("Maar deze aliens zien er helemaal niet vriendelijk uit, je blijft een beetje in de schaduw hangen.\n")
                time.sleep(3)
                print("Dan hoor je ineens van achteren: Probeer jij mijn circus attractie te redden jij pietleuterig mannetje.\n")
                time.sleep(3)
                print("2 aliens tillen je op en nemen je mee, een van de tenten in.")
                time.sleep(3)
                print(f"{speler_naam} word bij een ander persoon in de cel gegooid.")
                time.sleep(5)
                clear_screen()

            elif flesje is False:
                time.sleep(3)
                print("Je ziet een flyer aan de boom hangen maar je snapt er helemaal niks van je besluit het te negeren en richting het westen te lopen.\n")
                time.sleep(3)
                print("Je loopt het bos dieper in.\n")
                time.sleep(3)
                print("Je komt bij een beekje aan en besluit wat te drinken.\n")
                time.sleep(3)
                print("Ineens word alles zwart...")
                time.sleep(10)
                print("Je word wakker in een cel met een ander persoon er in.")
                time.sleep(5)
                clear_screen()
            
            print("Persoon: Je hebt mijn bericht gekregen! Wat mooi, alleen hebben ze ons nu alle 2 te pakken. ")
            time.sleep(3)
            print(f"{speler_naam}: We kunnen terug vechten, ik heb wapens.\n")
            time.sleep(3)
            print("Zodra de baas alleen is breken jij en je nieuwe vriend de cel open.\n")
            time.sleep(7)
            print("Hij is er! Dit is ons kans!")
            time.sleep(2)
            endboss_battle_check = True
            while endboss_battle_check:
                endboss_battle_check = endboss_battle()
                time.sleep(7)
                clear_screen()
            saturn_completion = True
            planet_travel()
            planeet_saturnus = False

        else:
            print("Je sterft...")
            planeet_saturnus = True


        #dit is ook voor planet travel dus niet weghalen, alles van het eind moet in deze while loop
    
    story_end = True
    while story_end:
          
        # Dit is voor planet travel en collectibles dus plaats de rest hierboven, dan komt dit als laatst
        print(spullen_in_backpack)
        if len(spullen_in_backpack) != 4:
            print("Er zijn nog collectibles die je niet hebt gevonden.")
            time.sleep(3)
            print("Wil je terugkeren en zoeken naar deze collectibles? ")
            time.sleep(3)
            print("-[A] Ja")
            print("-[B] Nee")
            time.sleep(2)
            planet_travel_check = True
            while planet_travel_check:
                planeet_travel_input = input(">> ").lower()
            
            if planeet_travel_input == "ja" or planeet_travel_input == "a":
                time.sleep(3)
                planet_travel()
                
            elif planeet_travel_input == "nee" or planeet_travel_input == "b":
                planet_travel_check = False 

        #dit is zodat loop niet oneindig lang doorgaat, kan later ergens anders staan
        story_end = False
