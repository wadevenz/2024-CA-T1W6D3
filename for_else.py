# for else

for i in range(10):
    print(i)
    if (i == 10): # i will never equal 10 as range will finish at coount - 1
        break
else:
    print("Loop Finished without interruption") # if for isnt broken and code successfully completes, else is then executed