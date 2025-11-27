
risks_list = [
        "Privacy concerns: AI-powered devices may collect personal data, raising concerns about how this data is stored and used.",
        "Security vulnerabilities: AI systems could be susceptible to cyberattacks, leading to unauthorized access to personal information.",
        "Bias in AI algorithms: AI algorithms might inadvertently perpetuate biases present in the data they are trained on, leading to unfair or discriminatory outcomes.",
        #you may add more AI Risks to this list
    ]


def get_risks_and_categories(risks_list):
    """
    Identify and categorize potential risks of using AI in everyday life.

    Parameters:
        risks_list (list): A list of potential risks and categories associated with AI usage.

    Returns:
        list: A list containing categorized risks.
    """

    print("Welcome to the AI Risks Identification Tool!")
    print("Enter the category of each risk:")

    risks_categories = []
    for risk in risks_list:
        print(f'\nRisk:\n{risk}')
        category= input("Enter the category for this risk:")
        risks_categories.append([category, risk])

    return risks_categories

def identify_risks(risks_categories):
    """
     Identify and categorize potential risks of using AI in everyday life.

     Parameters:
         risks_categories (list): A list of potential risks and categories associated with AI usage.

     Returns:
         dict: A dictionary containing categorized risks.
     """
    risks = {}
    for category, risk in risks_categories:
        if category not in risks:
            risks[category] = []
        risks[category].append(risk)
    return risks


def display_risks_summary(risks):
    """
    Display a summary of identified risks under each category.

    Parameters:
        risks (dict): A dictionary containing categorized risks.
    """
    print("\nAI Risks Summary:\n")
    for category in risks:
        print(category + ':')
        for risk in risks[category]:
            print("-", risk)

risks_categories = get_risks_and_categories(risks_list)
risks_data = identify_risks(risks_categories)
print(display_risks_summary(risks_data))
