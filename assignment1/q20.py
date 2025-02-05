"""A university has the following rules for a student to qualify for a degree with A as the
main subject and B as the subsidiary subject:
(a) He should get 55 percent or more in A and 45 percent or more in B.
(b) If he gets less than 55 percent in A he should get 55 percent or more in B. However, he
should get at least 45 percent in A.
(c) If he gets less than 45 percent in B and 65 percent or more in A he can reappear in an
examination in B to qualify.
(d) In all other cases he is declared to have failed.
Write a program to receive marks in A and B and Output whether the student has passed, failed
or can reappear in B."""


marks_A=int(input("Enter marks in subject A"))
marks_B=int(input("Enter marks in subject B"))

if (marks_A>=55) and (marks_B>=45):
    print("Passed")
elif (45<=marks_A<55) and (marks_B>=55):
    print("Passed")
elif (marks_A>=65) and (marks_B<45):
    print("Reappear in B")
else:
    print("Failed")