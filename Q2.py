import bisect as bs
def max_profit(jops):   #create function to take 3 element (startTime, endTime, profit)
    jobs=sorted(jops,key =lambda x: x[1])   #Sort jobs by end time
    print(jobs)

    e_t=[e for s,e,p in jobs]  #specify end Time from jobs
    n=len(jobs)  #measure length startTime must be the same for all
    dp=[0]*n  
    dp[0]=jobs[0][2]
    for i in range(1,n):  #We will work to walk on every profit and start seeing the highest profit
        s=jobs[i][0]  #Determine the start
        e=jobs[i][1]  #Determine the end
        p=jobs[i][2]  #Determine the profit 
        dp[i]=dp[i-1]
        index =bs.bisect_right (e_t,s)-1 #ensuring no two jobs overlap -1
        dp[i]=max(dp[i],(dp[index] if index >= 0 else 0)+p) 
    return dp[-1]

jobs = [[1,6,6],[2,5,5],[5,7,5],[6,8,3]]
ob = max_profit(jobs)
print(ob)