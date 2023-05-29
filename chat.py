# Define a dictionary of colleges and their admission criteria
colleges = {
    'College A': {
        'cet_cutoff': 90,
        'hsc_cutoff': 80,
        'branch': 'Engineering',
        'location': 'Nashik',
        'fee': 50000
    },
    'College B': {
        'cet_cutoff': 90,
        'hsc_cutoff': 80,
        'branch': 'Engineering',
        'location': 'Pune',
        'fee': 50000
    },
    'College C': {
        'cet_cutoff': 90,
        'hsc_cutoff': 80,
        'branch': 'Engineering',
        'location': 'Mumbai',
        'fee': 50000
    },
    'College D': {
        'cet_cutoff': 85,
        'hsc_cutoff': 75,
        'branch': 'Medicine',
        'location': 'Nashik',
        'fee': 80000
    },
    'College E': {
        'cet_cutoff': 85,
        'hsc_cutoff': 75,
        'branch': 'Medicine',
        'location': 'Pune',
        'fee': 80000
    },
    'College F': {
        'cet_cutoff': 85,
        'hsc_cutoff': 75,
        'branch': 'Medicine',
        'location': 'Mumbai',
        'fee': 80000
    },
    'College G': {
        'cet_cutoff': 80,
        'hsc_cutoff': 70,
        'branch': 'Arts',
        'location': 'Nashik',
        'fee': 30000
    },
    'College H': {
        'cet_cutoff': 80,
        'hsc_cutoff': 70,
        'branch': 'Arts',
        'location': 'Pune',
        'fee': 30000
    },
    'College I': {
        'cet_cutoff': 80,
        'hsc_cutoff': 70,
        'branch': 'Arts',
        'location': 'Mumbai',
        'fee': 30000
    }
}

# Function to determine the suitable college based on marks and preferences
def choose_college(cet_marks, hsc_marks, branch=None, location=None):
    suitable_colleges = []
    for college, criteria in colleges.items():
        if cet_marks >= criteria['cet_cutoff'] and hsc_marks >= criteria['hsc_cutoff']:
            if branch and branch.lower() != criteria['branch'].lower():
                continue
            if location and location.lower() != criteria['location'].lower():
                continue
            suitable_colleges.append(college)
    return suitable_colleges

# Main interaction loop
while True:
    print('----- Welcome to College Selection Chatbot -----')
    print('Enter your CET marks (-1 to exit):')
    cet_marks = float(input())
    
    if cet_marks == -1:
        break
    
    print('Enter your HSC marks:')
    hsc_marks = float(input())
    
    print('Enter your preferred branch (optional):')
    branch = input()
    
    print('Enter your preferred location (optional):')
    location = input()
    
    suitable_colleges = choose_college(cet_marks, hsc_marks, branch, location)
    
    if len(suitable_colleges) == 0:
        print('No suitable colleges found based on your criteria.')
    else:
        print('Suitable colleges based on your criteria:')
        for college in suitable_colleges:
            print('College:', college)
            print('Branch:', colleges[college]['branch'])
            print('Location:', colleges[college]['location'])
            print('Fee:', colleges[college]['fee'])
            print()
    
    print()