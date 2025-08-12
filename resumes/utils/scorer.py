# def score_resume(text, keywords):
#     matched = []
#     clean_text = text.lower()
#     for kw in keywords:
#         if kw.lower() in clean_text:
#             matched.append(kw)
#     score = len(matched)
#     print("🎯 Matched keywords:", matched)
#     return score, matched
def score_resume(text, keywords):
    matched = [kw for kw in keywords if kw.lower() in text.lower()]
    score = len(matched) / len(keywords) * 100 if keywords else 0
    return round(score, 2), matched