import curses

def draw_menu(stdscr):
    # Clear the screen
    stdscr.clear()
    curses.start_color()

    # Turn on cursor
    curses.curs_set(1)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) 

    # Define the menu options
    menu_options = ["Option 1", "Option 2", "Option 3", "Exit"]
    current_option = 0

    while True:
        # Get the screen size
        height, width = stdscr.getmaxyx()

        # Calculate the total width of all options and spacing
        total_width = sum(len(option) + 2 for option in menu_options)  # 2 for extra spacing

        # Calculate the starting position to center the options horizontally
        start_x = (width - total_width) // 90

        # Display the menu options
        for i, option in enumerate(menu_options):
            # Highlight the current selected option
            if i == current_option:
                stdscr.addstr(height//10, start_x, option, curses.color_pair(1)|curses.A_REVERSE)
            else:
                stdscr.addstr(height//10, start_x, option,curses.color_pair(1))
            
            start_x += len(option) + 2

        # Wait for user input
        key = stdscr.getch()

        # Process user input
        if key == curses.KEY_LEFT and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_RIGHT and current_option < len(menu_options) - 1:
            current_option += 1
        elif key in [curses.KEY_ENTER, ord('\n')]:
            # Perform the action corresponding to the selected option
            selected_option = menu_options[current_option]
            if selected_option == "Exit":
                break
            # Add your custom actions for other menu options here
            if current_option == 0:
                pass
            # For example, call a function for each option

        stdscr.refresh()

# Run the application
curses.wrapper(draw_menu)
