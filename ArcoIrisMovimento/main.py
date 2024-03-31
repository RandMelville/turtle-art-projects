from drawer import Drawer

if __name__ == "__main__":
    drawer = Drawer(screen_width=600, screen_height=600)

    while True:
        drawer.draw_rainbow(rainbow_lines_number=7)
        drawer.reconfigure_pen()
