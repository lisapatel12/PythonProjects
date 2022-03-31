#Lisa Patel (Driver)(U50140470) Naman Wadhwa (Navigator)(U98636423)

#create a tuple
Courses= ('COP 2510', 'EGN 3000L', 'MAC 2281', 'MUH 3016', 'PHY 2048')

#create the first dictionary
Course_Name= {'COP 2510' : 'Programming Concepts' , 'EGN 3000L' : 'Foundations of Engineering Lab' , 'MAC 2281' : 'Calculus 1' , 'MUH 3016' : 'Survey of Jazz' , 'PHY 2048' : 'General Physics 1'}

#create the second dictionary
Instructor = {'COP 2510' : 'S. Small', 'EGN 3000L' : 'J. Anderson', 'MAC 2281' : 'A. Makaryus', 'MUH 3016' : 'A. Wilkins', 'PHY 2048' : 'G. Pradhan'}

#create the third dictionary
Class_Times= {'COP 2510' : 'MW 12:30pm - 1:45pm', 'EGN 3000L' : 'TR 11:00am - 12:15 pm', 'MAC 2281' : 'MW 9:30am - 10:45am', 'MUH 3016' : 'online asynchronous', 'PHY 2048' : 'TR 5:00pm - 6:15pm'}

#display the course details depnding on course number selected
c= input('Enter a course number : ')

if c in Courses:
    print ('The course details are: ')
    print('Course Name:',Course_Name [c])
    print('Instructor:',Instructor[c])
    print('Class Times:',Class_Times [c])
else:
    print(c, 'is an invaild course number.')
