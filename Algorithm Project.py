
#QA Function
def schedule_job(jobs) :
    #sorting the jobs by Profit
     jobs.sort(key=lambda x: x[2],reverse = True)
    # initialize variables
     current_time = 0
     num_jobs_done = 0
     maxprofit = 0
     # loop through the jobs
     for i in jobs :
        # if Current time unit is less than the deadline of the job 
        if current_time < i[1] :
            current_time+=1
            num_jobs_done+=1
            maxprofit += i[2]

     return num_jobs_done,maxprofit



def main():
    
    #QA
    Q1jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
    num_jobs_done,maxprofit = schedule_job(Q1jobs)
    print('QA Number of jobs done = ' , num_jobs_done,'\nMax Profit = ',maxprofit )



if __name__ == "__main__":
         main()