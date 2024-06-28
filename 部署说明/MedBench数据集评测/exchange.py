import json
import sys
import os

def get_json_files_in_current_directory():
    json_files = []
    current_directory = os.getcwd()
    json_files = [file for file in os.listdir(current_directory) if file.endswith('.json')]
    return json_files

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    predictions = []
    for key, value in data.items():
        prediction = value.get('prediction', '').strip()
        predictions.append(prediction)
    return predictions

def find_matching_files(json_file):
    new_filename = json_file.replace("medbench-", "").replace(".json", "_test.jsonl")
    current_directory = os.getcwd()
    new_filepath = os.path.join(current_directory,'MedBench',new_filename)
    return new_filepath

def update_jsonl_file_with_predictions(jsonl_file, predictions):
    """
    更新 JSONL 文件中的 answer 字段。

    :param jsonl_file: JSONL 文件的路径。
    :param predictions: 预测结果列表。
    """
    updated_lines = []
    
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            json_obj = json.loads(line.strip())
            if i < len(predictions):
                json_obj['answer'] = predictions[i]
            updated_lines.append(json_obj)
    
    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for json_obj in updated_lines:
            f.write(json.dumps(json_obj, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    json_files = get_json_files_in_current_directory()
    print(json_files)

    for json_file in json_files:
        data = []
        predictions = read_json_file(json_file)

        matching_files = find_matching_files(json_file)

        if os.path.exists(matching_files):
            update_jsonl_file_with_predictions(matching_files,predictions)
            print(f"'{matching_files}'答案写入完成")

        else:
            print(f"File '{matching_files}' not found.")
