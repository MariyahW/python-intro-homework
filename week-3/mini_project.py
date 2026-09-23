day=input("What day of the week would you like to complete the suggested activity?")
dur=input("How about the time of day? Morning, Afternoon, or Evening?")

day=day.lower()
dur=dur.lower()
match day:
    case "monday" | "tuesday":
        if dur=="morning":
            print("You should go for a run.")
        elif dur=="afternoon":
            print("You should go to study Python!")
        elif dur=="evening":
            print("You should go to the gym.")
        else:
            print("Please enter a valid time of day.")
    case "wednesday" | "thursday":
        if dur=="morning":
            print("You should go to the gym.")
        elif dur=="afternoon":
            print("You should go to work on your side project.")
        elif dur=="evening":
            print("You should go get dinner with friends.")
    case "friday" | "saturday":
        if dur=="morning":
            print("You should go make pottery.")
        elif dur=="afternoon":
            print("You should go to the movies.")
        elif dur=="evening":
            print("You should go to a concert!")
        else:
            print("Please enter a valid time of day.")
    case "sunday":
        if dur=="morning":
            print("You should meditate.")
        elif dur=="afternoon":
            print("You should go to the park.")
        elif dur=="evening":
            print("You should go to bed early.")
        else:
            print("Please enter a valid time of day.")
    case _:
        print("Please enter a valid day of the week.")
