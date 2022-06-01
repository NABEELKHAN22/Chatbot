def main() :
     
     a=input("Enter your name \n")
     print ("HELLO !",a)
     j=input("Hope you are well , and doing good in your life  Yes/No? \n")
     if  j == "Yes" or j== "yes" or j== "YES" :
          print("nice to hear that")
     elif j =="no" or j=="NO" or j == "No" :
          print("do not worry")
     else :
          print("invalid choice ")
          
     print("1) CAN I HELP YOU \n2) End chat ")
     p=input(" ")
     if  p == "1" :
           print("tell me ur problem \n 1)Delivery related query \n 2)Order related query \n 3)Something else \n 4)For any other assitance")
     elif p =="2":
          print("bye bye , nice to talk to u . Kindly rate our converstaion ")
     else :
          print("invalid choice \n")
          print("1) CAN I HELP YOU \n2) End chat ")
     n=input(" ")
     if n== "1":
          print("Your delivery is in process , we are working hard to give you the best experience \n Kindly rate our coversation , restart the chat for more help")
     elif n =="2":
           print("This is the list of your orders , kindly select the specific order")
     elif n=="3":
          print("Please type your specific query")
          v=input(" ")
          print("Looking on your concern , please wait")
     elif n =="4":
          print("Kindly book a call from us , press 1 to book it")
          g=input("")
          if g=="1":
               print("Connecting you to the call, thanks for your patience")
          else :
               print("Type 1 to end chat")
               if n ==1:
                    print("bye bye , nice to talk to you")
               else :
                    print("invalid choice")
     else:
          print("invalid choice \n restarting the chat")
          main()
main()     


          


