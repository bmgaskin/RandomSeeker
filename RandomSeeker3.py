#
# Billy Gaskin
# Version 3 - June 20, 2019
#


def intro(max_count, max_randon_number):

    print("**\n** RandomSeeker by Billy Gaskin - v3", "\n**\n")
    print("Display the [count] of how many times it takes to find the requested")
    print("number as a random number (between 0 and {}) {} times...\n\n".format(max_random_number, max_count))

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


def random_seeker(my_num, max_loop_count, max_randon_number):

    import random
    import datetime
    import time
    import statistics

    now = datetime.datetime.now()
    start = time.time()
    print("\nStart Time:", str(now))
    my_results = []
    loop_count = 1
    innerloop = 1
    start_time = time.time()
    while True:
        x1 = random.randint(0, max_random_number)
        if x1 == my_num:
            now = datetime.datetime.now()
            print("Loop Count:", loop_count, "Elapsed time in seconds: {0:.2f}".format(time.time() - start_time),
                  "[{}]".format(innerloop))
            my_results.append(innerloop)
            if loop_count == max_loop_count:
                # print("\n",my_results)
                break
            else:
                loop_count += 1
                innerloop = 1
                start_time = time.time()
        else:
            innerloop += 1
    now = datetime.datetime.now()
    print("End Time:", str(now))
    print("\nTotal run time in seconds: {0:.2f}".format(time.time() - start))
    my_mean = statistics.mean(my_results)
    print("Mean value:", int(my_mean))
    return


#
# Start Execution
#

max_loop_count: int = 5
max_random_number: int = 10000000

my_num = intro(max_loop_count, max_random_number)
if my_num >= 0:
    random_seeker(my_num, max_loop_count, max_random_number)

# End of program...

