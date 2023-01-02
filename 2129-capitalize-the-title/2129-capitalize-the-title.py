class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(map(lambda x: x.capitalize() if len(x) > 2 else x.lower(), title.split()))