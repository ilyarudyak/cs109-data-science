features = ['1995', 'achievement', 'age', 'also', 'an', 'and', 'animated', 'animation', \
'appealing', 'be', 'bit', 'by', 'catalog', 'charm', 'comedy', 'computer', 'concept', 'could', \
'design', 'effect', 'engulfed', 'entertaining', 'equal', 'every', 'everyone', 'execution', \
'feature', 'film', 'for', 'generated', 'has', 'hyperrealist', 'in', 'ingenious', 'inventive', \
'it', 'its', 'most', 'of', 'on', 'postage', 'provocative', 'screen', 'sized', 'so', 'something', \
'spectrum', 'sports', 'stamp', 'still', 'story', 'technical', 'that', 'the', 'this', 'toy', 'watch', \
'winning', 'year', 'you']

text = 'So ingenious in concept design and execution that you could watch it on a postage \
stamp sized screen and still be engulfed by its charm'

x = []
text_split = text.lower().split()
for word in features:
    if word in text_split:
        x.append(1)
    else:
        x.append(0)

print(x)