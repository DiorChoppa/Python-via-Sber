import threading
import time
import random

class Philosopher(threading.Thread):

    running = True

    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            time.sleep(random.uniform(5, 10))
            print("{} is hungry".format(self.name))
            self.dine()

    def dine(self):
        while self.running:
            self.left_fork.acquire()
            if not self.right_fork.locked():
                self.right_fork.acquire()
                break
            else:
                self.left_fork.release()
        else:
            return

        self.start_dining()
        self.left_fork.release()
        self.right_fork.release()
        print("{} stop eating, start thinking".format(self.name))

    def start_dining(self):
        print("{} start eating".format(self.name))
        time.sleep(random.uniform(10, 20))

def go_philosophers():
    forks = [threading.Lock() for n in range(5)]
    names = ["Socrat", "Niche", "Aristotel", "Kant", "Mark"]

    philosophers = [Philosopher(names[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(50)
    Philosopher.running = False
    print("FINISH!!!")

if __name__ == "__main__":
    go_philosophers()