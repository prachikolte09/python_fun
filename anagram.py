from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
def_d = defaultdict(list)
for word in strs:
    sorted_word = ''.join(sorted(word))
    print(sorted_word)
    def_d[sorted_word].append(word)
    print(def_d)
print (list(def_d.values()))

print(15%3)

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(15)

