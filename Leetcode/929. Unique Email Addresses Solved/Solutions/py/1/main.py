class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # n = len(emails) ; m = max(len(emails[i]))
        # Time  -> O(n)
        # Space -> O(n*m)
        
        unique_emails = set()

        for email in emails:
            email_checked = []
            seen_at = False
            seen_plus = False
            for char in email:
                if char == "@":
                    seen_at = True
                if seen_plus and not seen_at:
                    continue
                if char == "+":
                    seen_plus = True
                    continue
                if not seen_at and char == ".":
                        continue
                email_checked.append(char)

            email_checked = "".join(email_checked)
            unique_emails.add(email_checked)

        return len(unique_emails)
        