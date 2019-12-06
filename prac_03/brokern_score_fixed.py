"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
	print(get_score_result(float(input("Enter a score: "))))
	print("random score result:")
	print(get_score_result(random.randrange(0,100)))

def get_score_result(score):
	result = ""
	if score < 0 or score > 100:
		result="Invalid score"

	elif score < 50:
		result="Bad"

	elif score >= 50 and score < 90:
		result="Pass"

	else:
		result="Excellent"

	return result

main()