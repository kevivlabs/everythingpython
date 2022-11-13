import csv
import time
from threading import Thread
timeout = False

start_time= time.time()
def quiz():
    global timeout

    question_count=0
    correct_count=0
    print("you have 10 seconds")
    while timeout == False: 
        with open ('problems.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if timeout== True:
               
                    print("total questions",question_count)
                    print("correctly answered",correct_count)
                    return 
                print(row[0])
                answer= input()
                question_count+=1
                if answer==row[-1]:
                    correct_count+=1
          
    
   
def countTime(seconds):
    global start_time
    global timeout
    while True:
        elapsed_time= time.time() - start_time
        if elapsed_time == seconds:
            timeout= True
            return print ("Timeout -- No fast enough")
            break
     
if __name__=='__main__':
    Thread(target=quiz).start()
    Thread(target=countTime(10)).start()
