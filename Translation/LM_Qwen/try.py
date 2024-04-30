from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import warnings
import torch
# 忽略所有警告
warnings.filterwarnings("ignore")

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-4B-Chat",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-4B-Chat")
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
prompt = "上文内容是："
print("控制台，如果输入exit则退出，输入clear则清楚历史记忆联想\n")
history="None"
response="None"
while True:
    input_query = input("请输入问题：\n")
    start_time = time.time()
    if input_query == "exit":
        break
    elif input_query == "clear":
        history = "None"
        response = "None"
        continue
    else:
        messages = [
            {"role": "system", "content":prompt+"问题"+history+"回答"+response },
            {"role": "user", "content": input_query}
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(device)

        generated_ids = model.generate(
            model_inputs.input_ids,
            max_new_tokens=1024*64
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        end_time = time.time()
        print(f"响应时间:{end_time - start_time :.2f}s")
        print(response+"\n")
        history = input_query