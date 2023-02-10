product_dict={1:["Puma Slides",20,500,"Puma","Sports"],2:["Fila Slides",30,100,"Fila","Sports"],
              3:["Iphone10",820,1000,"Iphone","Electronic"],
              4:["Samsung z-flip",1250,800,"Samsung","Electronic"],
              5:["Cannon A4 Paper",50,500,"Cannon","Paper"], 6:["Cannon Camera",625,720,"Cannon","Electronic"],
              7:["Nike running shoe",225,200,"Nike","Sports"], 8:["Doulbe A A4 paper",70,120,"Double A","Paper"],
              9:["Puma Cap",10,1200,"Puma","Sports"]}
select=0
count=len(product_dict)
def add_product():
    global count
    name=input("Enter product name: ")
    while True:
        try:
            price= int(input("Enter the cost of the product: "))
            break
        except ValueError:
            print("Oops!, That was not a number. Please try again")
    while True:
        try:
            quantity = int(input("Enter how many quantity are there: "))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")

    while True:
        brand=input("What will be the new brand name for your product?: ")
        if brand.isalpha():
            break
        else:
            print("Please enter only alphabetical characters")
    while True:
        category = input("Enter which category should it fall under: ")
        if category.isalpha():
            break
        else:
            print("Please enter only alphabetical characters")
    count+=1

    product_dict[count]=[name,price,quantity,brand,category]
    print("A product have been added sucessfully with a search code of %s."%count)
    return count



def del_product():
    while True:
        try:
            delete=int(input("What is the product id you want to delete?: "))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")
    global count
    no_of_item=len(product_dict)
    for key in product_dict.copy():
        if delete==key:
            del(product_dict[delete])
            print("The product have been deleted")
            count-=1
            no_of_run=no_of_item-delete
            item_to_del=delete
            for i in range(no_of_run):
                product_dict[item_to_del]=product_dict.pop(item_to_del+1)
                item_to_del+=1
            return count

def bubbleSort():
    while True:
        try:
            user_input=int(input("How would you like to sort by?(0.Name/1.Price/2.Quantity/3.Brand/4.Category):" ))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")
    if user_input<5:
        user_choice=input("Enter 'A' for ascending and 'B' for descending sort: ")
        choice=user_choice.capitalize()
        my_list = list(product_dict.items())
        n = len(my_list)

        # Perform n-1 bubble operations on the sequence
        for i in range(n -1, 0, -1):

            # Bubble the largest item to the end
            for j in range(i):
                if choice=="A":
                    if my_list[j][1][user_input] > my_list[j + 1][1][user_input]:
                        # Swap the j and j+1 items
                        tmp = my_list[j]
                        my_list[j] = my_list[j + 1]
                        my_list[j + 1] = tmp
                elif choice=="B":
                    if my_list[j][1][user_input] < my_list[j + 1][1][user_input]:
                        # Swap the j and j+1 items
                        tmp = my_list[j]
                        my_list[j] = my_list[j + 1]
                        my_list[j + 1] = tmp
                else:
                    print("You have entered a invalid input!")
                    break

        print(my_list)
    else:
        print("You have enter a invalid input!")

def selectionSort():
    while True:
        try:
            user_input=int(input("How would you like to sort by?(0.Name/1.Price/2.Quantity/3.Brand/4.Category):" ))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")
    if user_input<5:
        user_choice=input("Enter 'A' for ascending and 'B' for descending sort: ")
        choice=user_choice.capitalize()
        my_list = list(product_dict.items())
        n = len(my_list)

        for i in range(n - 1):
            # Assume the ith element is the smallest.
            smallNdx = i

            # Determine if any other element contains a smaller value.
            for j in range(i+1, n):
                if choice=="A":
                    if my_list[j][1][user_input] < my_list[smallNdx][1][user_input]:
                        smallNdx = j
                elif choice=="B":
                    if my_list[j][1][user_input] > my_list[smallNdx][1][user_input]:
                        smallNdx = j
                else:
                    break

            # Swap the ith value and smallNdx value only if the smallest
            # value is not already in its proper position.
            if smallNdx != i:
                tmp = my_list[i]
                my_list[i] = my_list[smallNdx]
                my_list[smallNdx] = tmp

        print(my_list)
    else:
        print("You have entered a invalid input!")

def insertionSort():
    while True:
        try:
            user_input=int(input("How would you like to sort by?(0.Name/1.Price/2.Quantity/3.Brand/4.Category):" ))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")
    if user_input<5:
        user_choice=input("Enter 'A' for ascending and 'B' for descending sort: ")
        choice=user_choice.capitalize()
        my_list = list(product_dict.items())
        n = len(my_list)
        # Starts with the first item as the only sorted entry.
        for i in range(1, n):
            # Save the value to be positioned
            value = my_list[i]

            # Find the position where value fits in the
            # ordered part of the list.
            pos = i
            if choice=="A":
                while pos > 0 and value[1][user_input] < my_list[pos - 1][1][user_input]:
                    # Shift the items to the right during the search
                    my_list[pos] = my_list[pos-1]
                    pos -= 1

                    # Put the saved value into the open slot.
                    my_list[pos] = value
            elif choice=="B":
                while pos > 0 and value[1][user_input] > my_list[pos - 1][1][user_input]:
                    # Shift the items to the right during the search
                    my_list[pos] = my_list[pos-1]
                    pos -= 1

                    # Put the saved value into the open slot.
                    my_list[pos] = value
            else:
                print("You have entered a invalid input!")
                break
        print(my_list)
    else:
        print("You have entered a invalid input!")

def sortedSequentialSearch(target):
    my_list=[]
    global count
    for key in product_dict:
        count+=1
        my_list.insert(count,key)
    n = len(my_list)
    for i in range(n):
        # If the target is in the ith element, return True
        if my_list[i] == target:
            return True
        elif my_list[i] > target: #STOP searching
            return False
    return False # If not found, return False

def binarySearch(target):
    my_list=[]
    global count
    for key in product_dict:
        count+=1
        my_list.insert(count,key)
    low = 0
    high = len(my_list)-1
    # Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (high+low) //2
        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list)
        if my_list[mid] == target:
            return True
        # Or is the target before the midpoint?
        elif target < my_list[mid]:
            high=mid -1
        # Or is the target after the midpoint?
        else:
            low= mid+1
        # If the sequence cannot be subdivided further,
        # target is not in the list of values
    return False


def display_product():
    for key in product_dict:
        print(key, product_dict[key])

def ask_qn():
    while True:
        try:
            select=int(input("Select the program (1-7) to run:"+
                 "\n"+"1. Add A Product"+
                 "\n"+"2. Delete A Product"+
                 "\n"+"3. Update A Product Record"+
                 "\n"+"4. Display All Product"+
                 "\n"+"5. Search For A Product"+
                "\n"+"6. Sort The Program"+
                "\n"+"7. Quit The Program"+
                 "\n"+"Enter your command (1-7): "))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")
    return select

def update_info():
    while True:
        try:
            choice=int(input("Enter The Id You Want To Update: "))
            break
        except ValueError:
            print("Oops!, that was not a number. Please try again")
    for key in product_dict.copy():
        if choice==key:
            while True:
                try:
                    update_choice=int(input("What would you like to update?(1.Name/2.Price/3.Quantity/4.Brand/5.Category): "))
                    break
                except ValueError:
                    print("Oops!, that was not a number. Please try again")
            if update_choice<6:
                if update_choice==1:
                    question=input("What will be the new name for your product?: ")
                    product_dict[choice][0]=question
                elif update_choice==2:
                    while True:
                        try:
                            question=int(input("What will be the new price for your product?: "))
                            product_dict[choice][1]=question
                            print("Done!")
                            break
                        except ValueError:
                            print("Oops!, that was not a number. Please try again.")
                elif update_choice==3:
                    while True:
                        try:
                            question=int(input("What will be the new Quantity for your product?: "))
                            product_dict[choice][2]=question
                            print("Done!")
                            break
                        except ValueError:
                            print("Oops!, that was not a number. Please try again.")
                elif update_choice==4:
                    while True:
                        question=input("What will be the new brand name for your product?: ")
                        if question.isalpha():
                            product_dict[choice][3]=question
                            print("Done!")
                            break
                        else:
                            print("Please enter only alphabetical characters")
                elif update_choice==5:
                    while True:
                        question=input("What will be the new Category for your product?: ")
                        if question.isalpha():
                            product_dict[choice][4]=question
                            print("Done!")
                            break
                        else:
                            print("Please enter only alphabetical characters")
            else:
                print("You have entered a invalid input!")

def end():
    print("Thank You")


def search(search_option):
    for key in product_dict.copy():
        if search_option==key:
            print([product_dict[search_option]])


