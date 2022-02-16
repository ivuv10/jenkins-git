while True:
    try:
        name = input ("What is your name ? ").strip()
        if name.startswith("A"):
            print("message for A")
            break       
        elif name.startswith("N"):
            print("message for N")
            break
        else:
            print("Sorry, my only purpose is to talk to N and A")
    except ValueError:
        print ("Sorry, my only purpose is to talk to N and A")