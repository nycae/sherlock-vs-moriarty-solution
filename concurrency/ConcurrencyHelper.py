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
                    threads.append( Thread(target = self.funct, args = arguments     ))
                else :
                    threads.append( Thread(target = self.funct, args = (arguments, ) ))


                threads[-1].start()
                tasks_started += 1

            # Remove completed tasks
            for t in threads:
                if not t.isAlive():

                    threads.remove(t)
                    tasks_completed += 1

class ConcurrentFor:

    def __init__(self, funct, values, max_threads):

        self.funct = funct
        self.values = values
        self.max_threads = max_threads<<<<<<< HEAD
<<<<<<< HEAD

    def run(self):

        class MyThread(Thread):

            def __init__(self, function, arguments, return_reference, return_index):

                Thread.__init__(self)

                self.function = function
                self.arguments = arguments
                self.return_reference = return_reference
                self.return_index = return_index

            def run(self):
                if isinstance(self.arguments, (list, )):
                    self.return_reference[self.return_index] = self.function(*self.arguments)
                else :
                    self.return_reference[self.return_index] = self.function(self.arguments)

        threads         = []
        tasks_completed = 0
        tasks_started   = 0
        return_values   = [None] * len(self.values)

        while tasks_completed < len(self.values):

            while len(threads) < self.max_threads and tasks_started < len(self.values):

                arguments = self.values[tasks_started]
                threads.append( MyThread(self.funct, arguments, return_values, tasks_started) )

                threads[-1].start()
                tasks_started += 1

            # Remove completed tasks
            for t in threads:
                if not t.isAlive():

                    threads.remove(t)
                    tasks_completed += 1

        return return_values

            threads = [t for t in threads if t.isAlive()]

            # Update completed tasks
            tasks_completed += self.max_threads - len(threads)



if __name__ == '__main__':

    def simpleFunction(to_print, to_sleep):
        print(to_print)
        time.sleep(to_sleep)
        return to_print

    def simplerFunction(to_sleep):
        time.sleep(to_sleep)
        return "Simple Function called"

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
    print(bucle.run())

    arguments2 =[1] * 10

    bucle = ConcurrentForVoidReturn(simpleFunction, arguments, 4)
    bucle.run()

    bluce = ConcurrentForVoidReturn(simplerFunction, arguments2, 4)
    bluce.run()
