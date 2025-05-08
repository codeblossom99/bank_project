"""
國泰程試驗習題
"""

def question1():
    """
    題目一：修正成績
    學生成績中, 有五位學生期中考分數分別為 [53, 64, 75, 19, 92]
    但是老師輸入時有錯誤, 把五位學生成績改成 [35, 46, 57, 91, 29]
    請使用一個變數將學生成績修正
    """

    incorrect_scores = [35, 46, 57, 91, 29]
    correct_scores = [53, 64, 75, 19, 92]

    print("question 1: 修正成績")
    print(f"輸入: {incorrect_scores}")
    print(f"輸出: {correct_scores}")

    fixed_scores = correct_scores
    print(f"替換成: {fixed_scores}")

def question2():
    """
    題目2：國泰60週年活動
    需要輸出"Hello welcome to Cathay 60th year anniversary"
    並給每一個英文單字賦予國字代碼(大小寫不同字母編碼也不同)
    """
    message = "Hello welcome to Cathay 60th year anniversary"
    
    def get_letter_code(letter):
        if 'A' <= letter <= 'Z':
            return chr(ord('A') + (ord(letter) - ord('A')))
        elif 'a' <= letter <= 'z':
            return chr(ord('A') + 26 + (ord(letter) - ord('a')))
        else:
            return letter
    
    words = message.split()
    word_codes = {}
    
    for word in words:
        if word.isalpha():
            code = ""
            for letter in word:
                code += get_letter_code(letter)
            word_codes[word] = code
    
    print("題目2：國泰60週年活動")
    print(f"原始訊息: {message}")
    print("單字代碼:")
    for word, code in word_codes.items():
        print(f"{word}: {code}")

def question3():
    """
    題目3：QA部門測試活動
    隨機產出一個0-100的數字n，要找出所有可整除n的數字
    """
    import random
    
    n = random.randint(0, 100)
    
    if n == 0:
        divisors = []
    else:
        divisors = [i for i in range(1, n + 1) if n % i == 0]
    
    print("題目3：QA部門測試活動")
    print(f"輸入: n值(0-100) = {n}")
    print(f"輸出: 整除{n}的數字 = {divisors}")
    print("\n")
    return divisors


def main():
    """主程式執行所有題目"""
    print("="*50)
    print("國泰程式練習題解答")
    print("="*50)
    
    question1()
    question2()
    question3()


if __name__ == "__main__":
    main()