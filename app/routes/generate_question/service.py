from flask import jsonify, request, current_app
from werkzeug.utils import secure_filename
from . import generate_question
import json
import os


@generate_question.route('/extract', methods=['POST'])
def extract():
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'response.json')
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except Exception as e:
        data = {
            'error': 'Failed to extract data from response.json',
            'exception': str(e)
        }
    return data


@generate_question.route('/web_modify_graph', methods=['POST'])
def web_modify_graph():
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'result.json')
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except Exception as e:
        data = {
            'error': 'Failed to modify data in response.json',
            'exception': str(e)
        }
    return data

# 生成题目


@generate_question.route('/exam_item', methods=['POST'])
def generate():
    return '嘿嘿'


# 文件上传
@generate_question.route('/upload', methods=['POST'])
def upload():
    # 上传模式
    '''
    三种模式：
    1. single：单文件直接上传，说明是小文件
    2. slice：大文件分片上传，需要合并
    3. merge：合并文件块，最后合并文件
    '''
    mode = request.form.get('mode')
    if (mode == "single"):
        # 处理标题
        headings = request.form['headings']

        print(headings)
        file = request.files['file']
        # 保存文件
        file.save(os.path.join(
            current_app.config['BASE_DIR'], 'uploads', file.filename))
        return jsonify({"message": "File uploaded and merged successfully!"}), 200
    elif (mode == "slice"):
        chunk_index = int(request.form['chunk_index'])
        chunk_count = int(request.form['chunk_count'])
        file_id = request.form['file_id']
        chunk_folder = os.path.join(
            current_app.config['BASE_DIR'], 'chunks', file_id)
        # 如果对应文件块已经存在，直接返回
        if os.path.exists(os.path.join(chunk_folder, f"{file_id}_{chunk_index}.part")):
            return jsonify({"message": f"Chunk already exists! Remaining {chunk_count-1-chunk_index} chunks"}), 200
        else:
            chunk_data = request.files['chunk_data']
            os.makedirs(chunk_folder, exist_ok=True)

            chunk_filename = secure_filename(f"{file_id}_{chunk_index}.part")
            chunk_filepath = os.path.join(chunk_folder, chunk_filename)

            # 保存文件块
            chunk_data.save(chunk_filepath)

            return jsonify({"message": f"Chunk uploaded and merged successfully! Remaining {chunk_count-1-chunk_index} chunks"}), 200
    else:
        # 合并文件
        file_id = request.form['file_id']
        filename = request.form['filename']
        chunks = request.form['chunks']

        # 处理标题
        headings = request.form['headings']

        chunk_folder = os.path.join(
            current_app.config['BASE_DIR'], 'chunks', file_id)
        final_filepath = os.path.join(
            current_app.config['BASE_DIR'], 'uploads', f"{file_id}-{filename}")
        with open(final_filepath, 'wb') as final_file:
            for i in range(int(chunks)):
                chunk_filename = secure_filename(f"{file_id}_{i}.part")
                chunk_filepath = os.path.join(chunk_folder, chunk_filename)
                with open(chunk_filepath, 'rb') as chunk_file:
                    final_file.write(chunk_file.read())
        # 删除块文件和临时目录
        for chunk_file in os.listdir(chunk_folder):
            os.remove(os.path.join(chunk_folder, chunk_file))
        os.rmdir(chunk_folder)
        return jsonify({"message": "File uploaded successfully!"}), 200
