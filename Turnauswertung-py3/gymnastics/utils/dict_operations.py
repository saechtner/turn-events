
def completed_performances(disciplines_result_dict):
    results = 0
    for model_id, disicpline_result_dict in disciplines_result_dict.items():
        for discipline_key, discipline_result in disicpline_result_dict.items():
            if discipline_result and discipline_key is not 'total':
                results += 1
    return results