def solution(players, callings):
    for name in callings:
        for idx, player in enumerate(players):
            if name == player:
                players[idx], players[idx - 1] = players[idx - 1], players[idx]

    answer = players
    return answer

