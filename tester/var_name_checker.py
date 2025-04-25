from pylint.checkers import BaseChecker

var_for_check = "daniil"

class VarNameChecker(BaseChecker):

    name = "var-name-checker"
    
    msgs = {
        "E2025": (
            f"Переменная с именем {var_for_check} найдена.",
            f"var-{var_for_check}-found",
            f"Проверьте правила проекта на запрет или допущение переменной с именем {var_for_check}."
        )
    }

    def visit_assign(self, node):
        for target in node.targets:
            if hasattr(target, "name") and target.name == var_for_check:
                self.add_message(f"var-{var_for_check}-found", node=target)

def register(linter):
    linter.register_checker(VarNameChecker(linter))