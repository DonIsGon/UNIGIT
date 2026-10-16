import itertools

def calculate_dice_probabilities():
    # Alle möglichen Ergebnisse von zwei Würfeln
    # Jedes Ergebnis ist ein Tupel (Würfel1, Würfel2)
    all_outcomes = list(itertools.product(range(1, 7), repeat=2))
    total_outcomes = len(all_outcomes) # 36

    print(f"Gesamtzahl der möglichen Ergebnisse: {total_outcomes}\n")

    # 1. Es wird genau eine 4 gewürfelt.
    count_exactly_one_4 = 0
    for d1, d2 in all_outcomes:
        if (d1 == 4 and d2 != 4) or (d1 != 4 and d2 == 4):
            count_exactly_one_4 += 1
    prob_exactly_one_4 = count_exactly_one_4 / total_outcomes
    print(f"1. Wahrscheinlichkeit für 'genau eine 4': {count_exactly_one_4}/{total_outcomes} = {prob_exactly_one_4:.4f}")

    # 2. Es wird eine Summe 7 gewürfelt.
    count_sum_7 = 0
    for d1, d2 in all_outcomes:
        if d1 + d2 == 7:
            count_sum_7 += 1
    prob_sum_7 = count_sum_7 / total_outcomes
    print(f"2. Wahrscheinlichkeit für 'Summe 7': {count_sum_7}/{total_outcomes} = {prob_sum_7:.4f}")

    # 3. Es wird eine 3 oder eine 5 gewürfelt. (Mindestens eine 3 oder 5)
    count_at_least_one_3_or_5 = 0
    for d1, d2 in all_outcomes:
        if (d1 == 3 or d1 == 5) or (d2 == 3 or d2 == 5):
            count_at_least_one_3_or_5 += 1
    prob_at_least_one_3_or_5 = count_at_least_one_3_or_5 / total_outcomes
    print(f"3. Wahrscheinlichkeit für 'mindestens eine 3 oder 5': {count_at_least_one_3_or_5}/{total_outcomes} = {prob_at_least_one_3_or_5:.4f}")

    # 4. Es wird eine ungerade Augenzahl gewürfelt. (Mindestens eine ungerade Augenzahl)
    count_at_least_one_odd = 0
    for d1, d2 in all_outcomes:
        if (d1 % 2 != 0) or (d2 % 2 != 0):
            count_at_least_one_odd += 1
    prob_at_least_one_odd = count_at_least_one_odd / total_outcomes
    print(f"4. Wahrscheinlichkeit für 'mindestens eine ungerade Augenzahl': {count_at_least_one_odd}/{total_outcomes} = {prob_at_least_one_odd:.4f}")

calculate_dice_probabilities()
