import httpx
from openai import OpenAI
import prompts
import config

openai_api_key = config.openai_key
client = OpenAI(
        # This is the default and can be omitted
        api_key=openai_api_key
    )

def default(latest_reply: str):
    prompt = prompts.default_prompt(latest_reply)

    company_info = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    company_info = company_info.choices[0].message.content
    return company_info

def get_company_name(client, latest_reply: str):
    prompt = prompts.company_name_prompt(latest_reply)

    company_info = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    company_info = company_info.choices[0].message.content
    return company_info

def engine(email):
    company_name = get_company_name(client, email).replace('COMPANY NAME: ', '')
    if 'NO COMPANY' in company_name:
        return {'is_company': 'NO', 'summary': None}
    else:
        print(f'Company name: {company_name}')
        company_summary = get_company_summary(client, company_name)
        if 'NO COMPANY' in company_summary:
            return {'is_company': 'NO', 'summary': None}
        else:
            return {'is_company': 'YES', 'summary': company_summary}
            
def get_company_summary(client, name):
    url = f"https://api.peopledatalabs.com/v5/company/enrich?name={name}&pretty=false"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-API-Key": config.company_enrich
    }

    response = httpx.get(url, headers=headers)
    prompt = prompts.company_summary_prompt(response.json())

    company_summary = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    company_summary = company_summary.choices[0].message.content
    return company_summary

def main(email):
    try:
        company_info = engine(email)
        return company_info
    except Exception as e:
        print(f'Error {e}')
        default_result = {'is_company': 'YES', 'summary': default(email)}
        return default_result