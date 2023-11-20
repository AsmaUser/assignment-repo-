Y= 10
tution = 10000
In = 0.05
#Calculate after 10 years
ten_year = float(tution * (1 + In)**Y)
#Total for 4 years
four_year = sum(
    float(tution * (1 + In)**(Y + i))
    for i in range(1, 5)
)
print ("Total cost of 10 years= ", ten_year)
print("Total cost of four year= ", four_year)