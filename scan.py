def scan_disk_scheduling(requests, start_position, direction, disk_size):
    total_head_movement = 0
    current_position = start_position
    requests_set = set(requests)

    sequence = [start_position]  # Prepend the starting position

    while requests_set:
        if direction == "right":
            for i in range(current_position, disk_size):
                if i in requests_set:
                    requests_set.remove(i)
                    total_head_movement += abs(i - current_position)
                    current_position = i
                    sequence.append(i)

            # Check if there are any remaining requests in the opposite direction
            if requests_set:
                total_head_movement += disk_size - 1 - current_position  # Move to the end
                current_position = disk_size - 1  # Update current position
                direction = "left"  # Change direction
                sequence.append(current_position)  # Add endpoint of right direction to sequence

        elif direction == "left":
            for i in range(current_position, -1, -1):
                if i in requests_set:
                    requests_set.remove(i)
                    total_head_movement += abs(i - current_position)
                    current_position = i
                    sequence.append(i)

            # Check if there are any remaining requests in the opposite direction
            if requests_set:
                total_head_movement += current_position  # Move to the beginning
                current_position = 0  # Update current position
                direction = "right"  # Change direction
                sequence.append(current_position)  # Add endpoint of left direction to sequence

    return total_head_movement, sequence


if __name__ == "__main__":
    disk_size = int(input("Enter the disk size: "))
    start_position = int(input("Enter the starting position: "))
    requests = list(map(int, input("Enter the requests separated by space: ").split()))
    direction = input("Enter the initial direction (left/right): ").lower()

    total_head_movement, sequence = scan_disk_scheduling(requests, start_position, direction, disk_size)
    print("Total head movement:", total_head_movement)
    print("Sequence of requests served:", sequence)