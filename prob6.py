from time import time

f_math = open("Math.txt",'r')
f_korean = open("Korean.txt",'r')
f_english = open("English.txt",'r')

lines_math = f_math.readlines()
lines_korean = f_korean.readlines()
lines_english = f_english.readlines()

score = []
start_time = time()
for i in lines_english:
    line_split_en = i.split()
    for j in lines_korean:
        line_split_ko = j.split()
        for k in lines_math:            
            line_split_ma = k.split()
            if line_split_en[0] == line_split_ko[0] and line_split_en[0] == line_split_ma[0]:
                average = (int(line_split_en[1])+int(line_split_ko[1])+int(line_split_ma[1]))/3
                score.append([line_split_en[0], str(round(average,2))])
                
end_time = time()

for e in range(len(lines_english)):
    print(score[e])
    
print("실행시간:",end_time-start_time)