from fractions import Fraction

def fifo_page_replacement(pages, capacity):
    page_faults = 0
    hits = 0
    page_queue = []
    page_set = set()

    for page in pages:
        if page in page_set:
            hits += 1
        else:
            page_faults += 1
            if len(page_queue) == capacity:
                removed_page = page_queue.pop(0)
                page_set.remove(removed_page)
            page_queue.append(page)
            page_set.add(page)

    return hits, page_faults

if __name__ == "__main__":
    pages = list(map(int, input("Enter the page references separated by space: ").split()))
    capacity = int(input("Enter the capacity: "))
    hits, faults = fifo_page_replacement(pages, capacity)
    total_pages = len(pages)
    hit_ratio = Fraction(hits, total_pages) if total_pages > 0 else 0
    print("Hits:", hits)
    print("Page faults:", faults)
    print("Hit ratio:", hit_ratio)
