import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison method for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
   
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, current_code, huffman_codes):
   
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code

    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)


def huffman_coding(input_string):
    
    # Step 1: Count frequencies
    frequencies = defaultdict(int)
    for char in input_string:
        frequencies[char] += 1

    # Step 2: Build Huffman Tree
    root = build_huffman_tree(frequencies)

    # Step 3: Generate Huffman Codes
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    # Step 4: Encode the input string
    encoded_string = ''.join(huffman_codes[char] for char in input_string)

    return encoded_string

if __name__ == "__main__":
    input_string = input()
    encoded_string = huffman_coding(input_string)
    print(encoded_string)
