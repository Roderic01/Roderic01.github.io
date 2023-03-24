import os
import openai
from git import Repo
from pathlib import Path

secret_key = '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'

openai.api_key = secret_key

path_to_blog_repo = Path("C:\\Users\\rodri\\OneDrive\\Desktop\\GPT Programming\\UdemyCurso2GPTAPIpy\\Roderic01.github.io\\.git")
path_to_blog = path_to_blog_repo.parent
path_to_content = path_to_blog/'content'

path_to_content.mkdir(exist_ok=True, parents=True)

def update_blog(commit_message='Updates blog'):
    repo = Repo(path_to_blog_repo)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

random_text_string = "<h1>Chichis pa la banda!!</h1>"

with open(path_to_blog/'index.html', 'w') as f:
    f.write(random_text_string)

update_blog()
