import pandas as pd


def create_data():
    d = [{"name": "超哥", "sex": "男", "course": "语文", "score": 90},
         {"name": "超哥", "sex": "男", "course": "数学", "score": 92},
         {"name": "超哥", "sex": "男", "course": "体育", "score": 100},

         {"name": "超人", "sex": "男", "course": "语文", "score": 93},
         {"name": "超人", "sex": "男", "course": "数学", "score": 96},
         {"name": "超人", "sex": "男", "course": "体育", "score": 120}
         ]
    df = pd.DataFrame(data=d)
    return df


def process():
    data = create_data()
    pass


if __name__ == '__main__':
    process()
