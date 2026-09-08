import random, asyncio, time

# using semaphore to use max 3 jobsa at once

semaphore = asyncio.Semaphore(3)

async def process_job(job_id):
    async with semaphore:
        print(f"Job {job_id} started. ")
        seconds = random.randint(1, 3)
        await asyncio.sleep(seconds)
        print(f"job {job_id} completed. ")
        return job_id

# asyncio.run(process_job(1))

# listing 20 jobs
jobs = list(range(1, 21))
async def run_jobs():
    start_time = time.time()
    results = await asyncio.gather(
        *(process_job(job) for job in jobs)
    )
    end_time = time.time()
    print(f"Total time: {end_time - start_time} seconds")
    return results

asyncio.run(run_jobs())
