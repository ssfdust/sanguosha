# Copyright 2021 RedLotus <ssfdust@gmail.com>
# Author: RedLotus <ssfdust@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
此脚本用以生成以2013年标准版武将表为基础的武将选项

直接执行，将会从所有武将:中随机挑选三个，生成“主公”与“反贼”的武将牌
"""
from typing import List
import secrets

# 武将牌列表
HEROS = [
    "曹　操",
    "司马懿",
    "夏侯惇",
    "张　辽",
    "许　褚",
    "郭　嘉",
    "甄　姬",
    "刘　备",
    "关　羽",
    "张　飞",
    "诸葛亮",
    "赵　云",
    "马　超",
    "黄月英",
    "伊　籍",
    "孙　权",
    "甘　宁",
    "吕　蒙",
    "黄　盖",
    "周　瑜",
    "大　乔",
    "陆　逊",
    "孙尚香",
    "华　佗",
    "吕　布",
    "貂　蝉",
    "华　雄",
    "袁　术",
]


def random_pop(heros: List[str]) -> str:
    """随机从数组中pop一个对象"""
    hero = secrets.choice(heros)
    return heros.pop(heros.index(hero))


def main():
    """生成列表"""
    heros = HEROS.copy()
    for role in ["主公", "反贼"]:
        print(role)
        for i in range(3):
            print("\t{}".format(random_pop(heros)))


if __name__ == '__main__':
    main()
