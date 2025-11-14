class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        len_s = len(sentence)
        stc = []
        words = sentence.split()

        trie = {}
        for word in dictionary:
            pointer = trie
            chars = [char for char in word]
            for i in range(len(word)):
                if pointer.get(word[i]):
                    pointer = pointer[word[i]]
                else:
                    pointer[word[i]] = {}
                    pointer = pointer[word[i]]
            pointer[1] = 1

        print(trie)
        answer = []
        for word in words:
            pointer = trie
            tmp = []
            for i in range(len(word)):
                if pointer.get(word[i]):
                    tmp.append(word[i])
                    if pointer[word[i]].get(1):
                        answer.append(''.join(tmp))
                        break
                    else:
                        pointer = pointer[word[i]]
                else:
                    answer.append(word)
                    break
            else:
                if tmp:
                    answer.append(''.join(tmp))

        return ' '.join(answer)