import pandas as pd

import data

dataset = pd.DataFrame(data.people_data)

#================Functions=============
# Questão
def add_person(data: pd.DataFrame, name: str, age: int, city: str, hobbies: list) -> pd.DataFrame:
	"""Adds person to the dataframe

	Keyword arguments:
	data -- the dataframe to add the person to
	name -- the name of the person
	age -- the age of the person
	city -- the city of the person
	hobbies -- a list of the person's hobbies
	"""
	if not data.loc[data["name"] == name].empty:
		print("Já há uma pessoa com esse nome no dataframe")
		return data
	
	try:
		if (age < 0) or (age > 100):
			raise ValueError
		if not isinstance(city, str):
			raise TypeError
		if len(hobbies) == 0:
			raise ValueError
	except ValueError:
		if len(hobbies) == 0:
			print("A lista de hobbies não pode ser vazia")
		else:
			print("A idade não pode ser maior que 100 ou menor do que 0")
		return data
	except TypeError:
		print("O nome da cidade deve ser do tipo string")
		return data

	data.loc[len(data.index)] = [name, age, city, hobbies]

	return data

	

#============Tests====================
if __name__ == "__main__":
	# print(dataset["hobbies"])
	# # transformando coluna de hobbies em uma lista de listas com os hobbies
	# # para cada pessoa
	# hobbies_list = []
	# for registro in dataset["hobbies"]:
	# 	hobbies_list.append(list(registro))
	# print(hobbies_list)

	print(dataset)
	add_person(dataset, "Daniel", 18, "Belo Horizonte", ["music", "guitar"])
	print(dataset)