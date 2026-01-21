# import os
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.exceptions import OutputParserException
# from dotenv import load_dotenv

# load_dotenv()

# class Chain:
#     def __init__(self):
#         # Update model_name to llama-3.3-70b-versatile
#         self.llm = ChatGroq(
#             temperature=0, 
#             groq_api_key=os.getenv("GROQ_API_KEY"), 
#             model_name="llama-3.3-70b-versatile"
#         )

#     def extract_jobs(self, cleaned_text):
#         prompt_extract = PromptTemplate.from_template(
#             """
#             ### SCRAPED TEXT FROM WEBSITE:
#             {page_data}
#             ### INSTRUCTION:
#             The scraped text is from the career's page of a website.
#             Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
#             Only return the valid JSON.
#             ### VALID JSON (NO PREAMBLE):
#             """
#         )
#         chain_extract = prompt_extract | self.llm
#         res = chain_extract.invoke(input={"page_data": cleaned_text})
#         try:
#             json_parser = JsonOutputParser()
#             res = json_parser.parse(res.content)
#         except OutputParserException:
#             raise OutputParserException("Context too big. Unable to parse jobs.")
#         return res if isinstance(res, list) else [res]

# def write_mail(self, job, links):
#     prompt_email = PromptTemplate.from_template(
#         """
#         ### JOB DESCRIPTION:
#         {job_description}

#         ### INSTRUCTION:
#         You are Nagendra Kumar, a Software Engineer and B.Tech graduate from IIIT Allahabad. 
#         You have professional experience at Amnic Technologies and Real Dimension Studio.
#         Your goal is to write a highly professional cold email to a recruiter for the job mentioned above.
        
#         Highlight your expertise in:
#         - Scalable backend systems (Java, Go, Node.js)
#         - Full-stack development (Next.js, React)
#         - Problem-solving (Codeforces Expert, CodeChef 4-Star)
        
#         Include the following relevant project links from your portfolio to demonstrate your fit: {link_list}
        
#         Keep the tone professional, results-oriented, and concise.
#         Do not provide a preamble.
#         ### EMAIL (NO PREAMBLE):
#         """
#     )
#     chain_email = prompt_email | self.llm
#     res = chain_email.invoke({"job_description": str(job), "link_list": links})
#     return res.content

# if __name__ == "__main__":
#     print(os.getenv("GROQ_API_KEY"))


import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Set USER_AGENT to suppress the warning
os.environ["USER_AGENT"] = "MyPersonalJobAppAssistant/1.0"

load_dotenv()

class Chain:
    def __init__(self):
        # Update model_name to llama-3.3-70b-versatile
        self.llm = ChatGroq(
            temperature=0, 
            groq_api_key=os.getenv("GROQ_API_KEY"), 
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    # MOVED INSIDE CLASS: This must be indented like extract_jobs
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Nagendra Kumar, a Software Engineer and B.Tech graduate from IIIT Allahabad. 
            You have professional experience at Amnic Technologies and Real Dimension Studio.
            Your goal is to write a highly professional cold email to a recruiter for the job mentioned above.
            
            Highlight your expertise in:
            - Scalable backend systems (Java, Go, Node.js)
            - Full-stack development (Next.js, React)
            - Problem-solving (Codeforces Expert, CodeChef 4-Star)
            
            Include the following relevant project links from your portfolio to demonstrate your fit: {link_list}
            
            Keep the tone professional, results-oriented, and concise.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(f"API Key Loaded: {os.getenv('GROQ_API_KEY') is not None}")