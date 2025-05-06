# To scrap players and stats from baseball-reference
from lxml import html
import requests
from PyBaseballFunctions import *

def LoadBatters(abbrs, years):
	# Scrape top 9 batters and batting averages for specified team/year

	# Load baseball-reference page for inputted team/year
	# URL format: https://www.baseball-reference.com/teams/BOS/2004.shtml
	home_page = cloudscraper.create_scraper().get(
		"https://www.baseball-reference.com/teams/" + abbrs["home"]  + "/" + years["home"] + ".shtml"
	)
	home_tree = html.fromstring(home_page.content)
	away_page = cloudscraper.create_scraper().get(
		"https://www.baseball-reference.com/teams/" + abbrs["away"]  + "/" + years["away"] + ".shtml"
	)
	away_tree = html.fromstring(away_page.content)

	batters = {"home": ["", "", "", "", "", "", "", "", ""], "away": ["", "", "", "", "", "", "", "", ""]}
	batters_stats = {"home": ["", "", "", "", "", "", "", "", ""], "away": ["", "", "", "", "", "", "", "", ""]} #Batters stats

	# Scrape names of top 8 batters
	for x in range(8):
		# Home
		fullname = home_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[' + str(x + 1) + "]//td[1]"
							)[0].text_content().strip()
		fname = str(fullname).split()[0].replace("*", "").replace("#", "")
		lname = str(fullname).split()[1].replace("*", "").replace("#", "")
		batters["home"][x] = fname.strip("[],'") + " " + lname.strip("[],'")
		batters_stats["home"][x] = batter_i(fname.strip("[],'"), lname.strip("[],'")) #Batters stats

		# Away
		fullname = away_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[' + str(x + 1) + "]//td[1]"
							)[0].text_content().strip()
		fname = str(fullname).split()[0].replace("*", "").replace("#", "")
		lname = str(fullname).split()[1].replace("*", "").replace("#", "")
		batters["away"][x] = fname.strip("[],'") + " " + lname.strip("[],'")
		batters_stats["away"][x] = batter_i(fname.strip("[],'"), lname.strip("[],'")) #Batters stats

	# Scrape name of 9th batter (sometimes the formatting on baseball-reference skips the 9th row)
	# Home
	fullname = home_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[9]//td[1]'
							)[0].text_content().strip()
	if fullname == []:
		fullname = home_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[10]//td[1]'
							)[0].text_content().strip()

	fname = str(fullname).split()[0].replace("*", "").replace("#", "")
	lname = str(fullname).split()[1].replace("*", "").replace("#", "")
	batters["home"][8] = fname.strip("[],'") + " " + lname.strip("[],'")
	batters_stats["home"][8] = batter_i(fname.strip("[],'"), lname.strip("[],'")) #Batters stats

	# Away
	fullname = away_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[9]//td[1]'
							)[0].text_content().strip()
	if fullname == []:
		fullname = away_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[10]//td[1]'
							)[0].text_content().strip()

	fname = str(fullname).split()[0].replace("*", "").replace("#", "")
	lname = str(fullname).split()[1].replace("*", "").replace("#", "")
	batters["away"][8] = fname.strip("[],'") + " " + lname.strip("[],'")
	batters_stats["away"][8] = batter_i(fname.strip("[],'"), lname.strip("[],'")) #Batters stats

	# Batting averages
	home_avg = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	away_avg = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	# Scrape batting averages of first 8 batters
	for x in range(8):
		avg = home_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[' + str(x + 1) + "]//td[18]"
							)[0].text_content().strip()
		home_avg[x] = float(str(avg).strip("[]'"))
		avg = away_tree.xpath(
			'//table[@id="players_standard_batting"]//tbody//tr[' + str(x + 1) + "]//td[18]"
							)[0].text_content().strip()
		away_avg[x] = float(str(avg).strip("[]'"))

	# Scrape batting average of 9th batter
	avg = home_tree.xpath('//table[@id="players_standard_batting"]//tbody//tr[9]//td[18]'
							)[0].text_content().strip()
	if avg == []:
		avg = home_tree.xpath('//table[@id="players_standard_batting"]//tbody//tr[10]//td[18]'
							)[0].text_content().strip()
		home_avg[8] = float(str(avg).strip("[]'"))
	else:
		home_avg[8] = float(str(avg).strip("[]'"))

	avg = away_tree.xpath('//table[@id="players_standard_batting"]//tbody//tr[9]//td[18]'
							)[0].text_content().strip()
	if avg == []:
		avg = away_tree.xpath('//table[@id="players_standard_batting"]//tbody//tr[10]//td[18]'
							)[0].text_content().strip()
		away_avg[8] = float(str(avg).strip("[]'"))
	else:
		away_avg[8] = float(str(avg).strip("[]'"))

	# Add batting averages to batters array
	batters["home"] = [
		[batters["home"][0], home_avg[0], batters_stats["home"][0]],
		[batters["home"][1], home_avg[1], batters_stats["home"][1]],
		[batters["home"][2], home_avg[2], batters_stats["home"][2]],
		[batters["home"][3], home_avg[3], batters_stats["home"][3]],
		[batters["home"][4], home_avg[4], batters_stats["home"][4]],
		[batters["home"][5], home_avg[5], batters_stats["home"][5]],
		[batters["home"][6], home_avg[6], batters_stats["home"][6]],
		[batters["home"][7], home_avg[7], batters_stats["home"][7]],
		[batters["home"][8], home_avg[8], batters_stats["home"][8]],
	]
	batters["away"] = [
		[batters["away"][0], away_avg[0], batters_stats["away"][0]],
		[batters["away"][1], away_avg[1], batters_stats["away"][1]],
		[batters["away"][2], away_avg[2], batters_stats["away"][2]],
		[batters["away"][3], away_avg[3], batters_stats["away"][3]],
		[batters["away"][4], away_avg[4], batters_stats["away"][4]],
		[batters["away"][5], away_avg[5], batters_stats["away"][5]],
		[batters["away"][6], away_avg[6], batters_stats["away"][6]],
		[batters["away"][7], away_avg[7], batters_stats["away"][7]],
		[batters["away"][8], away_avg[8], batters_stats["away"][8]],
	]

	# Fill in empty stats for box score
	for x in range(9):
		batters["home"][x].append(0)
		batters["home"][x].append(0)
		batters["home"][x].append(0)
		batters["home"][x].append(0)
		batters["home"][x].append(0)
		batters["home"][x].append(0)
		batters["home"][x].append(0)
		batters["away"][x].append(0)
		batters["away"][x].append(0)
		batters["away"][x].append(0)
		batters["away"][x].append(0)
		batters["away"][x].append(0)
		batters["away"][x].append(0)
		batters["away"][x].append(0)

	# Sort array by batting average to determine batting order
	batters["home"] = sorted(batters["home"], key=lambda x: x[1], reverse=True)
	batters["away"] = sorted(batters["away"], key=lambda x: x[1], reverse=True)

	return batters

def LoadPitchers(abbrs, years):

	home_page = cloudscraper.create_scraper().get(
			"https://www.baseball-reference.com/teams/" + abbrs["home"]  + "/" + years["home"] + ".shtml"
		)
	home_tree = html.fromstring(home_page.content)
	away_page = cloudscraper.create_scraper().get(
			"https://www.baseball-reference.com/teams/" + abbrs["away"]  + "/" + years["away"] + ".shtml"
		)
	away_tree = html.fromstring(away_page.content)

	###########################################################
	# Scrape top 12 pitchers and earned run averages for specified team/year
	# A third column was added so that we can store pitcher's stats
	pitchers = {"home": 
					[
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]]
					], 
				"away": 
					[
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]]
					]
				}

	# A third column was added so that we can store pitcher's stats
	relief_pitchers = {"home": [[[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]]], "away": [[[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]]]}

	closers = {"home": ["", 0, ""], "away": ["", 0, ""]}


	# Scrape names and Earned Run Averages of top 12 pitchers
	# (Some extras because there are a variable number of blank/header lines mixed in)
	for x in range(12):
		# Home
		if x <= 4:
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath('//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

		if x > 4 and x <= 9:
			# Home
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'"))
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

		if x > 9:
			# Home
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'"))
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

	# For some reason, these loops need to be run twice each to remove empty array elements
	for x in pitchers["home"]:
		if "_EMPTY_" in x:
			pitchers["home"].remove(x)
	for x in pitchers["home"]:
		if "_EMPTY_" in x:
			pitchers["home"].remove(x)
	for x in pitchers["away"]:
		if "_EMPTY_" in x:
			pitchers["away"].remove(x)
	for x in pitchers["away"]:
		if "_EMPTY_" in x:
			pitchers["away"].remove(x)

	# Pitchers 5 through 9 are relief pitchers
	for x in range(5, 9):
		relief_pitchers["home"][x - 5] = pitchers["home"][x]
		relief_pitchers["away"][x - 5] = pitchers["away"][x]

	return pitchers

def LoadRelievers(abbrs, years):

	home_page = cloudscraper.create_scraper().get(
			"https://www.baseball-reference.com/teams/" + abbrs["home"]  + "/" + years["home"] + ".shtml"
		)
	home_tree = html.fromstring(home_page.content)
	away_page = cloudscraper.create_scraper().get(
			"https://www.baseball-reference.com/teams/" + abbrs["away"]  + "/" + years["away"] + ".shtml"
		)
	away_tree = html.fromstring(away_page.content)

	###########################################################
	# Scrape top 12 pitchers and earned run averages for specified team/year
	# A third column was added so that we can store pitcher's stats
	pitchers = {"home": 
					[
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]]
					], 
				"away": 
					[
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]]
					]
				}

	# A third column was added so that we can store pitcher's stats
	relief_pitchers = {"home": [[[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]]], "away": [[[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]]]}

	closers = {"home": ["", 0, ""], "away": ["", 0, ""]}


	# Scrape names and Earned Run Averages of top 12 pitchers
	# (Some extras because there are a variable number of blank/header lines mixed in)
	for x in range(12):
		# Home
		if x <= 4:
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath('//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

		if x > 4 and x <= 9:
			# Home
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'"))
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

		if x > 9:
			# Home
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'"))
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

	# For some reason, these loops need to be run twice each to remove empty array elements
	for x in pitchers["home"]:
		if "_EMPTY_" in x:
			pitchers["home"].remove(x)
	for x in pitchers["home"]:
		if "_EMPTY_" in x:
			pitchers["home"].remove(x)
	for x in pitchers["away"]:
		if "_EMPTY_" in x:
			pitchers["away"].remove(x)
	for x in pitchers["away"]:
		if "_EMPTY_" in x:
			pitchers["away"].remove(x)

	# Pitchers 5 through 9 are relief pitchers
	for x in range(5, 9):
		relief_pitchers["home"][x - 5] = pitchers["home"][x]
		relief_pitchers["away"][x - 5] = pitchers["away"][x]

	return relief_pitchers

def LoadClosers(abbrs, years):

	home_page = cloudscraper.create_scraper().get(
			"https://www.baseball-reference.com/teams/" + abbrs["home"]  + "/" + years["home"] + ".shtml"
		)
	home_tree = html.fromstring(home_page.content)
	away_page = cloudscraper.create_scraper().get(
			"https://www.baseball-reference.com/teams/" + abbrs["away"]  + "/" + years["away"] + ".shtml"
		)
	away_tree = html.fromstring(away_page.content)

	###########################################################
	# Scrape top 12 pitchers and earned run averages for specified team/year
	# A third column was added so that we can store pitcher's stats
	pitchers = {"home": 
					[
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]]
					], 
				"away": 
					[
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]],
						[[""], [0], [""]]
					]
				}

	# A third column was added so that we can store pitcher's stats
	relief_pitchers = {"home": [[[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]]], "away": [[[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]], [[""], [0], [""]]]}

	closers = {"home": ["", 0, ""], "away": ["", 0, ""]}


	# Scrape names and Earned Run Averages of top 12 pitchers
	# (Some extras because there are a variable number of blank/header lines mixed in)
	for x in range(12):
		# Home
		if x <= 4:
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath('//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 1) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

		if x > 4 and x <= 9:
			# Home
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'"))
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 2) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

		if x > 9:
			# Home
			fullname = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[1]"
								)[0].text_content().strip()
			position = home_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Home closer detected
					closers["home"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					closers["home"][1] = float(str(era).strip("[]'"))
					closers["home"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'"))
					pitchers["home"][x][0] = "_EMPTY_"
				else:
					# Not closer
					pitchers["home"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = home_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["home"][x][1] = float(str(era).strip("[]'"))
					pitchers["home"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["home"][x][0] = "_EMPTY_"

			# Away
			fullname = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[1]"
								)[0].text_content().strip()
			position = away_tree.xpath(
				'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[3]"
								)[0].text_content().strip()
			if str(fullname).strip("[],'") != "":
				fname = str(fullname).split()[0].replace("*", "").replace("#", "")
				lname = str(fullname).split()[1].replace("*", "").replace("#", "")
				if str(position).strip("[],'") == "CL":
					# Away closer detected
					closers["away"][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					closers["away"][1] = float(str(era).strip("[]'"))
					closers["away"][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
					pitchers["away"][x][0] = "_EMPTY_"
				else:  # Not closer
					pitchers["away"][x][0] = fname.strip("[],'") + " " + lname.strip("[],'")
					era = away_tree.xpath(
						'//table[@id="players_standard_pitching"]//tbody//tr[' + str(x + 3) + "]//td[8]"
								)[0].text_content().strip()
					pitchers["away"][x][1] = float(str(era).strip("[]'"))
					pitchers["away"][x][2] = pitcher_i(fname.strip("[],'"), lname.strip("[],'")) # Pitcher's stats
			else:
				# Blank/header line
				pitchers["away"][x][0] = "_EMPTY_"

	# For some reason, these loops need to be run twice each to remove empty array elements
	for x in pitchers["home"]:
		if "_EMPTY_" in x:
			pitchers["home"].remove(x)
	for x in pitchers["home"]:
		if "_EMPTY_" in x:
			pitchers["home"].remove(x)
	for x in pitchers["away"]:
		if "_EMPTY_" in x:
			pitchers["away"].remove(x)
	for x in pitchers["away"]:
		if "_EMPTY_" in x:
			pitchers["away"].remove(x)

	# Pitchers 5 through 9 are relief pitchers
	for x in range(5, 9):
		relief_pitchers["home"][x - 5] = pitchers["home"][x]
		relief_pitchers["away"][x - 5] = pitchers["away"][x]

	return closers
