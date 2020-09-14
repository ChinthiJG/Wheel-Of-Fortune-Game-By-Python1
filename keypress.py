from turtle import *
import random
import turtle
from string import ascii_uppercase
import os
import sys

screen = Screen()
screen.screensize(1900, 1000)
screen.bgcolor('#ebe9f2')
turtle.title("Wheel Of Fortune Game")
screen.setup(width = 900, height = 700)
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()
t7 = Turtle()


t5.penup()
t5.setpos(0,360)
t5.write("WHEEL OF FORTUNE GAME", align='center', font=("Arial", 26, "normal"))

t6.penup()
t6.setpos(-650,-60)
t6.write("Player Name", align='center', font=("Arial", 17, "normal"))

t6.penup()
t6.setpos(-450,-60)
t6.write("Player Score", align='center', font=("Arial", 17, "normal"))

working = False
diretoria=r"wordPhrases.txt"        #Name of the directory that file exists
global count,count1,totalAmount,money,constont,vowels,letter_guessed,player_list,name, play_Amount,k
global colors
constont = 'bcdfghjklmnpqrstvwxyz '      #constants in english language
vowels = 'aeiou '                        #vowels in english language
letter_guessed = []
player_list = []
play_Amount = [0,0,0]
guessed = False
totalAmount = 0
vowelCost = 250
count=0
count1=0
money=0




def wordlist():                         #Randomly select phrase from the text file
	ficheiro=open(diretoria, 'r')
	lst=ficheiro.readlines()
	ficheiro.close()
	return lst[random.randint(0,len(lst))]

def printWord():                        #print the word that is randomly selected
  global word
  word=wordlist().strip('\n').lower()
  #print(word)
  spaces(word)

def go_to(x, y,p):                      #Set the positions of spaces making in turtle screen
	#turtle.hideturtle()
	turtle.penup()
	turtle.goto(x,y)
	turtle.setheading(p)
	turtle.pendown()
  

def spaces(word):                       #set the spaces in turtle screen according to the randomly selected word 
	l=len(word)
	if l %2 !=0:
		go_to(-5-(l//2*20) - (l//2*10), 310, 0)
		for i in range(l):
			turtle.forward(20)
			turtle.penup()
			turtle.forward(10)
			turtle.pendown()
	else:
		go_to(-(l//2*20) - (l//2*10), 310, 0)
		for i in range(l):
			turtle.forward(20)
			turtle.penup()
			turtle.forward(10)
			turtle.pendown()

def getName():
        global count,name,player_list,play_Amount,totalAmount
        print("---------------------------------------------------------------")
        print("<<<<<<<<<<<<<<<<<<<<<<<< WELCOME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<<<<<<Wheel Of Fortune>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<Game>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("---------------------------------------------------------------")
        print("")
        for i in range(3):
                name = input("Please input "+str(i+1)+" player name >>>>>>>>>>")
                player_list.append(name)

              
FONT_SIZE = 15
STYLE = ('Arial', FONT_SIZE, 'normal')   
global j,k
k,j=0,0
def inputName():                        #Get the name of the player
        global count,name,player_list,play_Amount,totalAmount,j,k
        while j < 3:
              
                totalAmount = play_Amount[j]
                k=j
                print(" ")
                print('Ok ' + player_list[j] + '....Let us move to the game>>>>>')

                t3.penup()
                t4.penup()
                t3.setpos(-650,-100)
                t4.setpos(-450,-100)
                for i in player_list:

                  output =  i 
                  t3.write(output, font=STYLE)
                  t3.goto(-650,t3.ycor() - 50)
                  
                for m in play_Amount:
                  output1=m
                  t4.color(turtle.bgcolor())
                  t4.begin_fill()
                  t4.fd(100)
                  t4.setheading(90)
                  t4.fd(30)
                  t4.setheading(180)
                  t4.fd(110)
                  t4.setheading(270)
                  t4.fd(30)
                  t4.setheading(0)
                  t4.fd(10)
                  t4.end_fill()
                  t4.color("blue")
                  t4.write(output1,font=STYLE)
                  t4.goto(-450,t4.ycor() - 50)
                  
                  

                

                
                count=0
                print(" ")
                print('Now click the mouse button to rotate...')
                turtle.onscreenclick(clicked)
                j+=1
                if j==3:
                        j=0 
                break



  
def getMoney(x,y):                      #Get the value of the cursor that is stoped in the wheel
  global money
  if (x>65 and x<126) and (y>-243 and y < -218) or (0<x<65 and 240<y<250):
    money = 900
    #print("700")
  elif(125<x<176 and -215<y<-179) or (245<x<251 and -66<y<0) or (-65<x<0 and 241<y<250) or (-239<x<-217 and 64<y<125) or (-250<x<-241 and -65<y<0):
    money = 500
    #print("700")
  elif(178<x<218 and -179<y<-126):
    money = 350
    #print("700")
  elif(218<x<243 and -126<y<-66):
    money = 600
    #print("700")
  elif(242<x<251 and 0<y<65):
    money = 400
    #print("700")
  elif(218<x<242 and 65<y<124):
    money = 550
    #print("700")
  elif(178<x<218 and 125<y<177) or (-241<x<-217 and -124<y<-65):
    money = 800
    #print("700")
  elif(126<x<178 and 176<y<217) or (-217<x<-177 and 125<y<175):
    money = 300
    #print("700")
  elif(65<x<126 and 217<y<243) or (-177<x<-125 and -217<y<-177):
    money = 700
    #print("700")
  elif(-123<x<-65 and 216<y<240):
    money = 5000
    #print("700")
  elif(-250<x<-241 and 0<y<66):
    money = 450
    #print("700")
  elif(-65<x<0 and -252<y<-243):
    money = 650
    #print("700")


	
def point(word, char, i):               #print the correct guessing letters in the turtle screen
	go_to(-5-(len(word)//2*20) - (len(word)//2*10), 320, 0)
	turtle.penup()
	for j in range(i):
		turtle.forward(20)
		turtle.forward(10)
	turtle.forward(20)
	turtle.pendown()
	turtle.write(char, align='center', font=("Arial", 22, "normal"))

def play(word, out):                    #method of play the game
  global count,count1,money,totalAmount,constont,letter_guessed,play_Amount,player_list,name,j,k
  inputType = input("If you want to input constont >>> Enter c OR if you want to input vowel >>> Enter v--->")       #The input type should be 'c' or 'v'. 
  if ((inputType=='c') or (inputType=='v')):    #Check that the input is correct or incorrect
    if (inputType=='c'):
      ch=input("Please input a character >>>> ")     #Get the input character
      key=''
      if ch not in letter_guessed:              #Check that input character is in the letter guessed list. If not print a error.
        letter_guessed.append(ch)               #Append the character to the letter guessed list.
        if ch in constont:                      #Check the character is constont or not.
          if ch in word:
            count,count2=0,0
            for i in range(len(word)):          
              if ch==word[i]:
                count2+=1
                key+=ch
                point(word, ch, i)              #call the point method to print correct guessing letter in the turtle screen.
              else:
                key+=out[i]
            totalAmount += (money*count2)       #awarded the dollar value of the number multiplied by the number of occurrences of the consonant in the phrase
            play_Amount[(k)]=totalAmount
            print(" ")
            print('Your total amount is $' + str(totalAmount))
            print(" ")
            solve = input("Do you want to solve the puzzel? (y/n) ")    #If you want to solve the puzzle print 'y' or 'n'.
            if ((solve == 'y') or (solve == 'n')):                      
              if(solve=='y'):
                guess = input("Guess the word >>>>>>>>>>> ")
                if (guess == word):                             #check the guessing phrase is equal to the correct phrase.
                  count1=1
                  count=1
                  print(" ")
                  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<CONGRATULATIONS!!! you won the game>>>>>>>>>>>>>>>>>>>>>>>>>>")
                  sys.exit()
                else:
                  print("<<<<<<<< You lose the game!!! Next player to chance>>>>>>>>>>>>>>>")
                  print("Your amount is = $" + str(play_Amount[(k)]))       #print the amount of money that lossed player
                  inputName()
                  count=0
                  turtle.onscreenclick(clicked)
              else:
                count1=0
                print(" ")
                print("<<<<<<<<<<<<<<<<<<<< Continue game..... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            else:
              count1=0
              count=0
              print(" ")
              print("<<<<<<<<<<Please enter valid input!!!>>>>>>>>>>>>>")

            return key
          else:
            count1=1
            print(" ")
            print("<<<<<<<< You lose the game!!! Next player to chance>>>>>>>>>>>>>>>")
            print("Your amount is = $" + str(play_Amount[(k)]))
            inputName()
            count=0
            turtle.onscreenclick(clicked)
            return out
        else:
          count=0
          print(" ")
          print("<<<<<<<<<<<<<<< This is not a consonant. Please enter only consonants >>>>>>>>>>>>>>>>>>>>>")
      else:
        count=0
        print(" ")
        print("<<<<<<<<<<<<<<<<<<You have already input this character!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Click again.....>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    else:
      v = input("please input vowel---> ")  #If player want to input vowel firstly check If the player’s total is below $250 he cannot buy vowel.
      if totalAmount>250:
        key=''
        if v not in letter_guessed:         #check the vowel guessed before or not.
          letter_guessed.append(v)
          if v in vowels:                   #Check the character is constont or not.
            if v in word:                   #check that vowel is in the phrse.
              count,count3=0,0
              for i in range(len(word)):
                if v==word[i]:
                  count3+=1
                  key+=v
                  point(word, v, i)         #call the point method to print correct guessing letter in the turtle screen.
                else:
                  key+=out[i]
              print(count3)
              totalAmount -= (250*count3)   #$250 is deducted from the player’s total regardless of the number of occurrences of the vowel.
              print(" ")
              print('Your total amount is $' + str(totalAmount))
              solve = input("Do you want to solve the puzzel? (y/n) ")  ##If you want to solve the puzzle print 'y' or 'n'.
              if ((solve == 'y') or (solve == 'n')):
                if(solve=='y'):
                  guess = input("Guess the word")
                  if (guess == word):
                    count1=1
                    count=1
                    print(" ")
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<CONGRATULATIONS!!! you won the game>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    sys.exit()
                  else:
                    print(" ")
                    print("<<<<<<<< You lose the game!!! Next player to chance>>>>>>>>>>>>>>>")
                    print("Your amount is = $" + str(play_Amount[(k)]))     #print the amount of money that lossed player
                    inputName()
                    count=0
                    turtle.onscreenclick(clicked)

                else:
                  count1=0
                  print("<<<<<<<<<<<<<<<<<<<< Continue game..... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
              else:
                count1=0
                count=0
                print(" ")
                print("<<<<<<<<<<Please enter valid input!!!>>>>>>>>>>>>>")

              return key
            else:
              count1=1
              totalAmount -= 250
              print(" ")
              print("<<<<<<<< You lose the game!!! Next player to chance>>>>>>>>>>>>>>>")
              print("Your amount is = $" + str(play_Amount[(k)]))
              inputName()
              count=0
              turtle.onscreenclick(clicked)
              return out
          else:
            count=0
            count1=0
            print(" ")
            print("<<<<<<<<<<<<This is not a vowel. Please enter only vowels>>>>>>>>>>>>")
        else:
          count=0
          count1=0
          totalAmount -= 250
          print(" ")
          print("<<<<<<<<<<<<<<You have already input this vowel!!!>>>>>>>>>>>>>>>>>>>>>")
      else:
        count=0
        count1=0
        print(" ")
        print("<<<<<<<<<<<<<<<<Not enough amount to buy a vowel>>>>>>>>>>>>>>>>>>>>>>>>>>")
      

  else:
    count1=1
    print(" ")
    print("Please check your input!!!")
    play(word,out)


def draw_color_wheel():
  global colors
  center=(0,0)
  slice_angle = 360 / 24
  colors = ['cornflower blue','spring green','purple','pink','violet','forest green','magenta','dark orchid',
          'yellow','pale goldenrod','medium violet red','beige','medium blue','gray','alice blue','green yellow',
          'dark turquoise','light slate gray','gold','lime','teal','sky blue','dark orange','pale violet red']
  heading, position = 90, (0 + 250, 0)
  turtle.speed(100)
  ang,count=5,0
  for color in colors:
    list1 = ['$400','$550','$800','$300','$700','$900','$500','$5000','Bankrupt','$300','$500','$450','$500','$800','Lose a turn','$700','Free play','$650','Bankrupt','$900','$500','$350','$600','$500']
    turtle.color(color, color)
    turtle.penup()
    c = turtle.getcanvas()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(250, extent=slice_angle)
    heading, position = turtle.heading(), turtle.position()
    turtle.penup()
    item_id = c.create_text(0,3, text='                                                                   '+str(list1[count]), angle=ang, font=("Arial", 15, "normal"))
    turtle.goto(center)
    turtle.end_fill()
    ang+=360/24
    count+=1

def draw():
  global word,money,out,count1,play_Amount,player_list,name,j,k
  t1.setheading(90)                 #Set heading of the cursor to 90.
  t1.up()
  t1.setpos(252,-1) 
  t1.down()
  t1.speed('fastest')
  out = ''
  for extent in range(1):
    t1.circle(251,random.randint(10,500))
    x = t1.xcor()
    y = t1.ycor() 
    if(((x>65 and x<126) and (y>-243 and y < -218) or (0<x<65 and 240<y<250)) or ((125<x<176 and -215<y<-179) or (245<x<251 and -66<y<0) or (-65<x<0 and 241<y<250) or (-239<x<-217 and 64<y<125) or (-250<x<-241 and -65<y<0)) or (178<x<218 and -179<y<-126) or (218<x<243 and -126<y<-66) or (242<x<251 and 0<y<65) or (218<x<242 and 65<y<124) or ((178<x<218 and 125<y<177) or (-241<x<-217 and -124<y<-65)) or ((126<x<178 and 176<y<217) or (-217<x<-177 and 125<y<175)) or (65<x<126 and 217<y<243) or (-177<x<-125 and -217<y<-177) or (-123<x<-65 and 216<y<240) or (-250<x<-241 and 0<y<66) or (-65<x<0 and -252<y<-243)):
      print(" ")
      print("<<<You get a number!!!>>>")
      getMoney(x,y)
      for i in range(len(word)):
        out+='_'
      while out != word:
        print(out)
        out=play(word, out)
        if(count1==0):
          print("Click again!!!")
        break
      if out==word:
        print(" ")      
        print("Congratulations!!! You are won")
        sys.exit()


    elif((0<x<66 and -252<y<-243) or (-177<x<-124 and 175<y<216)):
      print(" ")
      print("<<<Sory!!! It is a bankrupt!!!>>>")
      totalAmount = 0
      play_Amount[(k)]=totalAmount
      print("<<<<<<<<<<<<<<<<<<<<<<<You loss!!! Next player to chance >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      print("Your amount is = $" + str(play_Amount[(k)]))     #print the amount of money that lossed player
      inputName()
      count=0
      turtle.onscreenclick(clicked)

    elif(-126<x<-65 and -243<y<-219):
      print(" ")
      print("<<<<<<<<<<<<<<<<<<<<<<<<<<Woow!!! You got a free play chance>>>>>>>>>>>>>>>>>>>>>>>>>>")
      for i in range(len(word)):
        out+='_'
      while out != word:
        print(out)
        out=play(word, out)
        if(count1==0):
          print("Click again!!!")
        break
      if out==word:
        print(" ")
        print("Congratulations!!! You are won")
        sys.exit()

    elif(-216<x<-177 and -178<y<-126):
      print(" ")  
      print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Sorry you lose a turn!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<You loss!!! Next player to chance >>>>>>>>>>>>>>>>>>>>>>>>>")
      print(" ")
      print("Your amount is = $" + str(play_Amount[(k)]))     #print the amount of money that lossed player
      inputName()
      count=0
      turtle.onscreenclick(clicked)
        
        

  working = False

def clicked(x,y):
    global working,count
    if count<1:
      count +=1
      if working == False: 
          draw()
draw_color_wheel()
getName()
inputName()
printWord()
turtle.onscreenclick(clicked)
turtle.mainloop()
