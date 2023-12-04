class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Qlist = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.isFull():
            print("The list is full or overflow")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Qlist[self.rear] = item
        self.size = self.size + 1
        #print("%s added to list" % str(item))

    def dequeue(self):
        if self.isEmpty():
            print("The list is empty or underflow")
            return
        item = self.Qlist[self.front]
        for i in range(self.front, self.size - 1):
            self.Qlist[i] = self.Qlist[i + 1]
        self.Qlist[self.size - 1] = None
        self.size = self.size - 1
        #print(item, " is removed from list")
        return item

    def getQueueFront(self):
        '''
        if self.isEmpty():
            print("Queue is empty.")
        print("Front item is ", self.Qlist[self.front])
        '''
        return self.Qlist[self.front]

    def getQueueRear(self):
        '''
        if self.isEmpty():
            print("Queue is empty.")
        print("Rear item is ", self.Qlist[self.rear])
        '''
        return self.Qlist[self.rear]


class CarInfo:
    def __init__(self, plate_number, arrival_time):
        self.plate_number = plate_number
        self.arrival_time = arrival_time

class ParkingLot:
    def __init__(self, capacity):
        self.queue = Queue(capacity)

    def car_in(self, plate_number, arrival_time):
        if self.queue.isFull():
            print("Parking lot is full!")
        else:
            car_info = CarInfo(plate_number, arrival_time)
            self.queue.enqueue(car_info)
            print("Car with plate \"{0}\" has entered the parking lot at {1}.".format(car_info.plate_number, car_info.arrival_time))

    def car_out(self):
        if self.queue.isEmpty():
            print("Parking lot is empty!")
        else:
            front_car = self.queue.dequeue()
            if (front_car):
                print("Car with plate \"{0}\" has lef the parking lot at {1}.".format(front_car.plate_number, "00:00"))

    def display(self):
        size = self.queue.capacity
        lots = "|"
        for i in range(size):
            car = ""
            if self.queue.Qlist[i]:
                car = self.queue.Qlist[i].plate_number
            lots += " {0} |".format(car)
        
        print("Parking Lot:\n<< [EXIT] {0} << [ENTRANCE]".format(lots))

    def display2(self):
        size = self.queue.capacity
        lots = "|"
        for i in range(size):
            car = ""
            if self.queue.Qlist[i]:
                car = "🚗"
            lots += " {0} |".format(car)
        print("<< [EXIT] {0} << [ENTRANCE]".format(lots))



if __name__ == '__main__' :
    size = int(input("Enter parking lot size: "))
    parking_lot = ParkingLot(size)
    while True:
        print("Parking Lot Program:\n1. Enter Parking Lot\n2. Exit Parking Lot\n3. Display Parking Lot\n4. Display Parking Lot Icon\n5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            plate_number = input("Enter plate number: ")
            arrival_time = input("Enter arrival time: ")
            parking_lot.car_in(plate_number, arrival_time)
        elif choice == 2:
            parking_lot.car_out()
        elif choice == 3:
            parking_lot.display()
        elif choice == 4:
            parking_lot.display2()
        elif choice == 5:
            break
        else:
            print("Invalid input.")

