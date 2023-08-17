qu = [ "who is the best singer in this world ", 
      "Who is the best betsman in this world",
      "Who is the best bowler of all time",
      "Who is the best All rounder after 2015",
      "what will come after 2023",
      "What will come after monday",
      "Who is the PM of india Now", 
      "What is my fav game ",
      "What is you current winning ",
      ]
options = ["Nushrat fateh ali khan ", "Arijeet singh ", "Tonny kakkar",  "None", 
            "Virat kohli","Smith", "Kane willimson", "None",
           "Dale Stayn", "Bumrah","Mitchel starck","None",
             "Sakib al hasan", "Glen maxwell", "ben stocks ","None",
             "tuesday", "sunday", "tuesday","friday","none",
             "Narendra Modi","Rahul Ghandhi",  "Yogi aaditynath","None",
               "Pubg", "free fire","cany crush","none",
               "500000","10000","20000","None",
           ]
levels = [ 1000, 2000, 5000, 10000, 20000, 30000, 50000, 100000, 500000]
ans = [ "Nushrat fateh ali khan ", "Virat kohli", "Dale Stayn", "ben stocks ","2024","tuesday","Narendra Modi","Pubg","500000"]

for i in range(0,len(qu)) :
     question = qu[i]
     for j in range(0 , len(levels)):
        print(f"Question for Rs {levels[j]}")
        print(question)
        for k in options:
          print(f"{options[i]}                            {options[i+1]} \n {options[i+2]}                                {options[i+3]}  ")

          reply = int (input("Enter your answer 1-4 :"))
          # for i in range(0,len(reply)):
          for i in range(0,len(options)):
            if reply == options[i]:
                print("Your answer is correct \n You won Rs{levels[i]}")

    

