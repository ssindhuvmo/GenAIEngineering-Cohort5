import time

def time_lapsed (func):

    # Make the wrapper to capture start and end time
    # print the time lapsed
    def wrapper(*args):
        start_time = time.time()
        result = func(*args) # Call the original function
        end_time = time.time()
        
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper
	
	# use it on any function
@time_lapsed
def task (time_sec):

    # Simulate an intense task by delay
    time.sleep (time_sec)

@time_lapsed
def compute (factor) :

    rslt  = 0

    # Long computation
    for idx in range (factor) :

        rslt = rslt + ((factor * 1.2) + (factor + 2.78)) * 1.456
    
    return rslt        
	
	# Try with different delay values and check
task (1)

task (4)

r1 = compute (29876738)


r1 = compute (29876738)