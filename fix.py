with open("app/api/analyst.py", "r") as f:
    lines = f.readlines()

with open("app/api/analyst.py", "w") as f:
    for line in lines:
        if "response_model=GenericResponse if False else Dict[str, Any]" in line:
            f.write(line.replace("GenericResponse if False else Dict[str, Any]", "Dict[str, Any]"))
        else:
            f.write(line)
