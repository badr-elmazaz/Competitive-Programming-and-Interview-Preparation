class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # n = len(cpdomains)
        # m = max(cpdomains[i].split("."))
        # Time Complexity: O(n * m)
        # Space Complexity: O(n * m)
        
        hashtable = defaultdict(int)

        for visit_count in cpdomains:
            visits, domain = visit_count.split()
            visits = int(visits)
            subdomains = list(reversed(domain.split(".")))
            running_subdomains = subdomains[0]
            hashtable[running_subdomains] += visits
            for i in range(1, len(subdomains)):
                running_subdomains = subdomains[i] + "." + running_subdomains
                hashtable[running_subdomains] += visits

        output = []

        for domain, visits in hashtable.items():
            output.append(f"{visits} {domain}")  

        return output  