from itertools import permutations


def perm(size):
    for i in range(0, size+1):
        l = list()
        for j in range(0, i):
            l.append('C')
        for j in range(i, size):
            l.append('J')
        for p in set(permutations(l, size)):
            yield p


def get_score(x, y, seq):
    sum = 0
    for i in range(0, len(seq)-1):
        if seq[i] == "C" and seq[i+1] == "J":
            sum += x
        if seq[i] == "J" and seq[i+1] == "C":
            sum += y
    return sum


def solve(x, y, seq):
    best_seq_map = {}

    while "?" in seq:
        i = 0
        qms = ""
        _con = True
        while i < len(seq) and _con == True and qms.count("?") < 4:
            if seq[i] == "?":
                if len(qms) == 0 and i > 0:
                    qms += seq[i-1]
                qms += seq[i]
            else:
                if len(qms) > 0:
                    qms += seq[i]
                    _con = False
            i += 1

        if not qms:
            continue

        qm_indexes = list()
        for j in range(0, len(qms)):
            if qms[j] == "?":
                qm_indexes.append(j)

        best_score = None
        best_seq = None
        for p in perm(len(qm_indexes)):
            qms_arr = list(qms)
            for j in range(0, len(p)):
                qms_arr[qm_indexes[j]] = p[j]
            score = get_score(x, y, qms_arr)
            if best_seq is None or score < best_score:
                best_score = score
                best_seq = qms_arr
        best_seq_str = "".join(best_seq)
        best_seq_map[qms] = best_seq_str
        #print(qms, best_seq_str)

        reps = -1
        while reps != 0:
            reps = 0
            for best_seq in best_seq_map:
                new_seq = seq.replace(best_seq, best_seq_map[best_seq])
                if new_seq != seq:
                    reps += 1
                    seq = new_seq

    score = get_score(x, y, seq)
    return score, seq


t = int(input())
for i in range(1, t + 1):
    x, y, seq = [s for s in input().split(" ")]
    solution, _ = solve(int(x), int(y), seq)
    print("Case #{}: {}".format(i, solution))
