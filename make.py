import pandas as pd

# List of tweets copied from your provided output
tweets = [
    "🧑🏽‍🍳 4K from Trey is CRAZY!!!!! Congrats my brother!! That’s 🔥🔥🔥🔥🔥🔥🔥🔥 @StephenCurry30",
    "RT @LJFamFoundation: Akron! March is officially here which means it’s time to save the date for our favorite day of the year... #330Day! 👑…",
    "The kid from AKRON 🤴🏾",
    "Yessir!!! Congrats Cam 🙌🏾🙌🏾🙌🏾🙌🏾",
    "Prayers sent up to Ky 🧙🏾🤞🏾!!!  🙏🏾🙏🏾🙏🏾",
    "Nice linking up with you again @notthefakeSVP! Always a pleasure 🙏🏾🤝🏾🫡",
    "Exactly made my point but anyways.  Happy this convo has started. It ain’t  about ‘face of the game” and it ain't about one person or one show, it's about the culture of basketball,, the most beautiful game in the world. Our game has never been better. Incredible young stars from",
    "THANK YOU GUYS FOR HAVING ME ON!! YOU’RE THE NOW AND FUTURE!!! 🙏🏾🙏🏾🙏🏾🙏🏾🙏🏾🙏🏾🙌🏾🙌🏾🙌🏾🙌🏾🫡",
    "I JUST WANNA LOVE YOU BABY!!!! Yayayaaaaaaaaa!!! 😁🕺🏾👑 https://t.co/nHPeL5AgsA",
    "THE GOAT FAMILY OF COMEDY MAN!!!! LOVE THIS SHIT RIGHT HERE!!! 🫡 to The WAYANS",
    "Earned 2 Not Given! Gotta give him credit though! 🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣. 💩 💩 💩 💩 💩",
    "WELL DESERVING MY BROTHER!!!!! SO DAMN HAPPY AND PROUD OF YOU CHAMP!! 🙏🏾💪🏾🫡",
    "😤😤😤 @beatsbydre",
    "Yo @tacobell!! I put myself in your #ad to show how big a fan I am. 😁🌮👑 #ReleaseTheLeBronCut https://t.co/FqF18uK2AI",
    "HUBIE BROWN THE 🐐!!!!!!! 🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🫡",
    "Biggest game of the year and @KevinHart4real is locked in building his @DKSportsbook parlay! 💪🏾🏈 Great offers await with promo code LEBRON. 🔥👑#DKPartner https://t.co/DAxPJbiGi5",
    "AYYYYYYYEEEEEEE!!! WELCOME BACK RANDY!!! 🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾 @RandyMoss 🙏🏾🤎🫡",
    "#YNWA 😉👑",
    "This The Weeknd album \"Hurry Up Tomorrow\" so 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 Abel never disappoints! 🫡",
    "You a fkn lie!!! 🤥🤡",
    "Keep going Maximus!! Work work work! Happiness and work is all that matters. 🤴🏾",
    "I don’t mind it one bit Coach Day! Earned Not Given! 🙏🏾",
    "♾️ GRATEFUL OF YOU KID!! 🤴🏾🤎",
    "🐐!!!!!! TOO DAMN GOOD! 💐💐💐💐🫡",
    "MY BROTHER’S KEEPER!!! 💪🏾🙏🏾👑 https://t.co/UiVPhtmmEW",
    "🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🤴🏾",
    "So proud of you Maximus!!! I literally just shed a tear! PROUD POPS!!",
    "Bryce James going crazy in the Hoophall Classic right now! Flame 🔥 thrower",
    "👏🏾👏🏾👏🏾👏🏾👏🏾👏🏾",
    "Deep breaths @KevinHart4real 🤣🤣 Good luck on those parlays this weekend!! #DKPartner",
    "👑 HENRY!!! @KingHenry_2 🫡",
    "I pray this nightmare ends soon! 🙏🏾🙏🏾🙏🏾🤞🏾🤞🏾🤞🏾🤞🏾. So many prayers",
    "JUST LIKE THAT!!!! Right back at cha!! @OhioStateFB  O-H!! 🗣️🗣️",
    "🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾 College hoops ain’t the same w/o Dicky V calling them!",
    "Praying for everyone in Southern California!! ! 🙏🏾🙏🏾🙏🏾🙏🏾",
    "So damn 🔥🔥🔥🔥🔥🔥. Super congrats my brother! Too TOUGH!! @MikeEvans13_ 🫡",
    "DraftKings has got all the sports action and responsible gaming tools you need for the new year. The crown is yours! 🫡👑 @DraftKings #DKPartner https://t.co/5vNypkS2ij",
    "🤦🏾‍♂️ @tacobell is gonna regret this #ad https://t.co/l7KrQzcRyb",
    "Just got done playing “ricankilla722” randomly on Madden. Got on the headset. Good game and convo bro! Some good laughs too! lol. 🫡",
    "Not having Xmas day unis anymore really sucks! That was a great feeling walking into the locker room and seeing those. It was literally like receiving a 🎁! Whomp whomp! 🤷🏾‍♂️",
    "Slipsmas is here! Want to win a $500 bonus bet from DraftKings? 🏈🎁  \nPlace your bet, post it on X using #Slipsmas and follow @DKSportsbook for a shot. Happy holidays!! 😃#DKPartner https://t.co/5d8AQqfQjn",
    "SAQUON!!!! ⚡️⚡️⚡️",
    "This went so CRAZY!!!!!! Jetts ✈️ to DOPE! 🫡 Young 👑",
    "Congrats Arianna!!! Continue inspiring others!! 👏🏾👏🏾👏🏾👑❤️",
    "And with that said I’ll holla at y’all! Getting off social media for the time being. Y’all take care ✌🏾👑",
    "AMEN!! @richkleiman 🫡 https://t.co/OZr9e1CVbY",
    "Proud! 🙏🏾👑 @mavcarter @benwinston @makespringhill @uninterrupted @Fulwell73\n \nLET’S GO!!!! 🗣️🗣️🗣️🗣️",
    "I don’t hear non of those @CUBuffsFootball @DeionSanders HATERS being up front and loud! They’re in hiding 🫣 now! 🤣🤣🤣🤣🤣🤣🤣. Coach Prime said “We Coming”. Well it’s “We Here” now. Love what’s going on there in Boulder. 🦬🫡",
    "Just woke up from having a dream I was playing for Duke for Coach K inside Cameron Indoor Stadium! It was INSANE in there. Told Coach K it was an honor to suit up for him and he said the same thing back to me. He’s such a LEGEND! Then…..",
    "WOW!!!!!! MATTHEW STAFFORD A BEAST!!! What a win by the @RamsNFL on the road",
    "CONGRATULATIONS VINSANITY!!!! @mrvincecarter15 🫡. DOPE!! ♾️ IMMORTALIZED IN THE 6!!!",
    "What are we even talking about here?? When I think about my kids and my family and how they will grow up, the choice is clear to me. VOTE KAMALA HARRIS!!! https://t.co/tYYlTmQS6e",
    "Athletes get it. 👑🔥 @beatsbydre #beatspartner https://t.co/cOTPLpw5BA"
]

# Deduplicate tweets
unique_tweets = list(dict.fromkeys(tweets))

# Save to CSV
import pandas as pd

df = pd.DataFrame(unique_tweets, columns=['Tweet'])
csv_path = '/mnt/data/.csv'
df.to_csv(csv_path, index=False)

csv_path
