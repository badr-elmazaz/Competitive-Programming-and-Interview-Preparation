class Solution:
    def simplifyPath(self, path: str) -> str:
        # n = len(path)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        canonical_path = []

        for current_dir in path.split("/"):
            if current_dir in [".", ""]:
                continue

            if current_dir == "..":
                if canonical_path:
                    canonical_path.pop()
                continue

            canonical_path.append(current_dir)

        return "/" + "/".join(canonical_path)
