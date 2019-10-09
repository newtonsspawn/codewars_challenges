class Dinglemouse(object):
    
    def __init__(self, queues, capacity):
        self.queues = list(map(list, queues))
        self.cap = capacity
        self.passengers = []
    
    def theLift(self):
        
        queues = self.queues
        cap = self.cap
        
        floors = len(queues)
        floors_visited = [0]

        def empty(seq):
            try:
                return all(map(empty, seq))
            except TypeError:
                return False
        
        def move(start=floors_visited[-1], direction='up'):
            
            if empty(queues):
                return
            
            if direction == 'up':
                floors_to_visit = [x for x in range(start, floors)]
            else:
                floors_to_visit = [x for x in range(start, -1, -1)]
            
            for floor in floors_to_visit:
                stop = False
                remove = []
                if floor in self.passengers:
                    stop = True
                    self.passengers = [x for x in self.passengers if x != floor]
                for waiter in queues[floor]:
                    if direction == 'up':
                        if (waiter > floor):
                            stop = True
                            if len(self.passengers) < cap:
                                self.passengers.append(waiter)
                                remove.append(waiter)
                    else:
                        if (waiter < floor):
                            stop = True
                            if len(self.passengers) < cap:
                                self.passengers.append(waiter)
                                remove.append(waiter)
                for waiter in remove:
                    queues[floor].remove(waiter)
                if stop and (floors_visited[-1] != floor):
                    floors_visited.append(floor)
                if not empty(self.passengers):
                    continue
                elif empty(queues):
                    if floors_visited[-1] != 0:
                        floors_visited.append(0)
                    break
                elif (direction == 'up') and empty(queues[floor+1:]):
                    move(start=floor, direction='down')
                elif (direction == 'down') and empty(queues[:floor]):
                    move(start=floor, direction='up')
            return
            
        move()
        
        return floors_visited


if __name__ == '__main__':

    lift = Dinglemouse(((), (), (5, 5, 5), (), (), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (), (1, 1), (), (), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (3,), (4,), (), (5,), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (0,), (), (), (2,), (3,), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((3,), (2,), (0,), (2,), (), (), (5,)), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (), (4, 4, 4, 4), (), (2, 2, 2, 2), (), ()), 2)
    print(lift.theLift())

    lift = Dinglemouse(((3, 3, 3, 3, 3, 3), (), (), (), (), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse((
            (6, 11, 2, 2), (14, 12, 8, 10, 0), (12, 11, 5, 8), (6, 13, 2), (),
            (10, 3, 3, 1), (), (12, 12, 12), (14, 6), (13, 7, 1), (2, 7),
            (3, 1), (), (3, 11, 1, 3), (11, 3, 4, 0, 8)), 4)
    print(lift.theLift())
