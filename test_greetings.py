def test_greeting():

    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    assert output == "Привет, Анна! Тебе 25 лет."
