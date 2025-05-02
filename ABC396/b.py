def main():
    q = int(input())
    queries = []
    deck = [0] * 100
    for _ in range(q):
        query = input().split()
        queries.append(query)

    for query in queries:
        if query[0] == "1":
            x = int(query[1])
            deck.append(x)
        elif query[0] == "2":
            x = deck.pop()
            print(x)


main()
