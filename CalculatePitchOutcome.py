import random
from Functions import pitching_team

def calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning): #Needs cleanup

	# This function attempts to replicate real-world outcomes as accurately as possible.
	# Probability data was taken from this post:
	# https://www.baseball-fever.com/forum/general-baseball/statistics-analysis-sabermetrics/81427-pitch-outcome-distribution-over-25-years
	# Pitches 1-12 of each at bat match the probability data.
	# If pitch 13 is reached, there is no foul outcome, to help prevent infinite at-bats.

	# For each pitch, a random number between from 1 to 100 is generated. That number is used to determine the pitch outcome.
	# If the pitcher has the "edge", and the outcome is a ball or a ball in play (or vice versa), a second random number from 1 to 100 is generated.
	# If the second random number is between 0 and the edge %, the pitch outcome is disregarded and starts over.

	# So, if the pitcher has a 20% edge over the batter, and the initial outcome was a ball, there is a 20% chance of a do-over.

	rand = random.randint(1, 100)

	if pitch == 1:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 2:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 3:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 4:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 5:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 6:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 7:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 8:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 9:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 10:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 11:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	elif pitch == 12:
		if rand >= 1 and rand <= current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1]:  # Ball
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball"
			else:
				return "Ball"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1]):  # Called Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1]):  # Foul
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Foul"
			else:
				return "Foul"
		elif rand >= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + 1) and rand <= (current_pitcher[pitching_team(half_inning)][2]['B'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['C'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['F'][pitch - 1] + current_pitcher[pitching_team(half_inning)][2]['S'][pitch - 1] + 1):  # Swinging Strike
			if edge_pos == "Batter":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Strike"
			else:
				return "Strike"
		else:  # Ball in play
			if edge_pos == "Pitcher":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_pitch_loops += 1
					return calculate_pitch_outcome(pitch, redo_pitch, edge_pos, margin, redo_pitch_loops, current_pitcher, half_inning)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	else:
		return "Ball_in_play"