
def get_college_suggestion(marks_cet, marks_hsc):
    colleges = {
        "College of Engineering Pune": {"cet_cutoff": 97, "hsc_cutoff": 75},
        "Pune Institute of Computer Technology": {"cet_cutoff": 92, "hsc_cutoff": 70},
        "PES Modern College of Engineering": {"cet_cutoff": 85, "hsc_cutoff": 65},
        "Kk Wagh Institute of Engineering Education and Research ": {"cet_cutoff": 78, "hsc_cutoff": 60},
        "Sandip University": {"cet_cutoff": 65, "hsc_cutoff": 55}
    }
    
    suggestions = []
    
    for college, criteria in colleges.items():
        if marks_cet >= criteria["cet_cutoff"] and marks_hsc >= criteria["hsc_cutoff"]:
            suggestions.append(college)
    
    return suggestions


def main():
    
    print("Welcome to the College Suggestion Chatbot!")
    print("Please enter your marks obtained in CET and HSC to get college suggestions.")
    
    marks_cet = float(input("Marks in CET: "))
    marks_hsc = float(input("Marks in HSC: "))
    
    suggestions = get_college_suggestion(marks_cet, marks_hsc)
    
    if suggestions:
        print("Based on your marks, the suggested colleges are:")
        for college in suggestions:
            print(college)
    else:
        print("Sorry, based on your marks, we couldn't find any suitable colleges.")
    
    print("Thank you for using the College Suggestion Chatbot!")
    
if __name__ == "__main__":
    main()