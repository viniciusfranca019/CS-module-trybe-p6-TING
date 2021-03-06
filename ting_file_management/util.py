import re


def get_files_name(queue):
    files_names = []
    for msg in queue.__queue__():
        files_names.append(msg["nome_do_arquivo"])
    return files_names


def exists_word_in_line(word, line):
    """
    https://www.w3schools.com/python/python_regex.asp
    https://www.w3schools.com/python/python_regex.asp#matchobject
    https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
    https://gitanswer.com/flake8-g-incorrectly-flagged-as-invalid-escape-sequence-replacement-issue-python-849566460
    https://www.pythontutorial.net/python-basics/python-raw-strings/
    """
    match_obj = re.search(r'{word}'.format(word=word), line, re.IGNORECASE)
    if match_obj is None:
        return {"has": False, "line": ""}
    return {"has": True, "line": match_obj.string}


def exists_word_in_msg(word, lines_msg, return_line=False):
    exists_in_line = []
    for line in lines_msg:
        verify = exists_word_in_line(word, line)
        if verify["has"] and return_line:
            exists_in_line.append({
                "linha": lines_msg.index(line) + 1,
                "conteudo": verify["line"]
            })
        if verify["has"] and not return_line:
            exists_in_line.append({"linha": lines_msg.index(line) + 1})
    return exists_in_line


def exists_word_dto(word, msg, return_line=False):
    dto = None
    if len(exists_word_in_msg(word, msg["linhas_do_arquivo"])) > 0:
        lines = msg["linhas_do_arquivo"]
        dto = {
            "palavra": word,
            "arquivo": msg["nome_do_arquivo"],
            "ocorrencias": exists_word_in_msg(word, lines, return_line)
        }
    return dto
