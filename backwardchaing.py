def backward_chaining(goal, knowledge_base, facts):
    if goal in facts:
        return True
    if goal not in knowledge_base:
        return False
    return all(all(backward_chaining(sub_goal, knowledge_base, facts) for sub_goal in premise) 
               for premise in knowledge_base[goal])

knowledge_base = {
    "A": [["B", "C"]],
    "B": [["D"]],
    "C": [["E", "F"]],
}
facts = {"D", "E", "F"}
goal = "A"

if backward_chaining(goal, knowledge_base, facts):
    print(f"The goal '{goal}' is proven!")
else:
    print(f"The goal '{goal}' cannot be proven.")
