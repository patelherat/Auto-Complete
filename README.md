# Auto-Complete
Many of today's cell phones, text editors, and IDEs have an auto-complete feature. This feature attempts to complete the word for you using a list of known words to make suggestions.

<br />

Like with many auto-complete tools, you can cycle througth a list of possibe words with the given prefix. The system you will implement first sorts a list of words into lexicographic order. Given a prefix, it will make auto-complete suggestions starting with the first possible suggestion in the sorted list and - if asked - iterates through the list making further suggestions. When it reaches the last possible suggestions in the list it will restart back at the first suggestion.

<br />

Below is the example output of the auto-complete system:-
Given the file that contains one word per line:

baz <br />
test <br />
foo <br />
two <br />
zoo <br />
three <br />
bar <br />
fool <br />
dew <br />
duel <br />
guess <br />
baby <br />
boy <br />

Example program output: <br />

$ python3 auto_complete.py test.dic <br />
The sorted list: ['baby', 'bar', 'baz', 'boy', 'duel', 'few', 'foo', 'fool', 'guess', 'test', 'three', 'two', 'zoo'] <br />
Welcome to Auto-complete! <br />
Usage: Enter a prefix to auto-complete. <br />
Entering nothing will search for the next word with that prefix. <br />
Enter <QUIT> when asked for a prefix to exit. <br />
Enter a prefix to search for: app <br />
No match <br />
Enter a prefix to search for: ba <br />
baby <br />
Enter a prefix to search for: <br />
bar <br />
Enter a prefix to search for: f <br />
few <br />
Enter a prefix to search for: <QUIT> <br />
Exiting Auto-complete! Good bye.






