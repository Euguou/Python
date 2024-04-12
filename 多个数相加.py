running = True;
ans=0;
while running:
    user_input = input();
    if user_input == "":
        running = False;
        print(ans);
    else:  
        user_input = int(user_input);
        ans+=user_input;
