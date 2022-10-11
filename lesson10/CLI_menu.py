while True:
    print("""
    Welcome to calculator menu
    """)
    menu = """
    Make your choice
    
    1. Add numbers
    2. Diff numbers
    3. Mult numbers
    4. Div numbers
    """
    print(menu)
    user_choice = input('Enter yor choice: ')
    if not user_choice:
        print('Bye')
        break

    while True:
        menu_inner = """
            Make your choice

            1. Add numbers
            2. Diff numbers
            3. Mult numbers
            4. Div numbers
            """
        print(menu_inner)
        user_choice = input('Enter yor choice: ')
        if not user_choice:
            print('Back to main menu')
            break
