start =
""You're stuck in Beijing, China as a "tourist". You have multiple options as to what to do.""


print(start)

#print("Enter your name here.")
user_input = input("Enter your name here.")

strawberry=input("Hi, you are now residing in Bejing China. The world seems like a problem free, happy place, but is it really? You must learn how to make a living for yourself in these new conditions. What do you want to do first? You have the options to walk around, work, or shop; type what ya wanna do.To choose an option, type those words verbatim")
if  strawberry == "walk around":
    print("You start to walk around the pathways around the seemingly cool streets, and a horrible smell invades your nostrils. Smog floats through the air. You are not used to the fumes. The builidings start fading from the smog,too. What do you do now? You have the options to wear  a mask,____________")
    blueberry = input("what do you want to do?")
    if blueberry== "wear a mask":
        print("So you decide to go find a mask, but your lungs are still suffering from the extreme pollution in Beijing. As a foreigner, what do you? You have the options to 'walk to the hospital', or 'keep walking and to hope to feel better'.You ______")
        orange= input("What do you want to do?")
        if orange == "walk to the hospital":
            print("The Chinese dcotors say you have to wait on the waitlist and wait before the wealthy politicans recieve new lungs even though your lungs are deteriorating from the pollutiion. He also won't treat you unless you bribe him with a couple million USD. What do you do now?! You have the options to wait, argue with the doctors, or leave China")
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
