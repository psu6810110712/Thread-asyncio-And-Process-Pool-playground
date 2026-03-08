import asyncio
import time
import multiprocessing
import threading
import random

# ข้อมูลจำลอง: รายชื่อสื่อที่ต้องประมวลผล (ความเหงาระดับ 5 Centimeters per Second)
MEDIA_LIST = ["Cherry Blossom", "One more time", "One more chance", "Distance", "Speed"] * 10

# --- 1. Asyncio (I/O Bound - เหมาะสำหรับดึงข้อมูลจากเน็ต) ---
async def fetch_quote_async(media_name):
    wait_time = random.uniform(0.1, 0.5)
    await asyncio.sleep(wait_time) # จำลองการรอ Network
    return f"Async: {media_name} processed in {wait_time:.2f}s"

async def run_asyncio():
    tasks = [fetch_quote_async(m) for m in MEDIA_LIST]
    return await asyncio.gather(*tasks)

# --- 2. Threading (I/O Bound - เหมาะสำหรับเขียนไฟล์/DB) ---
def save_metadata_thread(media_name, results):
    time.sleep(0.2) # จำลองการเขียน Disk
    results.append(f"Thread: {media_name} saved")

def run_threading():
    results = []
    threads = []
    for m in MEDIA_LIST:
        t = threading.Thread(target=save_metadata_thread, args=(m, results))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results

# --- 3. Process Pool (CPU Bound - เหมาะสำหรับแต่งภาพ/คำนวณหนักๆ) ---
def calculate_melancholy_score(media_name):
    # จำลองการคำนวณหนักๆ (CPU Intensive)
    count = 0
    for i in range(10**6):
        count += i
    return f"Process: {media_name} score is {count}"

def run_multiprocessing():
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_melancholy_score, MEDIA_LIST)
    return results

# --- Main Performance Test ---
if __name__ == "__main__":
    print("🚀 Starting Antigravity Concurrency Test...\n")

    # Test Asyncio
    start = time.perf_counter()
    asyncio.run(run_asyncio())
    print(f"⏱️  Asyncio (I/O): {time.perf_counter() - start:.4f} seconds")

    # Test Threading
    start = time.perf_counter()
    run_threading()
    print(f"⏱️  Threading (I/O): {time.perf_counter() - start:.4f} seconds")

    # Test Multiprocessing
    start = time.perf_counter()
    run_multiprocessing()
    print(f"⏱️  Process Pool (CPU): {time.perf_counter() - start:.4f} seconds")
