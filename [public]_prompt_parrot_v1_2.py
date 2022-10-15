"""
Original file is located at
    https://colab.research.google.com/drive/1ZZWvzsqjEHNn1qevQ4ed7Ozs4vij7qfc
"""
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

#@title 1.1 prompts.txt

prompts_file_path = "C:/Users/victo/Downloads/PicturePromptGenerationStuff/content/prompts.txt" #@param{type:"string"}

all_prompts = []
if prompts_file_path:
    with open(prompts_file_path) as infile:
        all_prompts = infile.read().strip().split("\n")

if not all_prompts:
    raise UserWarning(f"Read 0 prompts from {prompts_file_path}")

prompt_starts = list(set([" ".join(p.split()[0:2]).replace(",", "") for p in all_prompts if len(p.split()) > 1]))

#@title 1.2 Train GPT-2
#@markdown Number of iterations to train for. Try 50-500? If prompts generated are identical to your input prompts, try turning down num_train_epochs.
num_train_epochs=50 #@param{type:"integer"}

end_token = "<|endoftext|>"
prompts_txt = "scrambled_prompts.txt"

# scramble the prompts so the model doesn't learn association between lines
with open(prompts_txt, "w+") as fp:
    for _ in range(19):
        random.shuffle(all_prompts)
        fp.write(end_token.join(all_prompts) + end_token)

# quick and dirty workaround to blow away the cache for now
# TODO: upgrade to huggingface datasets lib. TextDataset is deprecated
# !rm /content/cached_lm_GPT2TokenizerFast
# !rm -rf /content/output/

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")
train_dataset = TextDataset(tokenizer=tokenizer, file_path=prompts_txt, block_size=tokenizer.model_max_length)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

training_args = TrainingArguments(
    output_dir='./output',
    overwrite_output_dir=True,
    num_train_epochs=num_train_epochs,
    per_device_train_batch_size=1,
    prediction_loss_only=True,
    logging_steps=100,
    save_steps=0,
    seed=random.randint(0, 2**32-1),
)

trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

trainer.train()
model.save_pretrained("./model")

#@title 1.3 Generate prompts!

#@markdown _What?! A prompt for my prompts?!?_ **PREPOSTEROUS!!**
#@markdown
#@markdown GPT-2 requires a prompt string to start a sentence. Best results will resemble part of your prompts. It can be a single letter or a full sentence.
#@markdown `If you leave this blank, Prompt Parrot will automatically choose starting phrases from your prompts`
prompt_override="" #@param{type:"string"}
num_prompts=5 #@param{type:"integer"}


#@markdown Maximum and min length of the generated prompts. Will cut off mid word. This is expected behavior
max_length=30 #@param{type:"integer"}
min_length=10 #@param{type:"integer"}
#@markdown `temperature`: If you find your prompts are too similar to inputs, try turning up the temperature. If your prompts are too insane, turn down the temperature. A good deafult is 1.6
temperature=0.5 #@param{type:"number"}
#@markdown `top_k`: If you find your prompts are identical to your inputs, try turning down top_k. A good range is 70-100. A good default is 100.
top_k=80 #@param{type:"integer"}
top_p=0.9  #@param{type:"number"}

prompt = random.choice(prompt_starts)
if prompt_override:
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
