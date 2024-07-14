from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
programming_languages = [python, ruby, visual_basic]
dynamic_language_name = [pl.name for pl in programming_languages if pl.is_dynamic()]
print("The Dynamically Typed Languages are:")
for pl in dynamic_language_name:
    print(pl)

