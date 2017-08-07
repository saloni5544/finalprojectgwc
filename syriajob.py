start="..."
print("Don't forget to type your responses in all lowercase letters! ")
initialinput = input("In this game you will live in a country and face their everyday troubles. You may go to either Syria, New Orleans, Liberia, Chicago or China. ")

if initialinput == "China":
    print("You are stuck in Beijing, China as a tourist. You have multiple options as to what to do. ")
    strawberry=input("Hi, you are now residing in Bejing China. The world seems like a problem free, happy place, but is it really? You must learn how to make a living for yourself in these new conditions. What do you want to do first? You have the options to walk around, work, or shop; type what ya wanna do.To choose an option, type those words verbatim. ")
    if  strawberry == "walk around":
        print("You start to walk around the pathways around the seemingly cool streets, and a horrible smell invades your nostrils. Smog floats through the air. You are not used to the fumes. The builidings start fading from the smog,too. What do you do now? You have the options to wear  a mask. ")
        blueberry = input("what do you want to do?")
        if blueberry== "wear a mask":
            print("So you decide to go find a mask, but your lungs are still suffering from the extreme pollution in Beijing. As a foreigner, what do you? You have the options to 'walk to the hospital', or 'keep walking and to hope to feel better'. ")
            orange= input("What do you want to do?")
            if orange == "walk to the hospital":
                print("The Chinese dcotors say you have to wait on the waitlist and wait before the wealthy politicans recieve new lungs even though your lungs are deteriorating from the pollution. He also won't treat you unless you bribe him with a couple million USD. What do you do now?! You have the options to wait, argue with the doctors, or leave China")
                kiwi = input("what do you do now?")
                if kiwi=="wait":
                    print("Due to the abundant  pollution, your lungs start failing and you die. Coupled with the extreme corruption in China, you were unable to find a cure in the right amount of time. ")
         #exit and lead to home page with fundraising options for just this
                if kiwi=="leave china":
                    print("Your lungs couldn't survive in time. Your VISA is not approved in time before your lungs survive. Due to the abundant  pollution, your lungs start failing and you die. Coupled with the extreme corruption in China, you were unable to find a cure in the right amount of time")
             #exit and lead to home page with fundraising options for just this
                if kiwi=="argue with the doctors":
                    print("After arguing with the doctors, you are thrown into jail, and your prisonmate is a murderer who gets released after a day because he bribes the police official with a couple billion dollars.You're left to rot in prison alone because the government thinks you're a foreign threat to China now. In order to escape this hell-hole, you have to run away from the police officers in this upcoming game. Click the button to play the game.")
    #lLEAD TO BUTTON THAT LEADS TO GAME TO KILL POLICE officers
    #if you win, you survived china and leads to fundraising page
    # if you lose, you didn't survive and still leads to fundraising page


if initialinput == "Syria":
    syriainput = input("Hi, you have been dropped in Aleppo, Syria as a tourist. Your goal is to live a life that resembles that of a Syrian's as closely as possible. You have multiple options as to what to do. You can either find a job or go to school as a student. To choose an option, type one of those choices verbatim")
    if  syriainput == "find a job":
        print("You now have the option to find a job in  business or farming/manual labor.")
        blueberry = input("What do you want to do?")
        if blueberry=="farming/manual labor":
            print("You get sick from a lack of pay and resources like food and water, so you have to go to the hospital and die because the hospital doesn't treat you due to corruption. Syria was too rough for you. ")
            print("The End.")

    if blueberry== "business":
        print("So you decide to )open a business, but due to fighting against ISIS and a lack of infratstructure, there are not enough resources to start your business. There's also no reliable Syrian corporation to trust to start your business because you find out there are political monopoly ties with every business. So, now what do you do? You can wait or go fight with the government for not helping you pursue your dreams. Choose an option! ")
        orange= input("What do you want to do?")
        if orange == "go fight with the government for not helping you pursue your dreams":
            print("The Syrian government is extremely upset at you for not  being loyal, so they throw you in prison and severely abuse you and try to kill you with chemical weapons. They also find out you're not a Sunni muslim- the ruling religion of Syria; you're at the brink of life and death at this point. The only option you have is  to fight with the officials holding you captive. If you lose the game, you die, if you survive, you win. ")
#ADD GAME
        if orange ==  "wait":
            print ("You're about to die of starvation from being broke, so what do you do? You have the option  to wait more or join a seemingly succesful Syrian business. ")
        cherry= input("What do u do?")
        if cherry=="wait more":
            print("Your blood pressure falls incredibly and you become malnourished, and with no reliable hospitals, you die. ")
            print("The End.")
        if cherry=="join a seemingly sucesful Syrian company":
            print("Since the  business is actually succesful, the company gets shut down by Assad's regime and thet money is in his control, so you're left pennyless and jobless again. NOW what do you do? The only  job you can get is to work for a trading company or fight with the government. ")
        peach= input("what do u doo?")
        if peach=="fight with the government":
            print("You dig deeper in the problems of Syria and find out about the government's complete lack of structure and with your ties to American Media, you report it to them. However, the Syrian government finds out and throws you in prison and attempts  to murder you. Play the game to win or die. ")
#ADD THE GAME!!!!!!!
        if peach== "work for a trading company":
                print("You try to invest in trading in foreign investments, but no foreign country wants to invest with Syria because of the political situation. How sad. Now what do you do? You can either wait or join in field labor. ")
        lychee=input("what do you doooooo?")
        if lychee=="wait":
            print("You get no revenue and therefore are more malnourished and broke because the government gives you no benefits; you die of malnourishment. ")
            print("The End.")
        if lychee=="join in field labor":
            print("SO.. you decide to do the backaching labor in the fields. Well, event though you're sweating your back off to earn less than a penny due to corruption, you still don't  make enough to nourish yourself because the inflation is so high. ALSO, as you were working in the fields, ISIS took over the land and decapitated you for not being a Sunni Muslim. ")
            print("The End.")

    if syriainput == "go to school":
        print("You choose to go to high school and walk to school. When you get to school and enter class there is suddenly a large booming sound. The building shakes and the ceiling colapses in. ")
        schoolvar = input("As the ceiling falls down a piece of rubble hits your hand and gives you a large cut. You can either go to the Nurse or walk back Home. ")
        if schoolvar == "nurse":
            print("As you make your way to the Nurse you see a group of other stundents crowded there as well. Because of insuffiecient supplies few people recive bandages and help. ")
            print("You die of combined blood loss and infection. ")
            print("The End. ")
        if schoolvar == "home":
            print("Walking outside of the school you see cars in relatin to the Taliban members that control your city. All of a sudden a chemical weapon is released and you die. ")
            print("The End. ")

if initialinput == "Liberia":
    liberiainput = input("You begin in Monrovia, Liberia. It is a hot day out today at over 80 degrees. Today you can choose to go to School or Work to help out your family. ")
    if liberiainput == "work":
        workinput = input("Do you want to get a Labor job or Formal employment? ")
        if workinput == "formal":
            print("You go to look for Formal employment at an office, but they reluctanly tell you that there are no open positions. You are forced to go into a Labor job instead. ")
            workinput = "labor"
        if workinput == "labor":
            laborinput = input("As you search for a labor job you find three choices, one in Timber, another in Iron ore with the last in Rubber. Which would you like to work in? ")
            if laborinput == "timber":
                print("You begin your job at a small Timber mill, you work long hard hours and are exhausted. One day at the mill you fall on one of the saws and are gravelly injured. You do not survive and die later that day. ")
                print("The End. ")
            if laborinput == "iron":
                print("After starting you job at the Iron mine you work, seemingly without end, in the dark caves. One day after you finished working you go to leave the cave when one of your coworkers stabs you with their pick. The injury leads to your eventual death. ")
                print("The End. ")
            if laborinput == "rubber":
                print("When you start working you realize the job is not for a clumbsy person like you. After work one day you trip over a rock and fall into a vat of boiling hot rubber and melt. ")
                print("The End. ")
    if liberiainput == "school":
        print("At school you get recruited by the government to fight in your countries civil war as a child soldier. ")
        warinput = input("Now you have a choice, do you stay at Home to help fight the war by getting a government job for the rest of your life or go and Fight for your country. ")
        if warinput == "home":
            print("By deciding to stay home you sentenced yourself to a life of labor and died only after 50 years of working. ")
            print("The End. ")
        if warinput == "fight":
            print("After one day out on the field you are killed by a sniper on the opposing side. ")
            print("The End. ")

if initialinput == "Chicago":
    chiinput = input("It is a school day, how would you like to get to school? You can Walk, or take the Train. ")
    if chiinput == "train":
        print("You begin in the south side of Chicago on the CTA, this twenty minute ride is how you get to school everyday. ")
        traininput = input("On the CTA you get bored do you Listen to music at a low volume or go to Sleep? ")
        if traininput == "listen":
            print("As you listen to your music you see your stop to get off and meet up with friends! You have a great time walking to school together. ")
            print("The End. ")
        if traininput == "sleep":
            print("After falling asleep on the train you wake up only to realize you missed your stop. When you get off to transfer and go back you see a man creeping up to you. You get mugged and die. ")
            print("The End. ")
    if chiinput == "walk":
        reaction = input("As you walked to school a police car stopped you and got profiled for your skin color. How do you react, Calm or Angry that they would assume that you were up to no good? ")
        if reaction == "calm":
            print("You reacted calmly and stayed collected, the police left you alone and you were able to continue your walk to school peacefully. ")
        if reaction == "angry":
            print("The police took your angry response to their profiling as an act of aggression and you are forced to go to Juvie. ")
            print("The End. ")

if initialinput == "New Orleans":
    floodinput = input("You are walking from your grandmother's house when you receive a notification of a flash flood warning in your area. You have the options to Leave the city or go Home. What do you do? ")
    if floodinput == "leave":
        directioninput = input("You get in your car to prepare to leave the city and have the options to keep going Straight or Swerve to try to avoid a pothole. ")
        if directioninput == "straight":
            print("You return your house safely and make preparations to prevent water entering your house. ")
            print("The End.")
        elif directioninput == "swerve":
            print("You car enters the pothole, and it breaks down. You get swept away in the flood and are lost forever. ")
            print("The End.")
    if floodinput == "home":
        litterinput = input("You continue your route home and you see liter. Are you going to Pick It Up and waste a little time or Leave It on the ground. ")
        if litterinput == "pick it up":
            print("You find supplies for the flood among the rubble and continue home safely and survive the flood. ")
            print("The End.")
        if litterinput == "leave it":
            print("You suddenly are stopped by a sinkhole and are slowly being pulled down. You meet your immediate death. ")
            print("The End.")

input("Press enter to exit")
