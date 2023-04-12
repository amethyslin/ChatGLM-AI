from transformers import AutoTokenizer, AutoModel
import json5



with open("config.json",'r',encoding="utf-8",errors="ignore") as f:
    config = json5.loads(f.read())

def generate(title):
    prompt = config["prompt"].replace("[title]",title)
    max_length =config["max_length"]
    top_p = config["top_p"]
    temperature =config["temperature"]
    response, history = model.chat(tokenizer, prompt, history=[],max_length=max_length,top_p=top_p,temperature=temperature)
    print(response)


if  __name__ =="__main__" :
    tokenizer = AutoTokenizer.from_pretrained("chatglm-6b", trust_remote_code=True)
    if not config["quantize"]:
        model = AutoModel.from_pretrained("chatglm-6b", trust_remote_code=True).half().cuda()
    else:
        print("加载小内存运行")
        model = AutoModel.from_pretrained("chatglm-6b", trust_remote_code=True).quantize(config["quantize"]).half().cuda()
    model = model.eval()
    titleList = [title.rstrip() for title in open("./title.txt",encoding="utf8").readlines()]
    for title in titleList:
        generate(title)
