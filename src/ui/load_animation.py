import sys
import time


def loading_animation(stop):
    chars = ["   ", ".  ", ".. ", "..."]
    while not stop.is_set():
        for char in chars:
            sys.stdout.write("\rThis may take a few minutes" + ('.' * 67) + "Loading" + char)
            sys.stdout.flush()
            time.sleep(0.5)
