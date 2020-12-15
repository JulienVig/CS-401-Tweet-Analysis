import threading
import multiprocessing
from time import sleep


import twint
import nest_asyncio
import datetime
import os
import sys

# sys.path.append('../scripts/time_partition')
sys.path.insert(1, '../scripts/')
from time_partition import create_keyword_partition

nest_asyncio.apply()
DATA_FILE = "../sample_scrap/"

NB_PROC = 2
NB_THREAD_P_PROC = 1

def process_run(task_queue):
    for i in range(NB_THREAD_P_PROC):
        thread = threading.Thread(target = thread_run, args=(task_queue,))
        thread.start()
        sleep(20)

def thread_run(task_queue):
    continue_ = True
    while continue_:
        task = task_queue.get()
        if task == None:
            task_queue.put(None)
            continue_ = False
            break
        term = task[0]
        since = task[1]
        until = task[2]
        print("Beginning scrapping ", term, " from ", since, " until ", until)
        Scrap(term, since, until)
        print("Finished scrapping ", term, " from ", since, " until ", until)
        if (until == "2014-12-31"):
            print("##################### Finished last month of term ", term)
    print("No more element in the queue, terminating")

def Scrap(term, since, until):
    print(term, ' from ', since, ' to ', until)
    c = twint.Config()
    twint.token.Token(c).refresh()
    c.Search = term
    c.Since = since
    c.Until = until
    #c.Until = "2012-06-01"
    folder = DATA_FILE+term
    if not os.path.isdir(folder):
        os.mkdir(folder)
    c.Output = folder+'/'+since+'-'+term+".csv"
    c.Hide_output = True
    c.Store_csv = True
    twint.run.Search(c)
    
if __name__ == '__main__':

    if not os.path.isdir(DATA_FILE):
        os.mkdir(DATA_FILE)

    sample = ['abu_sayyaf']
    work = []

    for keyword in sample:
        work+=create_keyword_partition(keyword, 5)
    work = sorted(work, key= lambda elem: elem[0])
    print(work[:5])

    task_queue = multiprocessing.Queue()

    for w in work:
        task_queue.put(w)
    for i in range(NB_PROC):
        task_queue.put(None)
    num_cores = multiprocessing.cpu_count()
    print(num_cores)
    the_pool = multiprocessing.Pool(NB_PROC, process_run, (task_queue,))
    sleep(7200)