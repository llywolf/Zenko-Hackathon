import openai
import json
import key

with open('hackZenko/FAQ_FDV_Zenko_V1.2.json', 'r') as f:
    data = json.load(f)
#messages = [{'question': item['question'], 'answer': item['answer']} for item in data['Général']]
# Define the OpenAI API key here or use environment variables
openai.api_key = key.api_key

def get_api_response(messages: list) -> str:
    text = None
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        
        if response['choices'][0]['message']['role'] == 'assistant':
            text = response['choices'][0]['message']['content']
    except Exception as e:
        print('ERROR: ', e)
    
    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)

def create_prompt(message: str, pl: list[dict]) -> list[dict]:
    user_message = {'role': 'user', 'content': message}
    pl.append(user_message)
    return pl

def get_bot_response(message: str, pl: list[dict]) -> str:
    prompt = create_prompt(message, pl)
    bot_response = get_api_response(prompt)
  
    if bot_response:
        assistant_message = {'role': 'assistant', 'content': bot_response}
        pl.append(assistant_message)
        bot_response = bot_response.lstrip()
    else:
        bot_response = "something went wrong"
    
    return bot_response

def main():
    prompt_list = [{'role': 'system', 'content': 'You are an expert capable of meeting all the needs of a festival, both internally and externally. Central point of interaction with festival-goers. - Answer questions about tickets, schedules, and more. Provide multilingual support.'}]

    
    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')
#        print(prompt_list)

if __name__ == '__main__':
    main()
