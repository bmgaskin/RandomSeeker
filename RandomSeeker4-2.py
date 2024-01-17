# RandomSeeker
# Date: 27-DEC-2021
# Developed by: Billy Gaskin

def intro(max_loop_count, max_random_number):

    print("**\n** RandomSeeker", "\n**\n")
    print("Display the [count] of how many attempts it takes to find the requested")
    print("number as a random number (between 0 and {:,}) {} times...\n\n".format(max_random_number, max_loop_count))

    while True:
        my_num = input("What number do you want to use, or q to quit?: ")
        if my_num.upper() == "Q":
            break
        else:
            try:
                my_num = int(my_num)
            except ValueError:
                print("Exiting due to invalid entry.")
                break
        if my_num < 0 or my_num > max_random_number:
            print("Error: The number requested is out of range.\n")
        else:
            return(my_num)
    return -1


def random_seeker(my_num, max_loop_count, max_random_number):

    import random
    import datetime
    import time
    import statistics

    print("\nSeeking for number: {:,}".format(my_num))
    now = datetime.datetime.now()
    start = time.time()
    print("Start Time:", now.strftime("%A, %x %I:%M:%S %p"))
    my_results = []
    loop_count = 1
    innerloop = 1
    start_time = time.time()
    while True:
        x1 = random.randint(0, max_random_number)
        if x1 == my_num:
            now = datetime.datetime.now()
            print("Pass #",loop_count, " Elapsed time in seconds: {0:.2f} ".format(time.time() - start_time),
                  "[{:,}]".format(innerloop),sep='')
            my_results.append(innerloop)
            if loop_count == max_loop_count:
                #print("\n",my_results)
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
    my_mean = statistics.mean(my_results)
    print("Mean value:", "{:,}".format(int(my_mean)))
    return

def main(args=None):
    max_loop_count: int = 5
    max_random_number: int = 10000000
    my_num = intro(max_loop_count, max_random_number) 
    if my_num >= 0:
        random_seeker(my_num, max_loop_count, max_random_number)
        input("\nCompleted! Press Enter to quit...")

if __name__ == '__main__':
    main()

