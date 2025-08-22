def get_num_words(a):
    with open(a) as f:
       b = f.read()
       return len(b.split())



def sort_on(items):
    return items["num"]


def get_num_forLetter(a):
    items = {}
    with open(a) as f:
        b = f.read()
        a = b.lower()
        for i in (range(len(a))):
            c = a[i]
            if c.isalpha():
                if c in items:
                    items[c] += 1
                else:
                    items[c] = 1

    return items

def topHigh_bottom_sorting(a):
    L = []
    c = list(a)
    for i in range(len(a)):
        
        L.append({"name":c[i],"num":a[c[i]]})
    L.sort(reverse=True, key=sort_on)
    for i in range(len(L)):
        b = L[i]
        print(f"{b['name']}: {b['num']}")

def bookBot(a): 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{a}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(a)} total words")
    print("--------- Character Count -------")
    topHigh_bottom_sorting(get_num_forLetter(a))
    print("============= END ===============")