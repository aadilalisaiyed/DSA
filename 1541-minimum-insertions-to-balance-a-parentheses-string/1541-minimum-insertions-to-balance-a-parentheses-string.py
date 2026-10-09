class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        insertions = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1

                # A single ')' is needed for every unmatched '(',
                # but each '(' requires TWO closing parentheses.
            else:
                # Check whether the next character is also ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1  # Insert a missing ')'

                if open > 0:
                    open -= 1
                else:
                    insertions += 1  # Insert a missing '('

            i += 1

        return insertions + 2 * open