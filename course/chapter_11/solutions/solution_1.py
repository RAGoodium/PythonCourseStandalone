name = input()
vote_count = {}
for vote in name.split():
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1
for name in vote_count:
    print(f'{name}: {vote_count[name]}')