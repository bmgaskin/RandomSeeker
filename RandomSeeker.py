# RandomSeeker
# Programmer: Billy Gaskin

def intro(iteration_count, max_random_number):
    boarder = "*" * 20
    print()
    print(boarder)
    print("**  RandomSeeker  **")
    print(boarder,"\n")
    print("Display the [count] of how many attempts it takes to find the requested")
    print("number as a random number (from 0 to {:,}) {} times.\n".format(max_random_number, iteration_count))

    while True:
        target_num = input("Enter your target number, or q to quit?: ")
        if target_num.upper() == "Q":
            return -1
        else:
            try:
                target_num = int(target_num)
            except ValueError:
                print("Stopping due to invalid entry.")
                return -1
        if target_num < 0 or target_num > max_random_number:
            print("Error: The number requested is out of range.\n")
        else:
            return(target_num)
    
def random_seeker(target_num, iteration_count, max_random_number):

    import random
    import datetime
    import time
    import statistics

    print("\nSeeking for number: {:,}".format(target_num))
    now = datetime.datetime.now()
    start = time.time()
    print("Start Time:", now.strftime("%A, %x %I:%M:%S %p"))
    the_results = []
    loop_count = 1
    innerloop = 1
    start_time = time.time()
    while True:
        x1 = random.randint(0, max_random_number)
        if x1 == target_num:
            now = datetime.datetime.now()
            print("Pass #",loop_count, " Elapsed time in seconds: {0:.2f} ".format(time.time() - start_time),
                  "[{:,}]".format(innerloop),sep='')
            the_results.append(innerloop)
            if loop_count == iteration_count:
                break
            else:
                loop_count += 1
                innerloop = 1
                start_time = time.time()
        else:
            innerloop += 1
    now = datetime.datetime.now()
    print("End Time:", now.strftime("%A, %x %I:%M:%S %p"))
    run_time = time.time() - start
    print("\nTotal run time in seconds: {0:.2f}".format(run_time), "or {0:.2f} minutes.".format(run_time/60))
    the_mean = statistics.mean(the_results)
    print("Mean value:", "{:,}".format(int(the_mean)))
    return

def main(args=None):
    iteration_count: int = 5
    max_random_number: int = 10000000
    target_num = intro(iteration_count, max_random_number) 
    if target_num >= 0:
        random_seeker(target_num, iteration_count, max_random_number)
        input("\nCompleted! Press Enter to quit.")
    print("Goodbye")

if __name__ == '__main__':
    main()

