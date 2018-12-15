#!/usr/bin/python3

# Author: Roberto Plaza Romero

from threading import Thread
import time


class ConcurrentForVoidReturn:

    def __init__(self, funct, values, max_threads):

        self.funct = funct
        self.values = values
        self.max_threads = max_threads
    
    def run(self):

        threads         = []
        tasks_completed = 0
        tasks_started   = 0

        while tasks_completed < len(self.values):
            
            # Create threads with the tasks
            while len(threads) < self.max_threads and tasks_started < len(self.values):

                arguments = self.values[tasks_started]

                if isinstance(arguments, (list,) ):
                    threads.append( Thread(target = self.funct, args = arguments) )
                else :
                    threads.append( Thread(target = self.funct, args = (arguments, )) )

                threads[-1].start()
                tasks_started += 1

            # Remove completed tasks
            threads = [t for t in threads if t.isAlive()]

            # Update completed tasks
            tasks_completed += self.max_threads - len(threads)


if __name__ == '__main__':

    def simpleFunction(to_print, to_sleep):
        print(to_print)
        time.sleep(to_sleep)

    def simplerFunction(to_sleep):
        print("Simple Function called")
        time.sleep(to_sleep)
    
    arguments = [
                ["Proceso0", 1],
                ["Proceso1", 1],
                ["Proceso2", 1],
                ["Proceso3", 1],
                ["Proceso4", 1],
                ["Proceso5", 1],
                ["Proceso6", 1],
                ["Proceso7", 1],
                ["Proceso8", 1],
                ["Proceso9", 1]
                ]
    arguments2 =[1] * 10
    
    bucle = ConcurrentForVoidReturn(simpleFunction, arguments, 4)
    bucle.run()

    bluce = ConcurrentForVoidReturn(simplerFunction, arguments2, 4)
    bluce.run()