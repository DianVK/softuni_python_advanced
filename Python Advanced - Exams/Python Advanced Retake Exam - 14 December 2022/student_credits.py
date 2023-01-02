def students_credits(*args):
    result = ""
    student_info = {}
    total_credits = 0
    current_credit = 0
    for credit in args:
        course_name,credit_s,max_test_points,diyan_points = [int(x) if x.isdigit() else x for x in credit.split("-")]
        reached_points = (diyan_points / max_test_points) * 100
        current_credit = (credit_s * reached_points) / 100
        total_credits += current_credit
        student_info[course_name] = current_credit
    for course,student_credits in sorted(student_info.items(),key=lambda item: -item[1]):
        result += f"{course} - {student_credits:.1f}\n"
    if total_credits >= 240:
        return f"Diyan gets a diploma with {total_credits:.1f} credits.\n{result}"

    else:
        return f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.\n{result}"



print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
