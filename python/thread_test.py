from concurrent.futures import ThreadPoolExecutor
import time

def worker(timer, msg):
    time.sleep(timer)
    print(msg)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(worker, 3, "1")
    executor.submit(worker, 2, "2")

