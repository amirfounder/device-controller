import time

from device_controller.browser import Browser


QUESTIONS = [
    "Where's the next place you want to visit?",
    "What's the most difficult thing about being you?",
    "Is there a part of your culture that you don't like?",
    "What's your current Golden Rule when it comes to living life?",
    "Is there a personality trait that you'd like to adopt from one of your friends?",
    "What has been your 15 minutes of fame up to this point?",
    "If you knew the winning lottery numbers, would you keep them to yourself or share with others?",
    "What's something that you find difficult, but you think in your mind it should be easy?",
    "If you could only ask one question to each person you meet, what would that question be?",
    "What uncommon thing would you like to see become more common?",
    "What's the best compliment you ever received?",
    "Is it better to read books in electronic form or actually hold the book?",
    "How long does it take you to form an opinion about a person?",
    "What do you try to do to make the world a little better?",
    "What's your plan for surviving a zombie invasion?",
    "How often do you find yourself daydreaming?",
    "What's something that was completely out-of-character that you did?",
    "What food do you have a love-hate relationship with?",
    "What is the next thing you have on your to-buy list?",
    "What line from a song has had the biggest impact on you?",
    "What part of your body currently doesn't feel 100%?",
    "What or who are you always willing to make time for?",
    "If you had to wear a hat for the next week, what type of hat would you choose?",
    "Of all the things you've bought in your life, what has been the worst purchase?",
    "If you had to change the language you speak, which one would you choose?",
    "If you had the opportunity to look through someone's email without them knowing, would you?",
    "If everyone here was a color, what color would each person be?",
    "What's something that you know that few other people know?",
    "Where do you see yourself in 5 years?",
    "What was the unspoken scandal in your town when growing up?",
    "If you had to ask yourself one question to get the most information out of you, what would that question be?",
    "What does it mean to \"live a good life\" in your opinion?",
    "How do you make decisions?",
    "If you could lock someone up and throw away the key, would you and if so, who would that be?",
    "What do you consider the best decision you've made thus far in your life?",
    "If you could choose the way you became a hero, what would the circumstances be?",
    "If you had an extra hour a day that had to be allocated to one specific purpose, how would you use it?",
    "What was a past passion that you can't believe you were so passionate about?",
    "Is time currently passing quickly or slowly for you?",
    "What was your last \"ah-ha\" moment?",
    "What's the last thing that you gave up on? Are you happy or disappointed?",
    "Does your family have any weird traditions?",
    "When are you most productive?",
    "What are you currently doubting in your life?",
    "What law have you broken the most in your life?",
    "What do you think is the most useful skill to know?",
    "What's your close call story?",
    "Are you currently going through any type of phase?",
    "What's something about you today that the old you would find surprising?",
    "Would the world be better or worse if superheroes existed?"
]


if __name__ == '__main__':
    browser = Browser()
    for q in QUESTIONS[:20]:
        browser.search_google(q)
    time.sleep(10)
    for q in QUESTIONS[21: 40]:
        browser.search_google(q)
    time.sleep(10)
    for q in QUESTIONS[41:]:
        browser.search_google(q)
