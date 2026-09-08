import asyncio
import time

async def fetch_user():
    await asyncio.sleep(2)
    return {
        "id": 101,
        "name": "Poku"
    }

async def fetch_orders():
    await asyncio.sleep(3)
    return [
        {"id": 1, "amount": 1200},
        {"id": 2, "amount": 800}
    ]

async def fetch_notifications():
    await asyncio.sleep(1)
    return [
        "Payment received",
        "New login detected"
    ]


# using gather to run all async ops together    
async def dashboard():
    # measuring th starting time
    start_time = time.time()
    
    res = await asyncio.gather(
        fetch_user(), fetch_orders(), fetch_notifications()
    ) 
    result = {
        "user": res[0],
        "orders": res[1],
        "notifications": res[2]
    }
    
    # measuring the ending time
    end_time = time.time()
    
    print(result) 
    print(f"Total time: {end_time - start_time} seconds")
    # return result

asyncio.run(dashboard())

