def isPalindrome(s: str) -> bool:
        array = "".join([i.lower() for i in s if i.isalnum()])
        return array == array[::-1]