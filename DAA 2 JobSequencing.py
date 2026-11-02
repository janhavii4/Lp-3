def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2],reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline

    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        for j in range(min(deadline, max_deadline) - 1, -1,-1):
            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break
    
    print("Selected Jobs:", [job for job in slots if job is not None])
    print("Maximum Profit:", total_profit)

jobs = [
    ("J1", 2 , 100),
    ("J2", 1 , 19),
    ("J3", 2 , 27),
    ("J4", 1 , 25),
    ("J5", 3 , 15)
]

job_sequencing(jobs)
