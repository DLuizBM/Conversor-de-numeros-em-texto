
def format_output(million_final_phrase, thousand_final_phrase,
                  hundred_final_phrase, cents_final_phrase):
    
    final_phrase = ""
    if million_final_phrase:
        if not thousand_final_phrase and not hundred_final_phrase:
            final_phrase += million_final_phrase + "reais"
        else:
            final_phrase += million_final_phrase + " "

    if thousand_final_phrase:
        final_phrase += thousand_final_phrase + " "

    if hundred_final_phrase:
        if not len(million_final_phrase) and not len(thousand_final_phrase):
            if hundred_final_phrase == "um":
                final_phrase += hundred_final_phrase + " real"
            else:
                final_phrase += hundred_final_phrase + " "
        else:
            final_phrase += hundred_final_phrase + " "
    elif not len(million_final_phrase) and not len(thousand_final_phrase) and not len(hundred_final_phrase):
        final_phrase += "0 "

    if "reais" in final_phrase or "real" in final_phrase:
        pass
    else:
        final_phrase += "reais"

    if cents_final_phrase:
        final_phrase += " e " + cents_final_phrase

    return final_phrase
