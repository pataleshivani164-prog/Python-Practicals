# Initialize empty list
lst = []

while True:
    # Display menu
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")
    
    choice = input("Enter choice: ")
    
    # ADD
    if choice == '1':
        val = input("Integer: ")
        if val.lstrip('-').isdigit():   # check valid integer
            num = int(val)
            lst.append(num)
            print("List after adding:", lst)
        else:
            print("Invalid input")
    
    # REMOVE
      elif choice == '2':
        if not lst:
            print("List is empty")
        else:
            val = input("Integer: ")
            if val.lstrip('-').isdigit():
                num = int(val)
                if num in lst:
                    lst.remove(num)
                    print("List after removing:", lst)
                else:
                    print("Element not found")
            else:
                print("Invalid input")
    
    # DISPLAY
    elif choice == '3':
        if not lst:
            print("List is empty")
                  else:
            print(lst)
    
    # QUIT
    elif choice == '4':
        break
    
    # INVALID CHOICE
    else:
        print("Invalid choice")
    
