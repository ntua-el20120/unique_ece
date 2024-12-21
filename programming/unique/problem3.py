import os

'''  
Εκφώνηση:
Γράψτε ένα πρόγραμμα που παίρνει έναν θετικό φυσικό αριθμό Ν και θα επιστρέφει
την μεγαλύτερη δύναμη του 2 που διαιρεί το Ν.

Παραδείγματα:
32 -> 5
2016 -> 5
999999 -> 0
'''


def solution(n):
    result = 0
    ''' Γράψε τον κώδικά σου εδώ. Πρόσεχε την στοίχιση! '''
    ''' Το solution(n) σημαίνει ότι μπορείς να χρησιμοποιήσεις το n όπου θέλεις μέσα στη συνάρτηση. Άλλαξέ το αν χρειάζεται'''
    



    ''' Όπως και αν το έλυσες, βάλε το αποτέλεσμα στη μεταβλητή result πριν από εδώ'''
    return result

'''Υπάρχουν hints στο τέλος του κώδικα'''

# Αν δεν σου βγαίνει με τίποτα, αντίγραψε όλο το από πάνω στο ChatGPT.
# Και εμείς αυτό κάνουμε όταν τα βρίσκουμε σκούρα!! :D

''' 
Μην πειράξεις τίποτα από εδώ και κάτω
'''
if __name__ == "__main__":
    # Εξηγούμε τον παρακάτω κώδικα για όποιον βαριέται
    # Έχουμε 3 αρχεία που μας ενδιαφέρουν: το παρον αρχείο κώδικα, το αρχείο με τα testcases και το αρχείο με τα αποτελέσματα
    # ξέρουμε πού βρίσκονται το ένα σε σχέση με το άλλο
    # uniqe ----> testcases ----> input.txt
    #       |              |----> output.txt
    #       |----> problem.py
    # Ο κώδικας μπορεί να τρέξει από οποιοδήποτε φάκελο στον υπολογίστη οπότε για να ανοίξουμε τα αρχεία σωστά πρέπει να κατασκευάσουμε το μονοπάτι 
    # που θα ακολουθήσει ο υπολογιστής για να βρει τα αρχεία

    # Βρίσκουμε το μονοπάτι του κώδικα
    path = os.path.abspath(__file__)

    # βάσει του σχήματος παραπάνω, μπορούμε βρούμε το μονοπάτι του φακέλου με τα testcases
    test_path = os.path.join(os.path.dirname(path), "testcases")
    
    # ανοίγουμε το αρχείο με τα testcases
    with open(os.path.join(test_path, "input3.txt"), "r") as f:
        lines = f.readlines() # αυτό μας επιστρέφει μια λίστα με όλες τις γραμμές του αρχείου
        
        # αντί για κείμενο θέλουμε να έχουμε αριθμούς. Ο υπολογιστής καταλαβαίνει τον αριθμό 1
        # διαφορετικά από το κείμενο "1". Οπότε μετατρέπουμε το κείμενο σε αριθμούς
        # int -> integer -> ακέραιος
        inputs = [int(line) for line in lines] 

        # Τρέχουμε τη συνάρτηση λύσης για κάθε αριθμό στη λίστα και βάζουμε τα αποτελέσματα σε μια λίστα
        results = [solution(n) for n in inputs]
    

    # τώρα θα ανοίξουμε το αρχείο με τα αποτελέσματα για να συγκρίνουμε τα αποτελέσματα με τα αναμενόμενα
    with open(os.path.join(test_path, "output3.txt"), "r") as f:
        # επαναλαμβάνουμε την προηγούμενη διαδικασία
        lines = f.readlines()
        expected = [int(line) for line in lines]
    
    # Συγκρίνουμε τα αποτελέσματα με τα αναμενόμενα
    all_good = True
    for i, (r, e) in enumerate(zip(results, expected)):
        if r != e:
            print(f"Test case {i+1} failed: expected {e}, got {r}")
            all_good = False
    if all_good:
        print("All test cases passed!")

'''
Hint 1:
Αφού δεν ξέρουμε πόσες φορές διαιρείται το Ν με το 2 θα χρειαστούμε το while loop
Ποια θα είναι η συνθήκη του while loop;
Τι θα γίνεται μέσα στο while loop;
Πώς θα κρατάμε το αποτέλεσμα;
'''

'''
Hint 2:
Λογικά θα χρειαστείς μια μεταβλητή για να κρατάς το αποτέλεσμα
'''

'''
Hint 3:
To loop θα πρέπει να τρέχει όσο το Ν διαιρείται με το 2 (το ελέγχουμε από το υπόλοιπο %)
while n % 2 == 0:
'''

'''
Hint 4:
Μέσα στο loop μπορούμε να αυξήσουμε το counter και να διαιρέσουμε το Ν με το 2
'''