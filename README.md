# Honda_Capstone
Creating a way to study our system as it performs across different scales of parking lots and other arrangements of variables.




Assumptions:
    The central thinking station only tells the whole system to do one thing at a time. ie, two navigators cannot be charging at one time
    In this program currently the navigator doesn't run out of battery. Realistically, it should need to recharge every 15 cars or so. I can add this feature later


    # leave the battery there to "finish charging". bc in real life, the navigator would be done far before the car is done charging, we need 
        # now we pretend the car is done charging and the battery needs to be taken back to the central station to be recharged.
        # at this point the navigator we used to bring it there probably isn't there anymore. to simulate this, we remove that nav from the list of navs that the
        # search method can see. This means the program doesnt work if you only have one navigator arm bot, which is ok considering our system isn't for very small
        # case use. At this point I would like to rewrite this code using a different time system, maybe one that uses a big loop that increases t=+1 each iteration,
        # but ironically I don't have the real life time to do that. so for now this (assumes every system has more than one navigator arm bot). 

    1 time = 1 min




    # bc each "unit" in the parking lot represents one parking space, and parking spaces arent square, we need a separate x and y speed for the navigators
    # we assume the worst case scenario where it takes the arm nav 3 minutes to complete the plug guidance feature. thats in our design requirements

    # assuming nav moves at 3mph, or 264ft/min, and a parking space is positioned so that the y axis follows the car's length, and the x axis follows the cars width
    # xSpeed=31.05 means that the nav traverses the width of 31.05 parking spaces in one minute (aka it moves at 3mph)
    # ySpeed=14.67 means that the nav traverses the length of 14.67 parking spaces in one minute (aka it moves at 3mph)