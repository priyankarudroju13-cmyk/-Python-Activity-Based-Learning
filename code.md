###1. University Scholarship Allocation

###1. Problem Statement

Design a system that evaluates applicants using aggregate marks, minimum subject marks, attendance, and
family-income criteria. It ranks eligible students and resolves ties using attendance.
Assumptions / Rules
Eligibility rules used in this example: aggregate marks ≥ 80, attendance ≥ 75%, minimum subject marks ≥ 60, and
annual family income ≤ ■2,50,000. Rank by aggregate marks (highest first), then attendance (highest first).


###2. Algorithm

1.Start.
2. Read the number of students.
3. For each student, read name, aggregate marks, attendance, minimum subject marks, and family income.
4. Check all four eligibility conditions.
5. If every condition is satisfied, add the student to the eligible list; otherwise mark the student as not eligible.
6. Sort eligible students by aggregate marks and then attendance, both in descending order.
7. Display eligible students with ranks and list students who are not eligible.
 8.Stop.

###3 Mermaid Flowchart Code
flowchart TD
1. A([Start]) --> B[/Enter student details/]
2. B --> C{Marks >= 80?}
3. C -->|No| H[Not Eligible]
 4.C -->|Yes| D{Attendance >= 75?}
5. D -->|No| H
6. D -->|Yes| E{Subject marks >= 60?}
7. E -->|No| H
8. E -->|Yes| F{Income <= 250000?}
9. F -->|No| H
10. F -->|Yes| G[Add to eligible list]
11. G --> I[Rank students]
12. H --> I
13. I --> J[/Display results/]
14. J --> K([Stop])
 
 ####4. Pseudocode<br>
1.START<br>
2.INPUT number_of_students<br>
3.eligible = empty list<br>
4.ineligible = empty list<br>
5.FOR each student<br>
6. INPUT name, aggregate, attendance, subject_min, income
 IF aggregate >= 80 AND attendance >= 75
 AND subject_min >= 60 AND income <= 250000
 ADD (name, aggregate, attendance) TO eligible<br>
7. ELSE<br>
8. ADD name TO ineligible<br>
9. END IF<br>
10.END FOR<br>
11.SORT eligible by aggregate descending,
 then attendance descending
 12.DISPLAY eligible students with ranks<br>
  13.DISPLAY ineligible students<br>
14.STOP

###5. Sample Input
Enter number of students: 3
Student 1: Ravi, marks 90, attendance 85,
subject marks 70, income 200000
Student 2: Priya, marks 85, attendance 90,
subject marks 65, income 150000
Student 3: Kumar, marks 70, attendance 80,
subject marks 65, income 100000

###6. Sample Output
Eligible Scholarship Students
1 Ravi 90.0 85.0
2 Priya 85.0 90.0
Not eligible: ['Kumar']


###7. Conclusion
The program checks scholarship eligibility using all specified conditions and ranks eligible students by aggregate
marks, using attendance to break ties.
