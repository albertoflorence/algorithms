def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None

    count = 0

    for entry, exit in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None

        if entry <= target_time <= exit:
            count += 1

    return count
