# 다중 클립보드 프로그램
import sys, pyperclip

TEXT = {'agree':"""Yes, I agree. That sounds fine to me.""", 
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('TEXT for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

