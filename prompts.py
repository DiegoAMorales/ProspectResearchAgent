
def default_prompt(latest_reply):
    PROMPT = f"""
        EMAIL: {latest_reply}
        ---

        You are a company enrichment AI Agent with good knowledge of the web and remember is there is no company name in the email return "NO COMPANY".
        Above is an email; Your goal is to do a deep search about the company on the respective platforms to get the following information and generate a summary 
        paragraph for the company and make sure to include all links

        Name
        Website
        Description
        Linkedin Url
        Facebook
        Twitter / X
        Instagram
        Revenue
        Employees
        Industry

        (Return ONLY COMPANY SUMMARY)

        ONLY COMPANY SUMMARY:
        """
    return PROMPT

def company_name_prompt(latest_reply):
    return f"""
    EMAIL: {latest_reply}
    ---

    You are a company enrichment AI Agent with good knowledge of the web and remember is there is no company email in the search return NO COMPANY.
    Above is an email; Your goal is to return the name of the company:

    (Return ONLY COMPANY NAME or NO COMPANY)

    ONLY COMPANY NAME or NO COMPANY:
    """

def company_summary_prompt(company_info):
    return f"""
    CONTEXT: {company_info}
    ---

    You are a smart AI agent who can generate good summary about any company, If no company in context return "NO COMPANY".
    Using the CONTEXT above as the context, generate a summary for the company and make sure to include all links.

    (Return ONLY COMPANY SUMMARY)

    ONLY COMPANY SUMMARY:
    """


