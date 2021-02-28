def mastermind(u1, u2, u3, c1, c2, c3):
    user = [u1, u2, u3]
    correct = [c1, c2, c3]
    counts = {
        "b": user.count("b"),
        "w": user.count("w"), 
        "y": user.count("y")
    }

    score = 0
    for i in range(3):
        c = correct[i]
        
        if c == user[i]:
            score += 3
            user[i] = '-'
        elif c in user:
            counts[c] -= 1
            if counts[c] > -1:
                score += 1


    return score
