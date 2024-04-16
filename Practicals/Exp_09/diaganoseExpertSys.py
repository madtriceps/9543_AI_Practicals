class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'Yellow leaves': 'Nitrogen deficiency',
            'Brown spots on leaves': 'Fungal infection',
            'Wilting leaves': 'Watering issues',
            'White powdery substance on leaves': 'Powdery mildew'
        }

    def diagnose(self, symptoms):
        possible_diseases = []
        for symptom, disease in self.knowledge_base.items():
            if symptom in symptoms:
                possible_diseases.append(disease)
        return possible_diseases

class UserInterface:
    def __init__(self):
        self.expert_system = ExpertSystem()

    def start(self):
        print("Welcome to the Plant Disease Diagnosis System!")
        while True:
            print("\nEnter the symptoms separated by commas (e.g., Yellow leaves, Wilting leaves):")
            user_input = input("Symptoms: ")
            symptoms = [s.strip() for s in user_input.split(',')]
            diagnoses = self.expert_system.diagnose(symptoms)
            if diagnoses:
                print("\nPossible diseases:")
                for disease in diagnoses:
                    print(f"- {disease}")
            else:
                print("\nNo diagnosis could be made based on the symptoms provided.")

            choice = input("\nDo you want to diagnose another set of symptoms? (yes/no): ").lower()
            if choice != 'yes':
                print("Thank you for using the Plant Disease Diagnosis System!")
                break

# Example usage:
def main():
    ui = UserInterface()
    ui.start()

if __name__ == "__main__":
    main()
