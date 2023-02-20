def most_frequent(text):
    # create a dictionary to store the frequency of each letter
    freq = {}
    for letter in text:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    
    for letter, frequency in sorted_freq:
        print(f"{letter}: {frequency}")
