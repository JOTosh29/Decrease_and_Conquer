# Extended Python code for Josephus Problem with elimination order
def josephus(person, k, index, eliminated):
    # Base case: only one person left
    if len(person) == 1:
        print("Elimination order:", eliminated)
        print("Survivor:", person[0])
        return

    # Find the index of the next person to be eliminated
    index = (index + k) % len(person)

    # Add the eliminated person to the list
    eliminated.append(person[index])

    # Remove the person from the circle
    person.pop(index)

    # Recursive call for the remaining people
    josephus(person, k, index, eliminated)

# Driver code
n = int(input("Enter Number of People: "))  # Number of people
k = int(input("Enter the number on which every person is selected: "))   # Every "k"th person will be eliminated
k -= 1  # Convert to 0-based index (k-1)
index = 0

# Initialize the circle
person = list(range(1, n + 1))
eliminated = []

josephus(person, k, index, eliminated)
