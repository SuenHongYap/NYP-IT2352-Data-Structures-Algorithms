import Function



while True:
    user_input=Function.ask_qn()
    if user_input==1:
        if Function.count<20:
            Function.add_product()
        else:
            print("You have reached the max no of product")
    elif user_input==2:
        Function.del_product()
    elif user_input==3:
        Function.update_info()
    elif user_input==4:
        Function.display_product()
    elif user_input==5:
        while True:
            try:
                search_choice=int(input("Which Search do you want to use? (1. Sequential Search, 2. Binary search): "))
                break
            except ValueError:
                print("Oops!, that was not a number. Please try again")
        while True:
            try:
                search_option=int(input("What Number do you want to search for?: "))
                break
            except ValueError:
                print("Oops!, that was not a number. Please try again")
        if search_choice==1:
            u=Function.sortedSequentialSearch(search_option)
            if u==True:
                print("%s can be found in database, this is its detail" %search_option)
                Function.search(search_option)
            elif u==False:
                print("%s cannot be found in database" %search_option)
        elif search_choice==2:
            u=Function.binarySearch(search_option)
            if u==True:
                print("%s can be found in database, this is its detail" %search_option)
                Function.search(search_option)
            elif u==False:
                print("%s cannot be found in database" %search_option)
        else:
            print("You have entered a invalid option")
    elif user_input==6:
        while True:
            try:
                sort_choice=int(input("How do you want to sort your product? (1. BubbleSort, 2. SelectionSort, 3.Insertion Sort): "))
                break
            except ValueError:
                print("Oops!, that was not a number. Please try again")
        if sort_choice==1:
            Function.bubbleSort()
        elif sort_choice==2:
            Function.selectionSort()
        elif sort_choice==3:
            Function.insertionSort()
    elif user_input==7:
        Function.end()
        break



