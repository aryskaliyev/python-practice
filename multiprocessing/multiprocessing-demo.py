# Multiprocessing: Running code in parallel.
# https://www.youtube.com/watch?v=fKl2JW_qrso

### Using 'multiprocessing' module -- Old Method ###
# import multiprocessing
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping for {seconds} second(s)...')
#     time.sleep(seconds)
#     print('Done Sleeping...')

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()
# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')

### Using 'concurrent.futures' module -- New Method ###
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    # Submit method schedules a function to be executed and
    # returns a future object.
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # In the order they were completed.
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # Map method returns results in the order they have started.
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
