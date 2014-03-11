import work_queue as wq

t0 = wq.Task('ls')
t1 = t0.clone()
t2 = t0.clone()
t3 = t1.clone()

for t in [t0,t1,t2,t3]:
    print t._task
