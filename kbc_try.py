# Qu. Create a program for displaying questions to the user like KBC
#     Use list data type to store the question and their correct answer.
#      Display the final amount the person is taking home after playing the game .

qu = [ "who is the best singer in this world ","Nushrat fateh ali khan ", "Arijeet singh ", "Tonny kakkar",  "None",4 ,
      ["Who is the best betsman in this world", "Virat kohli","Smith", "Kane willimson", "None",4],
      ["Who is the best bowler of all time", "Dale Stayn", "Bumrah","Mitchel starck","None",4],
      ["Who is the best All rounder after 2015", "Sakib al hasan", "Glen maxwell", "ben stocks ","None",4],
      ["what will come after 2023", "2024", "2025","2026","none",4],
      ["What will come after monday","tuesday", "sunday", "tuesday","friday","none",4],
      ["Who is the PM of india Now", "Narendra Modi","Rahul Ghandhi",  "Yogi aaditynath","None", 4],
      ["What is my fav game ", "Pubg", "free fire","cany crush","none",4],
      ["What is you current winning ","50000","10000","20000","None",4],
      
      ]

levels = [ 1000 , 2000 , 5000 , 10000 , 20000 , 50000 , 100000, 200000 , 500000 ]

for i in range (0, len(qu),5) :
    question = qu[i]
    print(f"Question for Rupees {levels[i]}")
    print(qu[i])
    print(f"a.{qu[1]}                   b.{qu[2]}/n c.{qu[3]}                        d.{qu[4]}")

    reply = int(input("Enter your ans 1-4"))
    if reply == i+1:
        print(f"your ans is correct . you won Rs {levels[i]}")
    i = i + 6