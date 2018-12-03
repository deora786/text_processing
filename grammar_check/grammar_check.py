import language_check

## importing language
tool = language_check.LanguageTool('en-US')

## text to check for grammatical errors
#text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
text = "the Cardinals did better then the Cubs"

## grammar error found in the given text
matches = tool.check(text)
print("Total errors: ", len(matches))


## correcting errors
correct_text = language_check.correct(text, matches)

print ("original text: ", text)
print ("corrected text: ", correct_text)

