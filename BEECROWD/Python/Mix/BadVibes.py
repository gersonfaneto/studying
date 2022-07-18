nLines, nColumns = map(int, input().split())

lifeProblems = []
collegeProblems = []
for i in range(nLines):
    line = input().split()
    for item in line:
        if item[1] == "V":
            lifeProblems.append(item)
        else:
            collegeProblems.append(item)

print("\n".join(sorted(lifeProblems, reverse = True)))
print("\n".join(sorted(collegeProblems, reverse = True)))
