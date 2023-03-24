import os
import openai

secret_key = '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'

openai.api_key = secret_key

from git import Repo
from pathlib import Path

path_to_blog_repo = Path("C:\\Users\\rodri\\OneDrive\\Desktop\\GPT Programming\\UdemyCurso2GPTAPIpy\\Roderic01.github.io\\.git")
path_to_blog = path_to_blog_repo.parent
path_to_content = path_to_blog/'content'

path_to_content.mkdir(exist_ok=True, parents=True)

def update_blog(commit_message='Updates blog'):
    # GitPythin -- Repo Location
    repo = Repo(path_to_blog_repo)
    #git add .
    repo.git.add(all=True)
    # git commit -m 'updates blog'
    repo.index.commit(commit_message)
    #git push
    origin = repo.remote(name='origin')
    origin.push()

random_text_string = 'ldkfalkghoakgjladkjglskald'

with open(path_to_blog/'index.html','w') as f:
    f.write(random_text_string)

update_blog()