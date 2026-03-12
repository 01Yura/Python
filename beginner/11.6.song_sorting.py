n = int(input())
songs = []
for i in range(n):
    songs.append(input())

songs.sort()
print(*songs, sep="\n")
