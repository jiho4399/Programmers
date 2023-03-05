def solution(elements):
    elements2 = elements * 2
    s = set()

    for i in range(len(elements)):
        for j in range(len(elements)):
            s.add(sum(elements2[j:j+i+1]))

    return len(s)