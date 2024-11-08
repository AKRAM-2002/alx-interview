from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, val):
        '''Add an element to the end of the queue'''
        self.queue.append(val)
    
    def dequeue(self):
        '''Remove and return the element from the front of the queue. Return None if empty.'''
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def peek(self):
        '''Return the front element without removing it. Return None if empty.'''
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        '''Check if the queue is empty'''
        return len(self.queue) == 0

class Jobs:

    def __init__(self):
        # Initialize the queue
        self.queue = Queue()
        # Initialize the total_jobs and total_time variables
        self.total_jobs = 0
    
    def add_job(self, name):
        # Add a job to the queue
        self.queue.enqueue(name)
        self.total_jobs += 1
        print("New job added to the queue. Total jobs: ", self.total_jobs)
        
    
    def remove_job(self):
        if not self.queue.is_empty():
            self.total_jobs -= 1
            job = self.queue.dequeue()
            print(f"Job '{job}' completed. Remaining jobs: {self.total_jobs}")
            return job
        else:
            print("No jobs in the queue to remove.")
            return None
    
    def process_job(self):

        while not self.queue.is_empty():
            print("Processing job: ", self.queue.peek())
            self.remove_job()
        print("No jobs left in the queue.")

    

    
# Example usage
if __name__ == "__main__":
    jobs = Jobs()
    jobs.add_job("Job 1")
    jobs.add_job("Job 2")
    jobs.add_job("Job 3")
    jobs.process_job()
    jobs.remove_job()
    jobs.process_job()
    jobs.add_job("Job 4")


