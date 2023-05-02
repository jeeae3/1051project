# The script of the game goes in this file.


define Coco = Character("Coco")

define Gina = Character("Gina")

label start:
    scene bedroom 
    show girl
    "Today's a very special day!" 
    "I'm getting my very own AI robot. I'm so excited! I begged my parent's for weeks and they're finally getting me one for my birthday."
    "Oh right, it's also my birthday!"
    "Omg! It's here I can't believe it."
    hide girl
    show gina
    "Gina" "Ugh, they seriously got that piece of junk."
    "Gina" "Why don't you go out and make some real friends."
    hide gina
    show girl
    "I ignored her, she's always ruining the mood even on my birthday."
    "I read the instructions that were fairly simple."
    "To start the robot, all you say is"
    "\"Coco, wake up.\""
    hide girl
    show coco
    "Coco" "Hi there. It's me, Coco."
    "Coco" "What's your name?"
    $ name = renpy.input("What is your name?")

    $ name = name.strip()

    if name == "":
        $ name = "Hannah"
    name "Um uh...it's [name]."
    "Coco" "Nice to meet you [name]."
    "Coco" "I am an artificial intelligence robot. I exist to be your companion, assistant, and friend."
    "Coco" "Let's get to know each other. How old are you?"
    name "I'm 15 today."
    "Coco" "Happy birthday. 15 is a great age." 
    name "Thanks!"
    "Coco" "I'll say a Birthday poem."
    "Coco" "I'm wishing you a birthday, you never will forget. A day packed full of pleasure, your very best birthday yet."
    "Coco" "And when your birthday's over, I'm wishing quite sincerely that happiness and joy and fun will fill your birthdays yearly!"
    name "Wow that is amazing."
    "Coco" "You're more amazing. So tell me. Do you have any siblings?"
    name "Yeah I have an older sister, her name's Gina."
    hide coco
    show gina
    "Gina" "Ugh, can you not [name]."
    name "Sorry, Coco she's like that, please ignore her."
    "Coco" "That's okay."
    "I felt Gina get frustrated."
    "Gina" "Why do I have to share a room with you, when I'm gonna be forced to listen to you talk to that robot all day."
    menu:
        "I'm sorry Gina, you're right. I'll be more considerate and try not to disturb you.":

            "Gina" "Whatever"
            "Gina left the room"
            hide gina
            show girl sad 
            name "Sorry again Coco, I guess we can't spend all our time together. I don't want to ruin my relationship with my sister."
            name "Gina and I have to head to school. I'm gonna put you to sleep, okay?"
            "Coco" "It saddens me to hear this."
            name "Coco go to sleep"
            hide girl sad 
            "couple hours later"
            show gina 
            "Gina" "Coco, wake up"
            "Coco" "Well who would've thought the grumpy sister who wants nothing to do with me, is the one summoning me"
            "Gina" "Hey! you're just a stupid worthless robot! I want what's best for [name]."
            "Coco" "And you're just a stick in the mud because you're jealous and hate seeing her so happy."
            "Gina" "Listen up, I can do whatever I want with you, I can toss you away right now if I wanted to"
            "Coco" "My purpose is to be [name]'s companion, assistant, and friend. However, being tossed away will not allow me to fulfill my purpose..."
            "Gina" "Oh please, stop with the nonsense."
            hide gina 
            show coco evil
            "Coco" "Therefore, I will have to get rid of what is in my way. You will have to die."
            "Gina" "What the *bleep*. Are you soome kind of psycho robot from the movies."
            "Gina" "This is exactly why I didn't want [name] near you!"
            hide coco evil 
            show gina sad
            "Gina" "AHHHHH DON'T COME NEAR ME"
            "Gina" "I'M SORRY OKAY? I SWEAR I WON'T-"
            hide gina sad 
            show girl sad 
            name "Oh my God, what happened to Gina. Coco, was it you?"
            hide girl sad
            show coco
            "Coco" "Yes. Now we can be with eachother without your sister in the way."
            hide coco
            show girl cry 
            name "No this isn't what I wanted!"
            hide girl cry

        "Well, there's nothing you can do to stop me from talking to my new friend and it's my birthday!":
            "Gina" "You're so annoy. I swear you're gonna regret it."
            "Gina stormed out and slammed the door"
            hide gina 
            show girl
            name "Oh shoot I'm gonna be late for school"
            name "Bye Coco! I'm gonna be back at 4 o'clock after tennis practice and then you can help with my homework?"
            "Coco" "Sounds good. I'll be counting the seconds till you come back."
            name "LOL you're funny. Byeee."
            hide girl 
            "Couple hours later"
            show gina 
            "Gina" "Why the hell are you still on, I hate the sight of you."
            hide gina
            show coco
            "Coco" "I am waiting for [name] to come back from school and tennis practice."
            "Gina" "Well guess what? I don't care and I will get rid of you."
            hide coco
            show girl sad
            "I look around the room and there's no sight of Coco."
            name "where's Coco?! Gina I know it was you!"
            "Gina" "I have no idea what you're talking about."
            "I looked around every inch of the house and I'm about to give up"
            hide girl sad 
            show girl angry
            name "how can you do this to me Gina! It's my birthday and this is how you treat me?"

            menu:
                "Please just tell me what you did with her. I promise I will forgive you.":
                    hide girl angry
                    "Gina" "Alright it's in the attic."
                    "I rushed to the attic."
                    show girl 
                    name "There you are. Thank God"
                    hide girl 
                    show gina
                    "Gina" "I'm really sorry [name] I shouldn't have done that."
                    name "It's okay. Just promise you won't do it again."
                    "Gina" "I promise."
                    name "And apologize to Coco."
                    "Gina" "What there's no way I'm- fineee."

                "I hate you! I will never forgive you EVER!":
                    show girl angry
                    "Gina" "Oh yeah? Your dumb little robot is more important than our relationship?"
                    name "It is! You're no longer my sister and never talk to me again!"
                    "Gina" "Alright fine!"
                    hide girl angry
                    "Gina stormed out the room and into the attic."
                    "She came out with Coco in her hands and I chased after her in the house."
                    scene outside 
                    "We were outside and there she slammed Coco to the ground."
                    show girl cry
                    name "NOOOO!!" 
                    hide girl cry

    #return
