
def IntervieweeScreening(min_experince, requred, **canidate_cv) : 
    
    for name, cv in canidate_cv.items() :
        
        if cv['experinces'] >= min_experince and set(requred).issubset(set(cv['Skills'])): 
            print(f'{name} is passed the interview')

def canidatecanidateCV() :
   
    canidate_cv = {}
   
        
    skills = []
    
    try : 
        
        name = input('Canidate\'s Name ? ').strip().capitalize() 
        experinces = int(input('candate\'s years of experinces ? ').strip())
        languges = int(input('amount of skills canidate has ? ').strip())
        
        for lang in range(languges) : 
            skill = input(f'canidate skill {lang+1} ? ').strip().capitalize()
            skills.append(skill)
        canidate_cv.update({name: {'experinces': experinces, 'Skills' : skills}})
        return canidate_cv
    except :
        
        print('something went wrong.') 
        
        
canidate_cv = canidatecanidateCV()
min_experinces = 3 
requred = ['Python', 'R', 'English', 'Communication']

IntervieweeScreening(min_experinces, requred, **canidate_cv)
 
  