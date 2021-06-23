def walking_message():
    os.system("cls")
    print("""
    One 30 minute run is guaranteed to burn between 200-500 calories.\n" 
    "That's a fantastic step forwards to your weight loss goal.\n 
    "Or a guilt-free guilty pleasure later that day. 
      """)
      print("press SPACEBAR to continue")
      get_char.getch()
      op_3()
def hydration_message():
    os.system("cls")
    print("""
     Dehydration can have a noticeable effect if you lose as little as 2 per cent of your body's water content.\n" 
     So stay drinking water, especially during this hot summer weather. 
      """)
      print("press SPACEBAR to continue")
      get_char.getch()
      op_4()
def op_1():   
os.system("cls")
print("You have 2 minutes until lunch-break and want to get a head start on the changes you want to\n" 
"make on your new healthy lifestyle, However you have been working hard all morning and want to sneak\n" 
"a look of your social media on another tab, and just then you received an Email in your inbox\n" 
"which could be important, But your eyes have been straining at the screen for hours and deserve a rest\n" 
"What do you do next?")
time.sleep(1)
print("""
    \033[1;31;40mA.\033[1;37;40m Answer the incoming Email which has just pinged up your Inbox.
    \033[1;31;40mA.\033[1;37;40m Look away from your PC Screen and give your eyes some well needed rest.
    \033[1;31;40mA.\033[1;37;40m Click open a separate tab on your Google Chrome and check out your social media.
""") 
choice = input("what's your choice?")
if choice in answer A:
    op_2()
elif choice in answer B: 
    health_points = health_points + 1
    os.system("cls")
    print("\nwell done, you're one step closer to being healthier,")
    print("press SPACEBAR to continue")
    get char.getch()
    op_2()
elif choice in answer C:
    op_2()
def op_2():
    os.system("cls")
print("You leave the office for your 60 minute break and want to go to the park. You are motivated to\n" 
"live a more healthy work-life balance so you can put on your running shoes and go for a jog,\n" 
"but you feel a little lazy and want to get a taxi to the park but you also want to save money\n" 
"and a rentable electric scooter just outside of your office is half the price of an Uber \n"
"and is also a lot more fun. Now what will you do for your lunch break?\n" 
"What mode of transport will you take?")
time.sleep(1)
print("""
      \033[1;31;40mA.\033[1;37;40m Take UBER which will cost £5 pound, and is faster.
      \033[1;31;40mA.\033[1;37;40m Take the ELECTRIC SCOOTER which is more fun and costs £2.50.
      \033[1;31;40mA.\033[1;37;40m Take the RUNNING SHOES and start jogging which is healthier but is MORE harder and more tiring.
     """)    
choice = input("what's your choice?")
if choice in answer A:
    walking_message()
elif choice in answer B: 
    walking_message()
elif choice in answer C:
     health_points = health_points + 1
    os.system("cls")
    print("\nwell done, you're one step closer to being healthier,")
    walking_message()
    print("press SPACEBAR to continue")
    get char.getch()
def op_3():   
os.system("cls")
print("When you arrive at the park you feel great as the natural surroundings are beautiful and lush\n" 
"with greenery and you notice a gorgeous pond which reflects the glaring sun in the sky\n" 
"that makes the water sparkle and glitter. On the side of the pond,\n" 
"a mystic is selling NATURAL WATER in clear glass bottles.\n" 
"She is VIBING with MUSIC on her wooden rocking chair and she has a very alluring and mysterious presence.\n" 
"She comes up to you and offers you a glass bottle to purchase off her.\n" 
"On the left you see an ice-cream van which is selling beautiful ice cream and ice pop which you love?\n" 
"Do you buy her water or do you shun her, and buy ICE CREAM instead? What do you do next?")
time.sleep(1)
print("""
      \033[1;31;40mA.\033[1;37;40m To pay attention to the persuasive mystic & purchase her beverage. 
      \033[1;31;40mA.\033[1;37;40m To press on forward and pay the mystics water or ice cream van no mind.  
      \033[1;31;40mA.\033[1;37;40m Go to the ice cream van and buy your favorite ice cream.
  """)
choice = input("what's your choice?")
if choice in answer A:
    health_points = health_points + 1
    os.system("cls")
    print("\nwell done, you're one step closer to being healthier,")
    print("press SPACEBAR to continue")
    get char.getch()
elif choice in answer B: 
    hydration_message()
elif choice in answer C:
    hydration_message()