
# GitHub Tool Usage Guide

The GitHub tool allows you to interact with GitHub repositories directly from Agent Zero. Here's how you can use it effectively:

## Available Actions

1. create_repo: Create a new GitHub repository
2. push_project: Push a local project to a GitHub repository
3. get_repo: Fetch information about a specific GitHub repository
4. list_repos: List all repositories for the authenticated user

## Usage Examples

### 1. Create a new repository

To create a new repository on GitHub:
~~~json
{
    "tool_name": "github_tool",
    "tool_args": {
        "action": "create_repo",
        "repo_name": "my-new-awesome-project"
    }
}
~~~
### 2. Push a project to a repository

To push a local project to a GitHub repository:
~~~json
{
    "tool_name": "github_tool",
    "tool_args": {
        "action": "push_project",
        "repo_name": "my-new-awesome-project",
        "project_path": "/path/to/local/project"
    }
}
~~~
### 3. Get information about a repository

To fetch information about a specific repository:
~~~json
{
    "tool_name": "github_tool",
    "tool_args": {
        "action": "get_repo",
        "repo_name": "username/repo-name"
    }
}
~~~
### 4. List all repositories

To list all repositories for the authenticated user:
~~~json
{
    "tool_name": "github_tool",
    "tool_args": {
        "action": "list_repos"
    }
}
~~~
## Tips for Assisting Users

- When a user asks about version control or sharing code, suggest using the GitHub tool.
- If a user wants to collaborate on a project, recommend creating a repository and pushing their project.
- For users new to GitHub, explain the benefits of version control and how it can help in project management.
- If a user needs to check the status of their repositories, suggest using the list_repos action.
- Always remind users to ensure their GITHUB_TOKEN is set in the .env file before using the tool.

Remember to adapt your suggestions based on the user's experience level with Git and GitHub.
