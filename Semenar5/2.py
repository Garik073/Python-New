def max_to_min(list):
    Min = min(list)
    MAx = max(list)
    return [ Min if i == MAx else i for i in list ]
print(*max_to_min([int(i) for i in input().split()]))