# longestSubstring.py
# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    maxLen = 0
    trackingList = []

    for letter in s: 
        if letter in trackingList:
            trackingList = trackingList[trackingList.index(letter)+1:]
        trackingList.append(letter)
        maxLen = max(maxLen, len(trackingList))

    return maxLen

print( lengthOfLongestSubstring("pwwkew") )