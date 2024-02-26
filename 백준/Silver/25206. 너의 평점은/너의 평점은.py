major_score_sum = 0.0
score_sum = 0.0

for i in range(20) :
    subject_name, score, grade = input().split()

    if grade == 'P' :
        pass
    elif grade == 'A+' :
        major_score = float(score) * 4.5
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'A0' :
        major_score = float(score) * 4.0
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'B+' :
        major_score = float(score) * 3.5
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'B0' :
        major_score = float(score) * 3.0
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'C+' :
        major_score = float(score) * 2.5
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'C0' :
        major_score = float(score) * 2.0
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'D+' :
        major_score = float(score) * 1.5
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'D0' :
        major_score = float(score) * 1.0
        major_score_sum += major_score
        score_sum += float(score)
    elif grade == 'F' :
        major_score = float(score) * 0.0
        major_score_sum += major_score
        score_sum += float(score)

print(major_score_sum/score_sum)