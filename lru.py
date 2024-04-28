from fractions import Fraction

def lru_page_replacement(pages, capacity):
    page_faults = 0
    hits = 0
    page_list = []

    for page in pages:
        if page in page_list:
            hits += 1
            page_list.remove(page)
            page_list.append(page)  # Move the page to the end of the list (recently used)
        else:
            page_faults += 1
            if len(page_list) == capacity:
                page_list.pop(0)  # Remove the least recently used page (first element of the list)
            page_list.append(page)

    return hits, page_faults

if __name__ == "__main__":
    pages = list(map(int, input("Enter the page references separated by space: ").split()))
    capacity = int(input("Enter the capacity: "))
    hits, faults = lru_page_replacement(pages, capacity)
    total_pages = len(pages)
    hit_ratio = Fraction(hits, total_pages) if total_pages > 0 else 0
    print("Hits:", hits)
    print("Page faults:", faults)
    print("Hit ratio:", hit_ratio)
