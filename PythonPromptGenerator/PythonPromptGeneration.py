import random
import os
import random
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    TextDataset, DataCollatorForLanguageModeling,
    Trainer, TrainingArguments
)
import datasets
# import google.colab
# from google.colab import files
datasets.disable_caching()


#@title 1.3 Generate prompts!

#@markdown _What?! A prompt for my prompts?!?_ **PREPOSTEROUS!!**
#@markdown
#@markdown GPT-2 requires a prompt string to start a sentence. Best results will resemble part of your prompts. It can be a single letter or a full sentence.
#@markdown `If you leave this blank, Prompt Parrot will automatically choose starting phrases from your prompts`
prompt_override="Relaxing in" #@param{type:"string"}
num_prompts=10 #@param{type:"integer"}


#@markdown Maximum and min length of the generated prompts. Will cut off mid word. This is expected behavior
max_length= 10 #@param{type:"integer"}
min_length= 0 #@param{type:"integer"}
#@markdown `temperature`: If you find your prompts are too similar to inputs, try turning up the temperature. If your prompts are too insane, turn down the temperature. A good deafult is 1.6
temperature= 1.0 #@param{type:"number"}
#@markdown `top_k`: If you find your prompts are identical to your inputs, try turning down top_k. A good range is 70-100. A good default is 100.
top_k=100 #@param{type:"integer"}
top_p=0.9  #@param{type:"number"}


tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")
prompt = prompt_override

encoded_prompt = tokenizer(prompt, add_special_tokens=False, return_tensors="pt").input_ids
encoded_prompt = encoded_prompt.to(model.device)

output_sequences = model.generate(
    input_ids=encoded_prompt,
    max_length=max_length,
    min_length=min_length,
    temperature=temperature,
    top_k=top_k,
    top_p=top_p,
    do_sample=True,
    num_return_sequences=num_prompts,
    pad_token_id=tokenizer.eos_token_id # gets rid of warning
)

for generated_sequence in output_sequences:
    generated_sequence = generated_sequence.tolist()
    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True, skip_special_tokens=True)
    print(text.strip().replace("\n", " ").replace("/", ","))
