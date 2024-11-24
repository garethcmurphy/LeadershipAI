import pandas as pd

# Data for the 100 leadership skills
categories = [
    "Communication Skills",
    "Emotional Intelligence",
    "Decision-Making",
    "Team Management",
    "Vision and Strategy",
    "Adaptability and Resilience",
    "Motivation and Influence",
    "Collaboration",
    "Innovation and Creativity",
    "Coaching and Development"
]

skills = [
    # Communication Skills
    "Active listening", "Public speaking", "Non-verbal communication", "Writing clearly and concisely", 
    "Storytelling", "Giving feedback", "Receiving feedback", "Persuasion", "Conflict resolution", 
    "Asking open-ended questions",
    
    # Emotional Intelligence
    "Empathy", "Self-awareness", "Self-regulation", "Recognizing emotions in others", "Managing stress", 
    "Building rapport", "Emotional resilience", "Demonstrating humility", "Active patience", "Practicing gratitude",
    
    # Decision-Making
    "Strategic thinking", "Analyzing data", "Risk assessment", "Critical thinking", "Prioritization", 
    "Problem-solving", "Situational awareness", "Evaluating trade-offs", "Consensus-building", "Decisiveness",
    
    # Team Management
    "Delegation", "Time management", "Conflict mediation", "Setting expectations", "Performance management", 
    "Building team morale", "Empowering team members", "Supporting professional development", 
    "Resolving interpersonal disputes", "Leading by example",
    
    # Vision and Strategy
    "Goal setting", "Long-term planning", "Innovation", "Identifying opportunities", 
    "Crafting a compelling vision", "Aligning teams with vision", "Resource allocation", 
    "Building a strategic roadmap", "Driving organizational change", "Balancing short- and long-term goals",
    
    # Adaptability and Resilience
    "Adapting to change", "Overcoming setbacks", "Managing uncertainty", "Learning from failure", 
    "Staying composed under pressure", "Reframing challenges", "Encouraging flexibility in teams", 
    "Open-mindedness", "Resilience in leadership", "Handling ambiguity",
    
    # Motivation and Influence
    "Inspiring others", "Building trust", "Recognizing team contributions", "Encouraging collaboration", 
    "Fostering loyalty", "Promoting accountability", "Motivating during tough times", 
    "Celebrating successes", "Advocating for team members", "Establishing credibility",
    
    # Collaboration
    "Building cross-functional teams", "Managing stakeholder expectations", 
    "Partnering with external organizations", "Mediating between departments", 
    "Facilitating group discussions", "Encouraging knowledge sharing", "Promoting inclusivity", 
    "Resolving team dynamics", "Negotiation", "Working effectively across cultures",
    
    # Innovation and Creativity
    "Brainstorming new ideas", "Encouraging creative problem-solving", "Supporting experimentation", 
    "Overcoming resistance to innovation", "Learning from other industries", "Applying design thinking", 
    "Driving continuous improvement", "Fostering a growth mindset", "Rewarding innovative thinking", 
    "Challenging the status quo",
    
    # Coaching and Development
    "Mentoring team members", "Identifying individual strengths", "Creating development plans", 
    "Delivering constructive criticism", "Encouraging self-improvement", "Supporting mental health", 
    "Building leadership pipelines", "Facilitating skill-building workshops", "Promoting work-life balance", 
    "Providing career guidance"
]

# Create a DataFrame
leadership_skills = pd.DataFrame({
    "Category": [category for category in categories for _ in range(10)],
    "Skill": skills
})

# Save to Excel
leadership_skills.to_excel("Leadership_Skills_100.xlsx", index=False)

print("Excel file 'Leadership_Skills_100.xlsx' has been created!")