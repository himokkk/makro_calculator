
def input_text(text):
    while True:
        try:
            result = input(text)
            result = result.replace(",", ".")
            result = float(result)
        except KeyboardInterrupt:
            exit(0)    
        except:
            continue 
        else:
            break
    return result

weight = input_text("Put food weight [g]: ")
kcal = input_text("Put kcal [kcal/100g]: ")
carbs = input_text("Put carbs [kcal/100g]: ")
protein = input_text("Put protein [kcal/100g]: ")
fat = input_text("Put fat [kcal/100g]: ")

total_kcal_from_kcal= kcal * weight / 100
total_kcal_from_makro = (carbs * 4 + protein * 4 + fat * 9) * weight / 100
total_carbs = carbs * weight / 100
total_protein = protein * weight / 100
total_fat = fat * weight / 100

kcal_from_kcal_text = f"Kcal from kcal: {total_kcal_from_kcal}"
kcal_from_makro_text = f"Kcal from makro: {total_kcal_from_makro}"
makro_text = f"Fats Carbs Prot: {total_fat} / {total_carbs} / {total_protein}"

print("\n")
print("-"*40)
print(kcal_from_kcal_text)
print(kcal_from_makro_text)
print(makro_text)
print("-"*40)
print("\n")
