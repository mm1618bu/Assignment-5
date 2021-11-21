from time import time;
import random;

#Class definition for StopWatch
class StopWatch:
  
   #Initializing private members
   def __init__(self):
       #Private Variable startTime
       self.__startTime = time();
      
   #Mutator method that sets start time
   def start(self):
       self.__startTime = time();
  
   #Mutator method that sets stop time  
   def stop(self):
       self.__endTime = time();
      
   #Accessor method that gets start time
   def getStartTime(self):
       return self.__startTime;
  
   #Accessor method that gets stop time  
   def getStopTime(self):
       return self.__endTime;
  
   #Accessor method that returns elapsed time
   def getElapsedTime(self):
       return self.getStopTime() - self.getStartTime();
      
#Non-Pure function
def calculateSum():
   #Instantiating StopWatch object
   watch = StopWatch();

   #Start stopwatch
   watch.start();
  
   #Performing sum for the values from 1 to 1000000
   sum = 0;
   for i in range(1,(1000000+1)):
       sum = sum + i;
  
   #Stop the stopwatch
   watch.stop();
  
   #Printing sum
   print("\n\n Sum : " + str(sum));
  
   #Printed Elapsed time
   print("\n\n Amount of time taken for adding numbers from 1 to 1000000: " + str(watch.getElapsedTime()));
   print("\n\n");
  
#Calling function
calculateSum();
