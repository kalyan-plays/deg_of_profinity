##tweets.txt --> file with the list of tweets    
with open('tweets.txt') as f:
    words_list=[word for line in f for word in line.split()]
##profanity_words --> file with list of profanity words       
with open('profanity.txt') as f:
    profanity_words=[word for line in f for word in line.split()]
i = 0 ;
for w in words_list:
    if w in profanity_words:
        i = i + 1 ;

## deg of profanity is number of profine words by total words 

deg_of_prof = i / len(words_list)

print(deg_of_prof)


