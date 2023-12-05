import pandas as pd


class MedicalExpertSystem:
    def __init__(self):
        """Initialize the MedicalExpertSystem."""
        self.__symptoms = []
        self.__diagnosis = None
        self.__patient_data = pd.DataFrame(columns=["Symptoms", "Diagnosis"])

    def __ask_question(self, question):
        """Ask a yes/no question and return the answer."""
        answer = input(question + " (yes/no): ").strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            return self.__ask_question(question)

    def __diagnose(self):
        """Diagnose the patient based on symptoms."""
        if self.__ask_question("Do you have a fever?"):
            self.__symptoms.append("fever")
        if self.__ask_question("Do you have a headache?"):
            self.__symptoms.append("headache")
        if self.__ask_question("Do you have a cough?"):
            self.__symptoms.append("cough")

        new_data = pd.DataFrame(
            {"Symptoms": [", ".join(self.__symptoms)], "Diagnosis": [""]}
        )
        self.__patient_data = pd.concat(
            [self.__patient_data, new_data], ignore_index=True
        )

        if "fever" in self.__symptoms and "headache" in self.__symptoms:
            self.__diagnosis = "You might have the flu."
        elif "fever" in self.__symptoms and "cough" in self.__symptoms:
            self.__diagnosis = "You might have a cold."
        else:
            self.__diagnosis = "Your condition is unclear. Please consult a doctor."

        self.__patient_data.loc[
            self.__patient_data.index[-1], "Diagnosis"
        ] = self.__diagnosis

    def run(self):
        """Run the Medical Expert System."""
        print("Welcome to the Medical Expert System.")
        self.__diagnose()
        print("Diagnosis:", self.__diagnosis)
        print("Patient Data:")
        print(self.__patient_data)


if __name__ == "__main__":
    expert_system = MedicalExpertSystem()
    expert_system.run()
