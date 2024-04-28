def look_disk_scheduling(requests, start_position, direction, disk_size):
    total_head_movement = 0
    current_position = start_position
    requests_set = set(requests)

    # Sort the requests in ascending order
    requests_sorted = sorted(requests)

    sequence = [start_position]  # Prepend the starting position

    while requests_set:
        if direction == "right":
            for i in requests_sorted:
                if i >= current_position and i in requests_set:
                    requests_set.remove(i)
                    total_head_movement += abs(i - current_position)
                    current_position = i
                    sequence.append(i)

            # Check if there are any remaining requests in the opposite direction
            if requests_set:
                last_request_right = max(requests_sorted)
                total_head_movement += abs(last_request_right - current_position)
                current_position = last_request_right
                direction = "left"
                sequence.append(current_position)

        elif direction == "left":
            for i in reversed(requests_sorted):
                if i <= current_position and i in requests_set:
                    requests_set.remove(i)
                    total_head_movement += abs(i - current_position)
                    current_position = i
                    sequence.append(i)

            # Check if there are any remaining requests in the opposite direction
            if requests_set:
                first_request_left = min(requests_sorted)
                total_head_movement += abs(first_request_left - current_position)
                current_position = first_request_left
                direction = "right"
                sequence.append(current_position)

    return total_head_movement, sequence


if __name__ == "__main__":
    disk_size = int(input("Enter the disk size: "))
    start_position = int(input("Enter the starting position: "))
    requests = list(map(int, input("Enter the requests separated by space: ").split()))
    direction = input("Enter the initial direction (left/right): ").lower()

    total_head_movement, sequence = look_disk_scheduling(requests, start_position, direction, disk_size)
    print("Total head movement:", total_head_movement)
    print("Sequence of requests served:", sequence)