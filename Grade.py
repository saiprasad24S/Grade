project=int(input("Enter project marks"))
external=int(input("Enter external marks"))
internal=int(input("Enter internal marks"))
project_score = (70*project)/100
external_score = (20*external)/100
internal_score = (10*internal)/100
if project>=50 and external>=50 and internal >= 50:
    tot = project_score + external_score + internal_score
    print("total score is:",tot)
    if tot > 90:
        print("Grade A")
    elif 80 < tot <= 90:
        print("Grade B")
    elif 50 < tot < 80:
        print("Grade C")
else:
    if project < 50 :
        print("Fail in p",project)
    if external< 50 :
        print("Fail in e ",external)
    if internal < 50 :
        print("Fail in i",internal)
