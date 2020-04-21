sample = """
Betty Botter bought a bit of butter;

“But,” she said, “this butter's bitter!

If I put it in my batter

It will make my batter bitter.

But a bit o’ better butter

Will make my batter better.”

Then she bought a bit o’ butter

Better than the bitter butter,

Made her bitter batter better.

So ’twas better Betty Botter

Bought a bit o’ better butter.
"""
# The Jingle Book (1899)
word_count = dict()
for sentence in sample.split('\n'):
    for i in sentence.split():
        word = i.strip(", .“’”;!\n").lower()
        if(word in word_count):
            word_count[word] += 1
        else:
            word_count[word] = 1
for i in word_count:
    print(i + ":", word_count[i])