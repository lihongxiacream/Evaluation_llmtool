import json

with open("results/evaluation.jsonl", "r", encoding='utf-8') as f:
    records = json.load(f)

score_dict = {}
for record in records:
    score_dict[record['metric_zh']]=score_dict.get(record['metric_zh'],list())
    score_dict[record['metric_zh']].append(record['score'])

for metric in score_dict:
    print(metric)
    print(sum(score_dict[metric]) / len(score_dict[metric]))