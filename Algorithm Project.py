#QA Function
def schedule_job(jobs) :
     
    #sorting the jobs by Profit
     jobs.sort(key=lambda x: x[2],reverse = True)
    # initialize schedule list for jobs done
     schedule = []
     # loop through the jobs
     for job in jobs:
      if len(schedule) < job[1]:
       schedule.append(job)
     return len(schedule), sum([job[2] for job in schedule])


#QA Test with randomly generated jobs 
def JobSequence():
 import random

 jobs = []
 for i in range(5):
    jobs.append({'id': i, 'deadline': random.randint(1, 10), 'profit': random.randint(10, 100)})

 jobs.sort(key=lambda x: x['profit'], reverse=True)
 print('Jobs : ',jobs)

 jobsDone = []
 time = 0

 for job in jobs:
    if time < job['deadline']:
        time += 1
        jobsDone.append(job)

 print('Jobs Done: ',jobsDone)

 print('Num of Jobs Done: ', len(jobsDone))
 print('Total Profit: ', sum(job['profit'] for job in jobsDone))


def main():
    
    # QA test with predefined fixed input
    Q1jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
    num_jobs,maxprofit = schedule_job(Q1jobs)
    print('QA Number of jobs done = ' , num_jobs,'\nMax Profit = ',maxprofit )

    # QA test with random jobs
    # JobSequence()



if __name__ == "__main__":
         main()