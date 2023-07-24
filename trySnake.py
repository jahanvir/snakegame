
import curses
def main(screen):
    # Configure screen
    screen.timeout(0)
    screen.refresh()
    size=10
    for i in range(size):
            row = ''
            for j in range(size):
                row += '.'

            screen.addstr(i, 0, row)
    
    # Refresh the screen to display the changes
    screen.refresh()

    # Wait for a key press before exiting
    screen.getch()
    
if __name__=='__main__':
    curses.wrapper(main)