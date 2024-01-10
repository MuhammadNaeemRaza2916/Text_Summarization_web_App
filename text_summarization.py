import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# text = """In a surprising move, Samsung has officially canceled its in-person participation in the Mobile World Congress (MWC) 2021 event, opting for an online-only format. This decision comes amid ongoing global concerns related to the COVID-19 pandemic and reflects the company's commitment to prioritizing the health and safety of its employees, partners, and attendees.

# The tech giant had initially planned to showcase its latest innovations and technologies through a physical presence at MWC 2021, one of the most significant events in the mobile industry. However, with the evolving situation and uncertainties surrounding the pandemic, Samsung has chosen to pivot towards a virtual experience.

# The online-only format is expected to provide a comprehensive platform for Samsung to unveil its upcoming products, including the highly anticipated flagship smartphones, cutting-edge wearables, and advancements in other tech categories. Through this virtual approach, Samsung aims to reach a global audience, allowing tech enthusiasts, industry professionals, and consumers alike to participate in the event from the safety and comfort of their own spaces.

# Samsung's decision to embrace a digital platform aligns with the broader trend seen in the tech industry, where companies are increasingly leveraging virtual events to connect with their audiences. The move also reflects Samsung's adaptability and responsiveness to the changing landscape of events and conferences.

# While attendees will miss the hands-on experience and face-to-face interactions that are characteristic of in-person events, the online format opens up new possibilities for engagement. Samsung is expected to incorporate interactive elements, live streams, and virtual demonstrations to ensure an immersive and dynamic experience for participants.

# Industry analysts speculate that this shift to a virtual format may influence the future of tech events, even post-pandemic, as companies discover the benefits of reaching a wider audience through digital channels. Samsung's innovative approach to MWC 2021 marks a milestone in the evolving landscape of tech conferences, setting a precedent for other companies to consider alternative formats that blend the best of both physical and virtual worlds.

# As Samsung embraces the digital realm for MWC 2021, tech enthusiasts eagerly await the unveiling of the company's latest innovations and the unique experiences that the online event promises to deliver. Stay tuned for updates as Samsung reshapes the future of tech showcases in the wake of a changing global landscape."""

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)
    tokens = [token.text for token in doc]
    # print(tokens)

    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1   
            else:
                word_freq[word.text] += 1   

    # print(word_freq)

    max_freq = max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq  

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}

    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)

    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    # print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    # print("Text")
    # print(text)
    # print("Summmary")
    # print(summary)
    # print("length of original text ", len(text.split(' ')))
    # print("length of summary text ", len(summary.split(' ')))   

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))