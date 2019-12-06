"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
	rand_num = int(input("Enter the number of random scores: "))

	for i in range(rand_num):
		score = random.randrange(1,100)
		print("{} is {}".format(score, get_score_result(score)))

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