def mad_libs():
    # Prompting the user for words 
     name = input("Enter a name: ")
     place = input("Enter a place: ")
     adjective1 = input("Enter a adjective: ")
     noun1 = input("Enter a noun: ")
     verb = input("Enter a verb: ")
     adjective2 = input("Enter another adjective: ")
     noun2 = input("Enter another noun: ")
     
    # Story Template
story = f"""
    Once upon a time, {name} went to {place}. It was a very {adjective1} day.
    There, they found a {noun1} and decided to {verb} it. As they continued on,
    they came across a {adjective2} {noun2} that was unlike anything they had seen before.
    This was a day to remember for {name} at {place}!
    """
    
    # Display the story
print("\nHere's your Mad Libs story:\n")
print(story)
    
mad_libs()

     
    