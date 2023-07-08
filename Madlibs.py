print(f"Welcome to the Mad libs Game !!\n")

print("""
The Para is 

    There is a new toy on the market that has everyone saying
    ____________(exclamation)! It is called the ____________(sound)
    ____________(adjective) ____________(noun) box, and will be in stores in
    ____________(a month). The ____________(sound)
    ____________(adjective) ____________(noun) box is a new gadget that
    lets you do just about anything!
    It ____________(verb)s, it ____________(verb)s, and it even serves
    ____________(a beverage)! It is easy to operate and requires no
    instructions!
    You can also have it custom made any size up to
    ____________(number) inches or a ____________ (color) to glow in the
    dark at no extra charge! The original product is pocket-sized and
    ____________ (color). There are ____________(number) jacks on the
    product for 6V DC power and for upgrades and add-ons. You can add
    head-phones, ____________(plural noun) monitors, ____________(plural
    noun), and more! It’s possible to use them all at the same time! 
      
FILL THE WORDS ACCORDINGLY

""")


exclamation1 = input("Enter an exclamation : ")
sound1 = input("Enter a sound : ")
adjective1 = input("Enter an adjective : ")
noun1 = input("Enter a noun : ")
month = input("Enter a month : ")
sound2 = input("Enter another sound : ")
adjective2 = input("Enter another adjective : ")
noun2 = input("Enter another noun : ")
verb1 = input("Enter a verb : ")
verb2 = input("Enter another verb : ")
beverage1 = input("Enter a beverage name : ")
number1 = input("enter a number : ")
number2 = input("enter another number : ")
color1 = input("enter a color : ")
color2 = input("enter another color : ")
plural_noun1 = input("enter a plural noun : ")
plural_noun2 = input("enter another plural noun : ")

print(f"""

Te Para you formed is :  
      
    There is a new toy on the market that has everyone saying
    {exclamation1}! It is called the {sound1} {adjective1} 
    {noun1} box, and will be in stores in {month}. The 
    {sound2} {adjective2} {noun2} box is a new gadget that
    lets you do just about anything! It {verb1}s, it {verb2}s,
    and it even serves {beverage1}! It is easy to operate and 
    requires no instructions! You can also have it custom made 
    any size up to {number1} inches or a {color1} to glow in the
    dark at no extra charge! The original product is pocket-sized
    and {color2}. There are {number2} jacks on the product for 
    6V DC power and for upgrades and add-ons. You can add 
    head-phones, {plural_noun1} monitors, {plural_noun2}, and more!
    It’s possible to use them all at the same time! 

THAKS FOR PLAYING THE GAME
    """)
