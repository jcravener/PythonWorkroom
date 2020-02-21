
#LeetCode: 1184. Distance Between Bus Stops

def distanceBetweenBusStops(distance: [int], start: int, destination: int) -> int:
    
    if start < destination:
        return min( sum( distance[start:destination] ), sum( distance[destination:] + distance[:start] ) )
    else:
        return min( sum( distance[start:] + distance[:destination] ), sum( distance[destination:start] ) )

distance = [1,2,3,4]
start = 2
destination = 0

distance = [7,10,1,12,11,14,5,0]
start = 7
destination = 0

print(distanceBetweenBusStops(distance, start, destination))