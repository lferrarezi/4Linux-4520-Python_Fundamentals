while True:
    try:
        x = int(input("Insira um número a ser dividido (dividendo):\nx = "))
        y = int(input("Insira um número divisor:\ny = "))
        try:
            d = x / y
            r = x % y

            if r == 0:
                pass
            else:
                raise ValueError("ERRO: A conta deu resto")
        except ValueError as e:
            print(e)
        except ZeroDivisionError:
            print("Troque o valor de y, o divisor não pode ser 0")
        finally:
            print("Resultado: %s - resto: %s" %(d, r))

    except ValueError:
        print("Para divisões deve-se se usar apenas números")

