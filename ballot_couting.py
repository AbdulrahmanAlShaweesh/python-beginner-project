

# this function use to get the total number of people
# who are going to vote in this elections.
# this should be exntered by the admin.
def getPeopleVotes():

    while True:
        try:
            n_people_voted = int(input(
                'enter the total numbers of people voted ? ').strip())
            return n_people_voted
        except:
            print('please enter a digits only.')

# this function used to get the vots canindate,
# will ask the vots partipate to slecte on canidate and store
# the data into a list.


def collect_people_votes(canidates_vots, canidates_name, genders):
    print('*' * 50)
    print('welcome to vote election system'.center(50, ' '))
    print('*' * 50)
    people_voted = getPeopleVotes()
    for vote in range(people_voted):
        # vote particpate info and to who hi/she going to vot for
        gender = input(
            'ender your gender (male/female) ? ').strip().lower()
        vote_name = input('enter your name ? ').strip().capitalize()
        people_vot = input(
            f'{"Mr" if gender == "male" else "Ms"}.{vote_name} who do you want to vots for (Ben/Andy/Canel) only one caniadate allowed ? ').strip().capitalize()

        # chech if particapte info correct and canidate info correct or not.
        while people_vot not in canidates_name or gender not in genders:
            if people_vot not in canidates_name:
                people_vot = input(
                    f'pleas enter valid canidate (Ben/Andy/Canel) only one caniadate allowed ? '
                ).strip().capitalize()

            elif people_vot not in canidates_name and gender not in genders:
                gender = input(
                    'ender your gender (male/female) ? ').strip().lower()
                people_vot = input(
                    f'pleas enter your valid gender and valid canidate (Ben/Andy/Canel) only one caniadate allowed ? '
                ).strip().capitalize()

            else:
                gender = input(
                    'invalid gender name only (male/female)? '
                ).strip().lower()
        print('*' * 50)
        # the particpate vote will be store into the list if his/her input are valid.
        canidates_vots.append(people_vot)
    return canidates_vots


canidates_name = ['Ben', 'Andy', 'Canel']
genders = ['male', 'female']
canidates_vots = []


# this function used to get who is the winer.
def get_winers(canidates, votes):
    people_vots = collect_people_votes(canidates_vots, canidates_name, genders)

    for person in people_vots:
        if person not in canidates:
            canidates.append(person)
            votes.append(1)
        else:
            canidate_index = canidates.index(person)
            votes[canidate_index] += 1
    return votes, canidates


def display_winer():
    canidates = []
    votes = []
    votes, canidate = get_winers(canidates, votes)
    if 'Andy' not in canidates:
        for i in range(len(votes)):
            print(f'{canidates[i]} : {votes[i]}')
        print('Andy : 0')

    elif 'Ben' not in canidates:
        for i in range(len(votes)):
            print(f'{canidate[i]} : {votes[i]}')
        print('Ben : 0')
    else:
        for i in range(len(canidate)):
            print(f'{canidate[i]} : {votes[i]}')
        print('Canel : 0')
    winer_index = votes.index(max(votes))
    print(f'The winer is {canidate[winer_index]} got {max(votes)} votes.')


display_winer()
