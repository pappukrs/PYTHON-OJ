# import random;

# words = ['tree','sun','ball','moon','earth','grass','world'] 

# word = random.choice(words)
# print(word);
# print(random);

# random_number = random.randint(0,5);
# print(random_number);
# rand=random.random();
# print(rand);

import datetime;

x=datetime.datetime.now();
print("Year:",x.year);
print("Month:",x.month);
print("Day:",x.day);
print("Year:",x.year);
print(x.strftime("%A"));
 
y=datetime.datetime(2020,2,26);
print("y",y);
print(y.strftime("%Y"));
