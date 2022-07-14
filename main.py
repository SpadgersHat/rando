from copy import copy
from random import randint
import time

draft1 = ['A-to-Markworthy Utd',
'Australia',
'Austria',
'Belarus',
'Belgium',
'Boys Name Bureaucrats',
'Canada',
'China',
'Czech Republic',
'Finland',
'France',
'Germany',
'Girls Name Geronimites',
'Great Britain',
'Hungary',
'Italy',
'Japan',
'Kazakhstan',
'Latvia',
'Liechtenstein',
'Marl-to-Z Wanderers',
'Netherlands',
'New Zealand',
'Norway',
'Poland',
'Russian Olympic Comittee',
'Slovakia',
'Slovenia',
'South Korea',
'Spain',
'Sweden',
'Switzerland',
'Ukraine',
'United States']

draft2 = [
'AG2R Citroën Team',
'Alpecin-Deceuninck',
'Astana Qazaqstan Team',
'B&B Hotels - KTM',
'Bahrain - Victorious',
'BORA - hansgrohe',
'Cofidis',
'EF Education-EasyPost',
'Groupama - FDJ',
'INEOS Grenadiers',
'Intermarché - Wanty - Gobert Matériaux',
'Israel - Premier Tech',
'Jumbo-Visma',
'Lotto Soudal',
'Movistar Team',
'Quick-Step Alpha Vinyl Team',
'Team Arkéa Samsic',
'Team BikeExchange - Jayco',
'Team DSM',
'TotalEnergies',
'Trek - Segafredo',
'UAE Team Emirates'
]

answers = {'yes_no': ['Absolutely.', 'Almost certainly.', 'If not, it will be soon.', 'For sure.', 'Fuck, no.',
                      'I guess.', 'NO!', 'Probably not, in my opinion.', "The fact that you're asking means it's yes.",
                      'Not on your nelly.', 'A hundred percent.', 'Our survey says...WANK WAAANK.', 'Who knows?',
                      'Yuuup.', "Doubt it.", "It's yes and no. Sorry to be so vague on this."],
           'which': ['The first one.', 'Go with your gut on this.', 'Same ones as last time.',
                     'The last, alphabetically.', 'The best one.', 'Close your eyes and point.', 'None of them.',
                     'All of them.'],
           'who': ['John Martin Francis McElroy.', 'Me, I guess.', 'Ivan. Obviously.', 'Got to be Charlie.',
                   "It's either Ike or nobody.", "Paul Scholes.", 'Weirdly, Gordon Brown?!',
                   "My assistant, Markus't Fr.", "Anyone wearing shorts.", 'Bees.', 'FUCKING MEEEE.', 'The Zionists.',
                   'The person in first place.', 'If in doubt, the Italians.'],
           'how': ['With great difficulty.', 'Look it up on WikiHow.', 'Fuck if I know.', 'Like a salmon.'],
           'the rest': ["Ask Ike, he knows those sorts of things.", "This really isn't my remit.",
                        "It's weird you'd even ask me that.", 'Never ask me that again.',
                        "You realise you're asking this to a random number generator, right?", "OMG. Pray more.",
                        "I honestly don't know.", "Now that's a question.", "Ask Ivan.", 'That makes no sense.',
                        'Can you rephrase that?', 'Seek help.',
                        "As a glorified magic 8 ball, I'm not sure what you expect from me here."],
           'why': ['Because it is!', "That's for Jesus to say.", "Because I said so.", "So that Ivan wins again.",
                   "Because in the end, we're all made of stars.", "No reason.", 'Blame the wealthy.'],
           'what': ["It's too complicated to explain.", "You wouldn't get it.", "That thing. You know.",
                    "It's a sex thing.", 'You had to be there.']}


def start():
    print("Hi there, I'm Rando's personal assistant, Markus't Fr.\nHe's pretty busy, but hopefully I can help.\n")
    while True:
        answer = input('''What do you want from him?
- Take part in the draft (d)
- Take part in an auction (a)
- Ask Rando for some tactical advice (4)\n''')
        if answer == 'd':
            draft(draft2)
        elif answer == 'a':
            auction()
        elif answer == '4':
            advice()
        else:
            print("I don't feel comfortable asking Rando to do that.")


def draft(this_draft):
    print('Oh, you want Rando to make draft picks? Cool, I guess.')
    current_list = copy(this_draft)
    while True:
        if len(current_list) == 0:
            print("Draft complete!")
            return
        answer = input('''
- Remove options (r)
- Make a pick (p)
- Back (b)\n''')
        if answer == 'b':
            print('Bye then...')
            return
        elif answer == 'r':
            current_list = remove_options(current_list)
            while True:
                if len(current_list) == 0:
                    break
                else:
                    answer = input('''
    - Remove another (r)
    - Back (b)\n''')
                    if answer == 'r':
                        current_list = remove_options(current_list)
                    elif answer == 'b':
                        break
        elif answer == 'p':
            current_list = pick(current_list)
        else:
            print("Wow, I don't know how Rando tolerates you guys.")


def remove_options(current_list):
    print('Available picks:\n')
    print_current_list(current_list)
    while True:
        answer = input('''- Type a number to remove that pick
- Back (b)\n''')
        if answer == 'b':
            break
        try:
            selection = int(answer)
            if int(answer) >= len(current_list):
                print("That pick isn't available, jackass.")
            else:
                print(f'Removing {current_list[selection]}')
                current_list.pop(selection)
                break
        except ValueError:
            print("No, a number.")
    return current_list


def pick(current_list):
    print("Rando is making a pick...")
    rando_selection = current_list.pop(randint(0, len(current_list)-1))
    print(f"Rando has selected {rando_selection}!")
    return current_list


def print_current_list(current_list):
    for x in range(len(current_list)):
        print(f'{x}: {current_list[x]}')


def auction():
    while True:
        answer = input("What's Rando's current BTC balance?\n")
        if test_for_money(answer):
            balance = int(answer)
            break
    while True:
        answer = input(f'''--Rando's balance: {balance} --
- Test if Rando wants to make a bid (t)
- Log a purchase (l)
- Finish auction (f)\n''')
        if answer == 't':
            bid_test(balance)
        elif answer == 'l':
            balance = change_balance(balance)
        elif answer == 'f':
            print("K cool.")
            return


def test_for_money(attempt):
    try:
        int(attempt)
        print("Gotcha.")
        return True
    except ValueError:
        print("That isn't a quantity, gentlemen.")
        return False


def change_balance(balance):
    while True:
        answer = input('How much did Rando spend?\n')
        if test_for_money(answer):
            break
    return balance-int(answer)


def bid_test(balance):
    while True:
        bid = input('Highest current bid:\n')
        if test_for_money(bid):
            break
    if int(bid) >= balance:
        print("Rando can't afford to raise the bid!")
        return balance
    while True:
        lots_remaining = input('Lots remaining (including this one)?\n')
        if test_for_money(lots_remaining):
            break
    lot_confidence = 1 / int(lots_remaining)
    wallet_confidence = 1 - int(bid) / balance
    print(f"""
Lot Confidence: {lot_confidence}
Wallet Confidence: {wallet_confidence}\n""")
    bid_decision = lot_confidence + wallet_confidence + (randint(1, 10)/20)
    if bid_decision >= 1.2:
        new_bid = decide_new_bid(int(bid), balance)
        print(f"Rando bids {new_bid}!")
    else:
        print("Rando withdraws from this lot.\n")


def decide_new_bid(current_bid, balance):
    increase = (current_bid * 0.1) + randint(-2, 5)
    if increase <= 0:
        increase = 1
    new_bid = int(current_bid + increase)
    if new_bid > balance:
        new_bid = balance
    return new_bid


def advice():
    print("I'm happy to pass on any questions you have:")
    while True:
        question = input("Your question:\n")
        if len(question) < 4:
            print("That's too short of a question to bother Rando with.")
        else:
            opening_slice = make_opening_slice(question)
            answer_type = find_answer_type(opening_slice)
            print("I'll ask him now. Hang on...")
            time.sleep(1)
            print(f"Right, Rando told me to tell you, '{answers[answer_type][randint(0, len(answers[answer_type])-1)]}'")
            answer = input('''
- Ask another (a)
- Go back (b)\n''')
            if answer == 'b':
                return
            elif answer == 'a':
                pass
            else:
                print("You fucking twat.")


def make_opening_slice(question):
    opening_slice = ""
    for x in range(3):
        opening_slice += question[x].lower()
    return opening_slice


def find_answer_type(text):
    yes_no_strings = ["is ", "wil", 'sho', 'did', 'do ', 'are', 'am ', 'can', 'if ']
    if text in yes_no_strings:
        return 'yes_no'
    elif text == 'who':
        return 'who'
    elif text == 'whi':
        return 'which'
    elif text == 'how':
        return 'how'
    elif text == 'why':
        return 'why'
    elif text == 'wha':
        return 'what'
    else:
        return 'the rest'

start()