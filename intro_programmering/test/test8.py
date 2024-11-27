input_text = input("skriv en kort text som inne håller minst ett A")
output_text = ""
for text in input_text:
    if text == "a":
        output_text += "e"
    else:
        output_text += text
    sak = ""
print(output_text)