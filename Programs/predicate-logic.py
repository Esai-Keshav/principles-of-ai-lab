class KnowledgeBase:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def remove_fact(self, fact):
        self.facts.discard(fact)

    def check_fact(self, fact):
        return fact in self.facts

    def display_facts(self):
        print("Facts in the Knowledge Base:")
        for fact in self.facts:
            print(fact)

    def to_first_order_logic(self):
        first_order_logic_facts = []

        for fact in self.facts:
            # Split the fact into words
            words = fact.split()

            # Check if the fact has the format: [subject] [is/are] [object(s)]
            if len(words) >= 3 and words[1] in ["is", "are"]:
                subject = words[0]
                predicate = words[2]
                objects = words[3:]

                # Create a first-order logic statement
                if len(objects) == 1:
                    first_order_logic = f"{predicate}({subject} {objects[0]})"
                else:
                    first_order_logic = f"{predicate}({subject} " + " ".join(objects) + ")"

                first_order_logic_facts.append(first_order_logic)

        return first_order_logic_facts

# Create a knowledge base
kb = KnowledgeBase()

# Accept facts from the user
print("Enter facts (one per line). Type 'q' to quit.")
while True:
    fact_str = input("Enter a fact: ")
    if fact_str.lower() == 'q':
        break

    kb.add_fact(fact_str)

# Check if a fact is in the knowledge base
check_fact_str = input("Enter a fact to check: ")
if kb.check_fact(check_fact_str):
    print(f"'{check_fact_str}' is a fact in the knowledge base.")
else:
    print(f"'{check_fact_str}' is not a fact in the knowledge base.")

# Display all facts in the knowledge base
kb.display_facts()

# Convert facts to first-order logic and display
first_order_logic_facts = kb.to_first_order_logic()
print("\nFacts in First-Order Logic:")
for fact in first_order_logic_facts:
    print(fact)
