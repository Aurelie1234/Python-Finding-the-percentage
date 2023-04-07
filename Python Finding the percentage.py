 for k, v in student_marks.items():
       if str(query_name) == k:
        print('{:.2f}'.format(sum(v) / len(v)))
