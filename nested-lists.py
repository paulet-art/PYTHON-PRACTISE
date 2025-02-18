if __name__ == '__main__':
    n = int(input())
    students = []
    
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])
        
    scores = [student[1] for student in students]
    unique_scores = sorted(set(scores))
    second_lowest = unique_scores[1]
        
    result = [student[0] for student in students if student[1] == second_lowest]
    result.sort()
        
    for name in result:
        print(name)
