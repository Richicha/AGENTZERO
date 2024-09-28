import os
import subprocess
from dotenv import load_dotenv
from github import Github

from python.helpers.tool import Tool, Response

class GitHubTool(Tool):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()  # Load environment variables from .env file
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.g = Github(self.github_token)

    async def execute(self, **kwargs):
        action = kwargs.get('action')
        if action == 'create_repo':
            return await self.create_repo(**kwargs)
        elif action == 'push_project':
            return await self.push_project(**kwargs)
        elif action == 'get_repo':
            return await self.get_repo(**kwargs)
        elif action == 'list_repos':
            return await self.list_repos(**kwargs)
        else:
            return Response(message="Invalid action specified", break_loop=False)

    async def create_repo(self, **kwargs):
        repo_name = kwargs.get('repo_name')
        if not repo_name:
            return Response(message="Repository name not provided", break_loop=False)
        
        try:
            user = self.g.get_user()
            repo = user.create_repo(repo_name)
            return Response(message=f"Repository '{repo_name}' created successfully. URL: {repo.html_url}", break_loop=False)
        except Exception as e:
            return Response(message=f"Error creating repository: {str(e)}", break_loop=False)

    async def push_project(self, **kwargs):
        repo_name = kwargs.get('repo_name')
        project_path = kwargs.get('project_path')
        if not repo_name or not project_path:
            return Response(message="Repository name or project path not provided", break_loop=False)
        
        try:
            # Initialize git repository
            subprocess.run(['git', 'init'], cwd=project_path, check=True)
            
            # Add all files
            subprocess.run(['git', 'add', '.'], cwd=project_path, check=True)
            
            # Commit changes
            subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=project_path, check=True)
            
            # Add remote
            repo_url = f'https://{self.github_token}@github.com/{self.g.get_user().login}/{repo_name}.git'
            subprocess.run(['git', 'remote', 'add', 'origin', repo_url], cwd=project_path, check=True)
            
            # Push to GitHub
            subprocess.run(['git', 'push', '-u', 'origin', 'master'], cwd=project_path, check=True)
            
            return Response(message=f"Project pushed to '{repo_name}' successfully.", break_loop=False)
        except subprocess.CalledProcessError as e:
            return Response(message=f"Error pushing project: {str(e)}", break_loop=False)

    async def get_repo(self, **kwargs):
        repo_name = kwargs.get('repo_name')
        if not repo_name:
            return Response(message="Repository name not provided", break_loop=False)
        
        try:
            repo = self.g.get_repo(repo_name)
            return Response(message=f"Repository '{repo_name}' fetched successfully. URL: {repo.html_url}", break_loop=False)
        except Exception as e:
            return Response(message=f"Error fetching repository: {str(e)}", break_loop=False)

    async def list_repos(self, **kwargs):
        try:
            user = self.g.get_user()
            repos = user.get_repos()
            repo_list = [f"{repo.name}: {repo.html_url}" for repo in repos]
            return Response(message=f"List of repositories:\n{chr(10).join(repo_list)}", break_loop=False)
        except Exception as e:
            return Response(message=f"Error listing repositories: {str(e)}", break_loop=False)
