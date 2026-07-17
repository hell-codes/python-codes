
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
maths = float(input("Enter Mathematics marks: "))
pcm_avg = (physics + chemistry + maths) / 3
if pcm_avg >= 90:
    category = "Eligible for Engineering + Scholarship"
elif 75 <= pcm_avg <= 89:
    category = "Eligible for Engineering (self-finance)"
elif 60 <= pcm_avg <= 74:
    category = "Eligible for Arts/Science only"
else:
    category = "Not Eligible"
print("\n------ COLLEGE ADMISSION RESULT ------")
print(f"Physics   : {physics:.1f}")
print(f"Chemistry : {chemistry:.1f}")
print(f"Maths     : {maths:.1f}")
print(f"PCM Avg   : {pcm_avg:.2f}")
print(f"Category  : {category}")
