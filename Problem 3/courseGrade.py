def courseGrade():
    
    def assign_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
 # 
   
        filename = input("Enter the name of the tsv file: ")

    # Open the file and read the lines
        with open(filename, 'r') as f:
            lines = f.readlines()

    # Split each line into a list of values
        students = [line.strip().split('\t') for line in lines]

    # Initialize an empty list for the report and total scores for each test
        report = []
        midterm1_total = midterm2_total = final_total = 0

    # Loop through each student
        for student in students:
            # Unpack the student information
            last_name, first_name, midterm1, midterm2, final = student
            # Convert scores to integers
            midterm1, midterm2, final = int(midterm1), int(midterm2), int(final)
            # Compute the average score
            average = (midterm1 + midterm2 + final) / 3
            # Assign a letter grade based on the average score
            grade = assign_grade(average)
            # Add the student's information to the report
            report.append(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n")
            # Add the scores to the total scores
            midterm1_total += midterm1
            midterm2_total += midterm2
            final_total += final

        # Compute the average score for each test
        midterm1_avg = midterm1_total / len(students)
        midterm2_avg = midterm2_total / len(students)
        final_avg = final_total / len(students)

        # Add the average scores to the report
        report.append(f"Averages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")

        # Write the report to a file
        with open('report.txt', 'w') as f:
            f.writelines(report)

if __name__ == "__main__":
    courseGrade()
    
    