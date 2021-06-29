from db import insert_stats

sequence = [
    'AAAA',
    'TTTT',
    'CCCC',
    'GGGG'
]


def is_mutant(dna_json, board, index):
    N, M = len(board), len(board[0])  # n*n - N = Rows, M = Columns
    dna = sequence[index]
    tracks = []
    # find words that start with the first letter of the sequence "Pistas"
    for i in range(N):
        for j in range(M):
            if board[i][j] == dna[0]:
                tracks.append((i, j, 0, {(i, j)}))

    # went through all the tracks
    while tracks:
        i, j, step, path = tracks.pop()
        step += 1
        # 4-letter pair, possible correct sequence
        if step == 4:
            list_x = []
            list_y = []
            # validar la coincidencia, solo horizontal, vertical y diagonal (izquierda, derecha)
            for key, value in path:
                list_x.append(key)
                list_y.append(value)
            len_list_x = len(set(list_x))
            len_list_y = len(set(list_y))
            # The match only exists when the list has length of (1 & 4), (4 & 1), (4 & 4)
            if (len_list_x == 1 and len_list_y == 4) or (len_list_x == 4 and len_list_y == 1) or (
                    len_list_x == 4 and len_list_y == 4):
                insert_stats(dna_json, 1, 0)
                return True

            # step to 0 and continue to the next loop value
            step = 0
            continue
        # 8 cardinal points for a possible sequence
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, -1), (1, 1), (-1, 1), (1, -1)
        ]

        # it is iterated starting from the track its possible 8 close values until a sequence of dna is found
        for ni, nj in [(i + x, j + y) for x, y in directions]:
            if (ni, nj) not in path and 0 <= ni < N and 0 <= nj < M and board[ni][nj] == dna[step]:
                tracks.append((ni, nj, step, path.union({(ni, nj)})))

    # recursion (n*4)
    index += 1
    if index <= 3:
        return is_mutant(dna_json, board, index)

    insert_stats(dna_json, 0, 1)
    return False
