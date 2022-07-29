for i in range(2, 21):
    with open(f"tables/multiplication_of_table_of{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}")
            if j != 10:
                f.write('\n')

