import pandas as pd

import data

dataset = pd.DataFrame(data.people_data)

#================Functions=============
# Questão 1
def add_person(data: pd.DataFrame, name: str, age: int, city: str, hobbies: list) -> pd.DataFrame:
	"""Add person to the dataframe

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

# Questão 2
def remove_person(data: pd.DataFrame, name: str) -> pd.DataFrame:
	"""Remove person from the dataframe

	:param pd.DataFrame data: Datagrame to modify
    :param str num2: Name of person to delete
    :rtype: pd.DataFrame
    :return: The data frame modified
	"""
	if not data[data["name"] == name].empty:
		# se o nome não está presente na coluna names
		
		# remove pelo índice do nome que bate  ocm a variável
		data.drop(data[data["name"] == name].index, inplace = True)

	return data

# questao 3
def get_ages(data: pd.DataFrame) -> tuple:
	"""Get ages max, min and mean

	:param pd.DataFrame data: Dataframe with the ages
	:rtype: tuple
	:return: Tuple with max min and mean of ages, in this order 
	"""
	
	ages = data["age"]
	max_age = ages.max()
	min_age = ages.min()
	mean_age = int(ages.mean())

	return (max_age, min_age, mean_age)

# questao 4
def get_hobbies(data: pd.DataFrame) -> set:
	"""Get the set of hobbies of dataframe

	:param pd.DataFrame data: Dataframe with hobbies
	:rtype: set
	:return: Set with all the hobbies in the dataframe
	"""
	# get the list of hobbies
	hobbies_list = data["hobbies"].to_list()
	
	# and return as set
	return set(hobbies_list)


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
	print(get_ages(dataset))
	add_person(dataset, "Daniel", 18, "Belo Horizonte", ["music", "guitar"])
	print(dataset)
	print(get_ages(dataset))
	remove_person(dataset, "Daniel")
	print(dataset)
	print(get_ages(dataset))
