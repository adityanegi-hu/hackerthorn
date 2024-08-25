# Career Path Recommender

skills_to_career = {
    "programming": ["Software Engineer", "Data Scientist", "Web Developer"],
    "design": ["UI/UX Designer", "Graphic Designer", "Product Designer"],
    "communication": ["Content Writer", "Public Relations Specialist", "Marketing Manager"],
    "leadership":["ability of an individual, group, or organization to, influence, or guide other individuals, teams,"],
    "creative" :[" Creativity may also describe the ability to find new solutions to problems, or new methods of performing a task or reaching a goal"],
    }

def recommend_career(skill):
    """
    Recommends career paths based on a given skill.
    """
    if skill in skills_to_career:
        return skills_to_career[skill]
    else:
        return ["No specific career path found for this skill."]

if __name__ == "__main__":
    user_skill = input("Enter a skill: ").lower()
    recommended_careers = recommend_career(user_skill)
    print("Recommended career paths:")
    for career in recommended_careers:
        print(f"- {career}")
