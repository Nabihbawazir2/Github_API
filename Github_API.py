import requests
import pandas as pd

class GitHubAPI:
    def __init__(self, username, token=None):
        self.username = username
        self.base_url = "https://api.github.com"
        self.headers = {'Authorization': f'token {token}'} if token else {}

    def get_repositories(self):
        url = f"{self.base_url}/users/{self.username}/repos"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch repos: {response.status_code}")
        return response.json()

    def get_commit_count(self, repo_name):
        url = f"{self.base_url}/repos/{self.username}/{repo_name}/commits"
        response = requests.get(url, headers=self.headers, params={'per_page': 1})
        if 'Link' in response.headers:
            # Extract the last page number from the Link header
            link = response.headers['Link']
            if 'rel="last"' in link:
                last_page = int(link.split('page=')[-1].split('>')[0])
                return last_page
        return len(response.json())  # fallback if pagination is not available

class GitHubRepoAnalyzer:
    def __init__(self, api: GitHubAPI):
        self.api = api

    def analyze_repositories(self):
        repos = self.api.get_repositories()
        data = []
        for repo in repos:
            name = repo['name']
            stars = repo['stargazers_count']
            forks = repo['forks_count']
            try:
                commits = self.api.get_commit_count(name)
            except Exception as e:
                commits = None
            data.append({
                'name': name,
                'stars': stars,
                'forks': forks,
                'commits': commits
            })
        df = pd.DataFrame(data)
        return df

# --- Usage ---
if __name__ == "__main__":
    username = "octocat"  # change this to your username or any public one
    token = None  # optional: generate a GitHub personal access token to avoid rate limits

    github_api = GitHubAPI(username, token)
    analyzer = GitHubRepoAnalyzer(github_api)

    df = analyzer.analyze_repositories()
    print(df.sort_values(by='stars', ascending=False))
    df.to_csv("github_repo.csv")
