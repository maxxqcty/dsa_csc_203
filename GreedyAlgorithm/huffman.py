import heapq

class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def print_codes(self, root, code, huffman_codes, code_lengths):
        if not root:
            return

        if root.data != '$':
            huffman_codes[root.data] = code
            code_lengths[root.data] = len(code)

        self.print_codes(root.left, code + "0", huffman_codes, code_lengths)
        self.print_codes(root.right, code + "1", huffman_codes, code_lengths)

    def display_table(self, chars, freqs, huffman_codes, code_lengths):
        print("+-----------+-----------+----------------+----------------+----------------+")
        print("| Character | Frequency | Huffman Code   | Original Bits  | Encoded Bits   |")
        print("+-----------+-----------+----------------+----------------+----------------+")
        
        total_bits = 0
        initial_bits = 0

        for ch, freq in zip(chars, freqs):
            original_bits = 8 * freq  # Assuming 8 bits for the original character
            encoded_bits = freq * code_lengths.get(ch, 0)  # Length of the Huffman code

            print(f"| {ch:<9} | {freq:<9} | {huffman_codes.get(ch, '-'): <14} | {original_bits:<14} | {encoded_bits:<14} |")
            initial_bits += original_bits
            total_bits += encoded_bits

        print("+-----------+-----------+----------------+----------------+----------------+")
        print(f"| {'Total':<38} | {initial_bits:<14} | {total_bits:<14} |")
        print("+-----------+-----------+----------------+----------------+----------------+")

    def run_huffman_coding(self):
        n = int(input("Enter the number of characters: "))
        chars = []
        freqs = []

        # Collecting characters and frequencies separately
        for i in range(n):
            char = input(f"Enter character {i + 1}: ")
            freq = int(input(f"Frequency for'{char}': "))
            chars.append(char)
            freqs.append(freq)

        # Building the Huffman tree
        min_heap = [Node(chars[i], freqs[i]) for i in range(n)]
        heapq.heapify(min_heap)

        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)
            right = heapq.heappop(min_heap)
            top = Node('$', left.freq + right.freq)
            top.left = left
            top.right = right
            heapq.heappush(min_heap, top)

        huffman_codes = {}
        code_lengths = {}
        self.print_codes(min_heap[0], "", huffman_codes, code_lengths)

        # Display the final results
        self.display_table(chars, freqs, huffman_codes, code_lengths)

# Run the Huffman Coding program
def run_huff():
    huffman_coding = HuffmanCoding()
    huffman_coding.run_huffman_coding()

if __name__ == "__main__":
    run_huff()

# -----------------------------------------------------------
# OUTPUT :

# Enter the number of characters: 9
# Enter character 1: g
# Frequency for'g': 5
# Enter character 2: o
# Frequency for'o': 10
# Enter character 3: 0
# Frequency for'0': 15
# Enter character 4: d
# Frequency for'd': 7
# Enter character 5: l
# Frequency for'l': 8
# Enter character 6: u
# Frequency for'u': 9
# Enter character 7: c
# Frequency for'c': 4
# Enter character 8: k
# Frequency for'k': 8
# Enter character 9: !
# Frequency for'!': 9
# +-----------+-----------+----------------+----------------+----------------+
# | Character | Frequency | Huffman Code   | Original Bits  | Encoded Bits   |
# +-----------+-----------+----------------+----------------+----------------+
# | g         | 5         | 1011           | 40             | 20             |
# | o         | 10        | 110            | 80             | 30             |
# | 0         | 15        | 00             | 120            | 30             |
# | d         | 7         | 1110           | 56             | 28             |
# | l         | 8         | 1111           | 64             | 32             |
# | u         | 9         | 011            | 72             | 27             |
# | c         | 4         | 1010           | 32             | 16             |
# | k         | 8         | 010            | 64             | 24             |
# | !         | 9         | 100            | 72             | 27             |
# +-----------+-----------+----------------+----------------+----------------+
# | Total                                  | 600            | 234            |
# +-----------+-----------+----------------+----------------+----------------+

