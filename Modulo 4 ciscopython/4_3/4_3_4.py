def is_year_leap(yr):
    #
    # Write your code here.
    #
    
    test_data = [1900, 2000, 2016, 1987]
    test_results = [False, True, True, False]
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr,"->",end="")
        result = is_year_leap(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")
            
is_year_leap(yr=3)
