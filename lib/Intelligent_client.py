from ast import Dict
from calendar import c
from typing import TypedDict
from zhipuai import ZhipuAI
import json
import re


class SummaryDict(TypedDict):
    content: str
    summary: str


class Intelligent_client:

    question_types = ["填空题", "简答题", "选择题", "判断题"]

    question_difficulties = ["简单", "中等", "困难"]

    result_format_prompts = [
        '''
        [
            {
                "question": "因特网的拓扑结构虽然非常复杂，并且在地理上覆盖了全球，但从其工作方式上看，可以划分为以下的两大块：$1 和 $2。",
                "answer": [
                    "客户端-服务器模式",
                    "对等网络模式"
                ],
                "difficulty": "中等"
            },
            {
                "question": "在因特网的拓扑结构中，$1 是指网络中的每个节点都与其他节点相连，形成一个没有中心节点的网络结构。",
                "answer": ["网状拓扑结构"],
                "difficulty": "简单"
            }
        ]
        ''',
        '''
        [
            {
                "question": "多态性的定义是什么？",
                "answer": "多态性是指允许不同类的对象对同一消息做出响应，即同一消息可以根据发送对象的不同而采用多种不同的行为方式。",
                "difficulty": "简单"
            },
            {
                "question": "多态性在面向对象编程中的作用是什么？",
                "answer": "多态性可以简化程序设计，提高代码的可重用性和可维护性。它允许通过基类指针或引用来调用派生类的方法，从而实现接口的通用性和灵活性，减少代码冗余，并且使得系统更加模块化和扩展性更强。",
                "difficulty": "中等"
            }
        ]
        ''',
        '''
        [
            {
                "question": "xxx",
                "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
                "answer": "A. xxx",
                "difficulty": "简单"
            },
            {
                "question": "xxx",
                "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
                "answer": "C. xxx",
                "difficulty": "简单"
            }
        ]
        ''',
        '''
        [
            {
                "question": "多态性允许不同类的对象对同一消息做出响应。",
                "answer": true,
                "difficulty": "简单"
            },
            {
                "question": "多态性增加了消息连接的复杂程度。",
                "answer": false,
                "difficulty": "简单"
            }
        ]

        '''
    ]

    special_example = '''
    在某些情况下，你可能会接触到形如'图1-7客户-服务器工作方式'文本，在这个总情况下，你所生成的题目不应该包含'图1-7'这样的内容，因为我们并没有给出这个图的具体内容，所以你需要根据文本的内容进行合理的推断。
    '''

    result_additional_prompts = [
        "$数字   这是给答案提供占位符，方便后续替换处理",
        "",
        "",
        ""
    ]

    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)


    '''
    knowledge:知识点,其格式如下:
        {
            "content":"xxxxx",
            "summary":"xxxxx"
        }
    q_type:题目类型:
        0:填空题
        1:简答题
        2:选择题
        3:判断题
    q_difficulty:题目难度:
        0:简单
        1:中等
        2:困难
    number:题目数量
    '''
    def generate_questions(self, knowledge: SummaryDict, q_type: int, q_difficulty: int, number: int):

        system_message = "你是一个高级教师，具备通过文本和对应知识点进行出题的能力，你有能力设计填空题、简答题、选择题和判断题。题目难度分为简单、中等和困难。这些题目应该涉及到给定的知识点，给出的答案应该在文本中涉及。"

        user_message = f"""
                文本：{knowledge['content']},
                知识点：{knowledge['summary']},
                {self.special_example}。
                根据给定的文本和知识点，设计{number}个{self.question_types[q_type]}，题目难度为{self.question_difficulties[q_difficulty]}，给出标准答案。
                """
        assistant_message = f"""
          给出的结果的形式应该是是json，{self.question_types[q_type]}的一个规范的示例如下:
              {self.result_format_prompts[q_type]}
              {self.result_additional_prompts[q_type]}
              给出的回答信息中，只需要json结果部分，不要涉及多余的话语。
              注意要好好参照示例的格式。
              结果中，question部分不要出现与题目难度相关的字样，difficulty部分要指明题目难度,answer部分要精炼准确。
              如果在给定的知识点中无法识别到有用的信息，或者知识点为'None'，请给出一个空的json数组。
        """

        tool_message = "对于部分知识点在文本中并没有涉及的情况，可以根据文本的内容进行合理的推断。"

        response = self.client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=[
                {"role": "system",
                 "content": system_message
                 },
                {"role": "user",
                 "content": user_message
                 },
                {"role": "assistant",
                 "content": assistant_message
                 },
                {"role": "tool",
                 "content": tool_message
                 },
            ],
        )

        content = response.choices[0].message.content

        return self.extract_json(content)

    def extract_json(self, text: str):
        json_pattern = re.compile(r'```json\s*(.*?)\s*```', re.DOTALL)
        json_matches = json_pattern.findall(text)
        if json_matches:
            try:
                json_data = json.loads(json_matches[0])
            except:
                json_data = []
        else:
            json_data = []
        return json_data
