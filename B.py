import bisect as bs
import random
def max_profit_Job(s_T, e_T, profit):   #create function to take 3 element (startTime, endTime, profit)
    N=len(s_T)        #measure length startTime must be the same for all
    jobs=list(zip(s_T, e_T, profit))     #Use zip to combine startTime, endTime, profit to sort them by start time
    jobs.sort() #Sort jobs by end time
    # two choices either first job+next job starting time/skip job
    def rec(i):
        if i==N :
            return 0 #If i==N we return to 0, that's why there is no profit
        j= bs.bisect_left(s_T,jobs[i][1]) #Walk step by step and skip if there is an overlap
        one = jobs[i][2] + rec(j) #Find the longest profit
        two = rec(i+1) #Find the longest profit
        return max(one , two)  # return max profit
    
    return rec(0)
startTime=[1,2,5,6]
endTime=[6,5,7,8]
profit =[6,5,5,3]
df= max_profit_Job(startTime,endTime,profit)
print(df)