from openie import StanfordOpenIE
import spacy
import re

nlp = spacy.load('en_core_web_lg') # or whatever model you have installed

with StanfordOpenIE() as client:
    with open('corpus/text', 'r', encoding='utf8') as r:
        corpus = r.read().replace('\n', ' ').replace('\r', '')
    
    doc = nlp(corpus)
    sentences = [sent.string.strip() for sent in doc.sents]

    for sentence in sentences:
        sentence = re.sub(r'\.(?=.*\.)', '', sentence)
        output = client.annotate(sentence, properties={"openie.format":"ollie", "openie.max_entailments_per_clause": 3 })
        print(output)
        # result = [output["sentences"] for item in output]
        # print(result)
        # for i in result:
        #     for rel in i:
        #         relationSent=rel['relation'],rel['subject'],rel['object']
        #         print(relationSent)