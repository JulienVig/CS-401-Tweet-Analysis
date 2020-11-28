import threading
import multiprocessing
from time import sleep
from joblib import Parallel, delayed
import threading

import twint
import nest_asyncio
import tqdm
import datetime
import os

nest_asyncio.apply()
DATA_FILE = "data_test/"

NB_PROC = 12
NB_THREAD_P_PROC = 20

def process_run(task_queue):
    for i in range(NB_THREAD_P_PROC):
        thread = threading.Thread(target = thread_run, args=(task_queue,))
        thread.start()

def thread_run(task_queue):
    continue_ = True
    while continue_:
        task = task_queue.get()
        if task == None: #TODO change
            task_queue.put(None)
            continue_ = False
            break
        term = task[0]
        since = task[1]
        until = task[2]
        print("Beginning scrapping ", term, " from ", since, " until ", until)
        Scrap(term, since, until)
        print("Finished scrapping ", term, " from ", since, " until ", until)
        if (int(until[-2:])>25):
            print("##################### Finished term ", term)
    #print("No more element in the queue, terminating")

def Scrap(term, since, until):
    print(term, ' from ', since, ' to ', until)
    c = twint.Config()
    c.Search = term
    c.Since = since
    c.Until = until
    #c.Until = "2012-06-01"
    folder = DATA_FILE+term
    os.mkdir(folder)
    c.Output = folder+'/'+since+'-'+term+".csv"
    c.Hide_output = True
    c.Store_csv = True
    twint.run.Search(c)
    
if __name__ == '__main__':
    task_queue = multiprocessing.Queue()
    work = [['abu_sayyaf', '2012-01-01', '2012-02-01'], ['afghanistan', '2012-01-01', '2012-02-01']]
    for w in work:
        task_queue.put(w)
    for i in range(NB_PROC):
        task_queue.put(None)
    num_cores = multiprocessing.cpu_count()
    print(num_cores)
    the_pool = multiprocessing.Pool(NB_PROC, process_run, (task_queue,))
    #results = Parallel(n_jobs=NB_PROC)(delayed(process_run)(task_queue) for i in range(NB_PROC))
    sleep(45)